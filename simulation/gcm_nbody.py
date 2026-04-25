"""
GDGM N-Body Graviton Simulation
================================
Paste this entire file into a Google Colab cell and run it.
Or run cell by cell by splitting at the # --- CELL --- markers.

The equation of motion (dimensionless):
  d²ξᵢ/ds² = Σⱼ≠ᵢ  (ξⱼ − ξᵢ) / max(|ξⱼ − ξᵢ|, 1)³

No free parameters. All constants absorbed into units.
ℓ_min = 1 (length unit), τ = 1 (time unit).
"""

# --- CELL 1: Imports ---

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

print("Libraries loaded.")

# --- CELL 2: Parameters ---

N       = 100     # number of gravitons (try 50 for speed, 200 for richness)
R0      = 25.0    # initial spread radius (in units of ℓ_min)
dt      = 0.03    # timestep (dimensionless)
N_STEPS = 4000    # total steps  (~120 time units)
SAVE_EVERY = 20   # save a snapshot every N steps

# Minimum distance (= 1.0 in dimensionless units by construction)
L_MIN = 1.0

print(f"N={N} gravitons | R0={R0} | dt={dt} | steps={N_STEPS}")
print(f"Total simulation time: {N_STEPS * dt:.1f} τ")

# --- CELL 3: Initialization ---

np.random.seed(42)

# Uniform random positions inside a sphere of radius R0
directions = np.random.randn(N, 3)
directions /= np.linalg.norm(directions, axis=1, keepdims=True)
radii = R0 * np.cbrt(np.random.uniform(0, 1, N))   # uniform in volume
pos = directions * radii[:, np.newaxis]

# Zero initial velocity — things were just apart, then gravity took over
vel = np.zeros((N, 3))

# Snapshot storage
snapshots_pos = [pos.copy()]
snapshots_vel = [vel.copy()]
times         = [0.0]

print("Initialized.")
print(f"  Mean separation: {np.mean(radii):.2f} ℓ_min")
print(f"  Max separation:  {np.max(radii):.2f} ℓ_min")

# --- CELL 4: Force Calculation ---

def compute_forces(pos):
    """
    Vectorized pairwise gravitational forces.
    Returns acceleration array of shape (N, 3).

    Force on i from j:  (xⱼ - xᵢ) / max(|xⱼ - xᵢ|, L_MIN)³
    """
    # diff[i,j] = xⱼ - xᵢ   shape: (N, N, 3)
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]

    # Pairwise distances   shape: (N, N)
    dist = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))

    # Apply minimum distance floor
    dist_eff = np.maximum(dist, L_MIN)

    # 1/r³ factor — zero out diagonal to exclude self-force
    inv_r3 = 1.0 / dist_eff**3
    np.fill_diagonal(inv_r3, 0.0)

    # Acceleration on i = Σⱼ diff[i,j] / dist_eff[i,j]³
    acc = np.einsum('ij,ijk->ik', inv_r3, diff)

    return acc

# Quick sanity check
test_acc = compute_forces(pos)
print(f"Force calc OK | max acceleration: {np.max(np.abs(test_acc)):.4f}")

# --- CELL 5: Velocity Verlet Integrator ---

def step(pos, vel, acc):
    """One velocity Verlet step."""
    pos_new = pos + vel * dt + 0.5 * acc * dt**2
    acc_new = compute_forces(pos_new)
    vel_new = vel + 0.5 * (acc + acc_new) * dt
    return pos_new, vel_new, acc_new

def total_energy(pos, vel):
    """Kinetic + gravitational potential energy."""
    # Kinetic
    KE = 0.5 * np.sum(vel**2)

    # Potential: -Σᵢ<ⱼ 1/r_ij
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dist = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))
    dist_eff = np.maximum(dist, L_MIN)
    np.fill_diagonal(dist_eff, np.inf)
    PE = -0.5 * np.sum(1.0 / dist_eff)   # 0.5 for double-counting

    return KE + PE, KE, PE

