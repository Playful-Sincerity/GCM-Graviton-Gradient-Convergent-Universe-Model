#!/usr/bin/env python3
"""Print tool versions for output headers."""
import sys
try:
    import sympy
    sympy_v = sympy.__version__
except ImportError:
    sympy_v = "not installed"
try:
    import mpmath
    mpmath_v = mpmath.__version__
except ImportError:
    mpmath_v = "not installed"
print(f"Python {sys.version.split()[0]} / SymPy {sympy_v} / mpmath {mpmath_v}")
