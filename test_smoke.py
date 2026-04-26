"""
Smoke tests for GCM N-Body Graviton Simulation.

Validates:
- Python file has no syntax errors (compiles successfully)
- Core functions (compute_forces, step, total_energy, find_clusters) work on small inputs
- Energy conservation holds for a short integration
- Cluster detection returns sensible results

Run:  python3 -m pytest test_smoke.py -v
  or: python3 test_smoke.py
"""

import ast
import os
import sys
import unittest
import importlib.util
import types

import numpy as np

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
NBODY_PATH = os.path.join(PROJECT_ROOT, "simulation", "gcm_nbody.py")


def _load_functions_from_source(filepath):
    """
    Parse the simulation file and extract function definitions + constants
    without executing top-level code (which runs the full simulation and
    opens matplotlib windows).

    Returns a module-like namespace with the functions and constants injected.
    """
    with open(filepath, "r") as f:
        source = f.read()

    tree = ast.parse(source, filename=filepath)

    # Build a minimal module with only imports, constants, and function defs
    # (skip bare expressions, print calls, and matplotlib/IPython usage)
    safe_nodes = []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            # Skip IPython import — not needed for tests
            if isinstance(node, ast.ImportFrom) and node.module and "IPython" in node.module:
                continue
            safe_nodes.append(node)
        elif isinstance(node, ast.FunctionDef):
            safe_nodes.append(node)
        elif isinstance(node, ast.Assign):
            # Only keep simple constant assignments (not snapshot lists, etc.)
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            constants = {"N", "R0", "dt", "N_STEPS", "SAVE_EVERY", "L_MIN"}
            if any(t in constants for t in targets):
                safe_nodes.append(node)

    new_tree = ast.Module(body=safe_nodes, type_ignores=[])
    ast.fix_missing_locations(new_tree)
    code = compile(new_tree, filepath, "exec")

    mod = types.ModuleType("gcm_nbody")
    mod.__file__ = filepath
    # Provide a non-interactive matplotlib backend before exec
    import matplotlib
    matplotlib.use("Agg")
    exec(code, mod.__dict__)
    return mod


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------


class TestSyntax(unittest.TestCase):
    """The simulation file should compile without syntax errors."""

    def test_nbody_compiles(self):
        with open(NBODY_PATH, "r") as f:
            source = f.read()
        # compile() raises SyntaxError on bad syntax
        compile(source, NBODY_PATH, "exec")


class TestCoreFunctions(unittest.TestCase):
    """Core simulation functions should work on small inputs."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_functions_from_source(NBODY_PATH)
        # Override N for test purposes
        cls.mod.N = 5

    def _make_positions(self, n=5):
        np.random.seed(0)
        return np.random.randn(n, 3) * 5.0

    def test_compute_forces_shape(self):
        pos = self._make_positions()
        acc = self.mod.compute_forces(pos)
        self.assertEqual(acc.shape, (5, 3))

    def test_compute_forces_no_nan(self):
        pos = self._make_positions()
        acc = self.mod.compute_forces(pos)
        self.assertFalse(np.any(np.isnan(acc)), "Acceleration contains NaN")

    def test_compute_forces_zero_self_force(self):
        """A single particle should have zero acceleration."""
        self.mod.N = 1
        pos = np.array([[1.0, 2.0, 3.0]])
        acc = self.mod.compute_forces(pos)
        np.testing.assert_array_equal(acc, np.zeros((1, 3)))
        self.mod.N = 5  # restore

    def test_step_returns_correct_shapes(self):
        pos = self._make_positions()
        vel = np.zeros_like(pos)
        acc = self.mod.compute_forces(pos)
        pos2, vel2, acc2 = self.mod.step(pos, vel, acc)
        self.assertEqual(pos2.shape, (5, 3))
        self.assertEqual(vel2.shape, (5, 3))
        self.assertEqual(acc2.shape, (5, 3))

    def test_total_energy_returns_three_values(self):
        pos = self._make_positions()
        vel = np.zeros_like(pos)
        result = self.mod.total_energy(pos, vel)
        self.assertEqual(len(result), 3, "Expected (E_total, KE, PE)")

    def test_total_energy_zero_velocity_no_kinetic(self):
        pos = self._make_positions()
        vel = np.zeros_like(pos)
        E, KE, PE = self.mod.total_energy(pos, vel)
        self.assertAlmostEqual(KE, 0.0, places=10)
        self.assertLess(PE, 0.0, "Potential energy should be negative")

    def test_energy_conservation_short_run(self):
        """Energy should be approximately conserved over a short integration."""
        pos = self._make_positions()
        vel = np.zeros_like(pos)
        acc = self.mod.compute_forces(pos)

        E0, _, _ = self.mod.total_energy(pos, vel)

        # Run 50 steps
        for _ in range(50):
            pos, vel, acc = self.mod.step(pos, vel, acc)

        E_final, _, _ = self.mod.total_energy(pos, vel)

        # Allow up to 5% drift for such a short test
        if abs(E0) > 1e-10:
            drift = abs((E_final - E0) / E0)
            self.assertLess(drift, 0.05,
                            f"Energy drifted {drift*100:.1f}% (limit: 5%)")


class TestClusterDetection(unittest.TestCase):
    """Cluster detection should return sensible results."""

    @classmethod
    def setUpClass(cls):
        cls.mod = _load_functions_from_source(NBODY_PATH)

    def test_two_nearby_particles_form_cluster(self):
        self.mod.N = 3
        # Two particles close together, one far away
        pos = np.array([
            [0.0, 0.0, 0.0],
            [0.5, 0.0, 0.0],
            [100.0, 100.0, 100.0],
        ])
        vel = np.zeros_like(pos)
        clusters = self.mod.find_clusters(pos, vel, r_threshold=3.0)
        # Should find exactly one cluster of size 2
        self.assertEqual(len(clusters), 1)
        self.assertEqual(len(clusters[0]), 2)

    def test_all_far_apart_no_clusters(self):
        self.mod.N = 3
        pos = np.array([
            [0.0, 0.0, 0.0],
            [100.0, 0.0, 0.0],
            [0.0, 100.0, 0.0],
        ])
        vel = np.zeros_like(pos)
        clusters = self.mod.find_clusters(pos, vel, r_threshold=3.0)
        self.assertEqual(len(clusters), 0, "No clusters expected when all particles are far apart")


class TestRequirements(unittest.TestCase):
    """requirements.txt should be valid and parseable."""

    def test_requirements_file_exists(self):
        req_path = os.path.join(PROJECT_ROOT, "requirements.txt")
        self.assertTrue(os.path.isfile(req_path))

    def test_requirements_has_numpy_and_matplotlib(self):
        req_path = os.path.join(PROJECT_ROOT, "requirements.txt")
        with open(req_path, "r") as f:
            content = f.read().lower()
        self.assertIn("numpy", content)
        self.assertIn("matplotlib", content)


if __name__ == "__main__":
    unittest.main()