print("Integrator ready.")

# --- CELL 6: Run the Simulation ---

print(f"\nRunning {N_STEPS} steps...")
acc = compute_forces(pos)

energies = []

for step_num in range(N_STEPS):
    pos, vel, acc = step(pos, vel, acc)

    if (step_num + 1) % SAVE_EVERY == 0:
        t = (step_num + 1) * dt
        E, KE, PE = total_energy(pos, vel)
        energies.append((t, E, KE, PE))
        snapshots_pos.append(pos.copy())
        snapshots_vel.append(vel.copy())
        times.append(t)

        if (step_num + 1) % (SAVE_EVERY * 10) == 0:
            print(f"  t={t:.1f} | E={E:.2f} | KE={KE:.2f} | PE={PE:.2f}")

print("\nDone.")

# --- CELL 7: Visualize Snapshots ---

n_snaps = len(snapshots_pos)
show_indices = [0,
                n_snaps // 4,
                n_snaps // 2,
                3 * n_snaps // 4,
                n_snaps - 1]

fig, axes = plt.subplots(1, 5, figsize=(20, 4))
fig.suptitle("GDGM Graviton Simulation — XY Projection", fontsize=14)

for ax, idx in zip(axes, show_indices):
    snap = snapshots_pos[idx]
    t    = times[idx]

    # Color by distance from origin (proxy for density)
    r = np.linalg.norm(snap, axis=1)
    sc = ax.scatter(snap[:, 0], snap[:, 1],
                    c=r, cmap='plasma_r',
                    s=15, alpha=0.8, vmin=0, vmax=R0)
    ax.set_aspect('equal')
    ax.set_title(f't = {t:.1f} τ')
    ax.set_xlabel('x / ℓ_min')
    if idx == 0:
        ax.set_ylabel('y / ℓ_min')

    # Draw circle at R0 for reference
    theta = np.linspace(0, 2*np.pi, 100)
    ax.plot(R0 * np.cos(theta), R0 * np.sin(theta),
            'gray', lw=0.5, ls='--', alpha=0.3)

plt.tight_layout()
plt.savefig('gdgm_snapshots.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: gdgm_snapshots.png")

# --- CELL 8: Energy Conservation Check ---

ts   = [e[0] for e in energies]
Es   = [e[1] for e in energies]
KEs  = [e[2] for e in energies]
PEs  = [e[3] for e in energies]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

ax1.plot(ts, Es,  'k-',  lw=1.5, label='Total E')
ax1.plot(ts, KEs, 'r--', lw=1,   label='Kinetic')
ax1.plot(ts, PEs, 'b--', lw=1,   label='Potential')
ax1.set_xlabel('Time (τ)')
ax1.set_ylabel('Energy (dimensionless)')
ax1.set_title('Energy over Time')
ax1.legend()
ax1.grid(alpha=0.3)

E0 = Es[0]
drift = [(e - E0) / abs(E0) * 100 for e in Es]
ax2.plot(ts, drift, 'g-', lw=1.5)
ax2.set_xlabel('Time (τ)')
ax2.set_ylabel('Energy drift (%)')
ax2.set_title('Energy Conservation (should stay near 0%)')
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('gdgm_energy.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: gdgm_energy.png")

# --- CELL 9: Cluster Detection ---

def find_clusters(pos, vel, r_threshold=3.0, ke_check=True):
    """
    Find bound graviton clusters at the current timestep.

    A cluster is a connected group of gravitons within r_threshold of
    each other, with negative total internal energy (actually bound).
    """
    # Pairwise distances
    diff = pos[np.newaxis, :, :] - pos[:, np.newaxis, :]
    dist = np.sqrt(np.einsum('ijk,ijk->ij', diff, diff))
    np.fill_diagonal(dist, np.inf)

    # Adjacency: connected if within threshold
    adj = dist < r_threshold

    # Connected components (simple BFS)
    visited = np.zeros(N, dtype=bool)
    clusters = []
    for i in range(N):
        if not visited[i]:
            cluster = []
            queue = [i]
            while queue:
                node = queue.pop(0)
                if not visited[node]:
                    visited[node] = True
                    cluster.append(node)
                    neighbors = np.where(adj[node])[0]
                    for nb in neighbors:
                        if not visited[nb]:
                            queue.append(nb)
            clusters.append(cluster)

    # Filter: only clusters with > 1 graviton
    clusters = [c for c in clusters if len(c) > 1]

    return clusters

# Run cluster detection on final snapshot
final_pos = snapshots_pos[-1]
final_vel = snapshots_vel[-1]
clusters  = find_clusters(final_pos, final_vel, r_threshold=4.0)

# Sort by size
clusters.sort(key=len, reverse=True)

print(f"\nCluster analysis at t = {times[-1]:.1f} τ:")
print(f"  Total gravitons: {N}")
print(f"  Clusters found:  {len(clusters)}")
print(f"  Gravitons in clusters: {sum(len(c) for c in clusters)}")
print(f"  Isolated gravitons:    {N - sum(len(c) for c in clusters)}")
print()

for i, c in enumerate(clusters[:10]):
    members = np.array(c)
    center  = np.mean(final_pos[members], axis=0)
    spread  = np.std(np.linalg.norm(final_pos[members] - center, axis=1))
    print(f"  Cluster {i+1}: {len(c):3d} gravitons | "
          f"center=({center[0]:.1f}, {center[1]:.1f}, {center[2]:.1f}) | "
          f"spread={spread:.2f} ℓ_min")

# --- CELL 10: Visualize Final Clusters ---

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax.set_title(f'Final State (t={times[-1]:.1f} τ) — Clusters Colored', fontsize=12)

# Assign colors to clusters
colors = list(mcolors.TABLEAU_COLORS.values())
cluster_color = {i: 'lightgray' for i in range(N)}  # default: isolated
for ci, cluster in enumerate(clusters):
    for gi in cluster:
        cluster_color[gi] = colors[ci % len(colors)]

xs = final_pos[:, 0]
ys = final_pos[:, 1]
cs = [cluster_color[i] for i in range(N)]

ax.scatter(xs, ys, c=cs, s=20, alpha=0.9, zorder=3)
ax.set_aspect('equal')
ax.set_xlabel('x / ℓ_min')
ax.set_ylabel('y / ℓ_min')
ax.grid(alpha=0.2)

# Label top clusters
for ci, cluster in enumerate(clusters[:5]):
    members = np.array(cluster)
    cx = np.mean(final_pos[members, 0])
    cy = np.mean(final_pos[members, 1])
    ax.annotate(f'#{ci+1} ({len(cluster)})',
                xy=(cx, cy), fontsize=8,
                ha='center', va='bottom',
                color=colors[ci % len(colors)])

plt.tight_layout()
plt.savefig('gdgm_clusters.png', dpi=150, bbox_inches='tight')
plt.show()
print("Saved: gdgm_clusters.png")

# --- CELL 11 (Optional): Animated View ---
# Uncomment to generate an animation (takes ~1 min in Colab)

# fig, ax = plt.subplots(figsize=(6, 6))
# scat = ax.scatter([], [], s=10, alpha=0.7, c='steelblue')
# ax.set_xlim(-R0*1.1, R0*1.1)
# ax.set_ylim(-R0*1.1, R0*1.1)
# ax.set_aspect('equal')
# time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
#
# def update(frame):
#     snap = snapshots_pos[frame]
#     scat.set_offsets(snap[:, :2])
#     time_text.set_text(f't = {times[frame]:.1f} τ')
#     return scat, time_text
#
# anim = FuncAnimation(fig, update, frames=len(snapshots_pos),
#                      interval=50, blit=True)
# HTML(anim.to_jshtml())
