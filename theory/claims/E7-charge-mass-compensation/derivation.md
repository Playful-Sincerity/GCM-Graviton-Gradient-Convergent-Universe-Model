# E7 — Derivation

## Starting Point — The Bohr Ground-State Energy

The hydrogen ground-state energy in the non-relativistic Bohr model is:

$$E_1 = -\frac{m_e k^2 e^4}{2 \hbar^2}$$

where $m_e$ is the electron mass, $e$ is the elementary charge, $k = 1/(4\pi\epsilon_0)$ is the Coulomb constant, and $\hbar$ is the reduced Planck constant. Numerical value: $E_1 = -13.6$ eV.

## Partial Derivatives

Treat $E_1$ as a function of two parameters $(e, m_e)$ with $k$ and $\hbar$ fixed. Compute the two partial derivatives.

$$\frac{\partial E_1}{\partial e} = -\frac{m_e k^2 \cdot 4 e^3}{2 \hbar^2} = \frac{4 E_1}{e}$$

$$\frac{\partial E_1}{\partial m_e} = -\frac{k^2 e^4}{2 \hbar^2} = \frac{E_1}{m_e}$$

(Each is obtained by differentiating the closed-form expression and then identifying the result with $E_1$ divided by the varied parameter and multiplied by the appropriate power.)

## Perturbation Condition

For the ground-state energy to remain invariant under simultaneous shifts $\Delta e$ and $\Delta m_e$:

$$\Delta E_1 = \frac{\partial E_1}{\partial e} \Delta e + \frac{\partial E_1}{\partial m_e} \Delta m_e = 0$$

Substituting the partial derivatives:

$$\frac{4 E_1}{e} \Delta e + \frac{E_1}{m_e} \Delta m_e = 0$$

Divide through by $E_1$ (nonzero):

$$\frac{4 \Delta e}{e} + \frac{\Delta m_e}{m_e} = 0 \quad \Longrightarrow \quad \boxed{\frac{\Delta m_e}{m_e} = -4 \cdot \frac{\Delta e}{e}}$$

## Interpretation of the Ratio

The ratio $-4$ comes from the exponent of $e$ in $E_1$ (which is $+4$) compared to the exponent of $m_e$ (which is $+1$). Any observable $X(e, m_e) \propto e^p \cdot m_e^q$ yields a constraint $\Delta m_e / m_e = -(p/q) \cdot \Delta e / e$. The Bohr energy's $e^4 \cdot m_e$ dependence gives $p/q = 4$.

## Dimensional Check

Both sides of the constraint are dimensionless ratios ($\Delta e / e$ and $\Delta m_e / m_e$). The prefactor $-4$ is dimensionless. ✓

## Worked Numerical Example

The session brief cites: $\Delta e = 10^{-35}$ C implies $\Delta m_e \approx -2.27 \times 10^{-46}$ kg.

Substituting $m_e = 9.10938 \times 10^{-31}$ kg and $e = 1.60218 \times 10^{-19}$ C:

$$\Delta m_e = -4 \cdot m_e \cdot \frac{\Delta e}{e} = -4 \cdot (9.10938 \times 10^{-31}) \cdot \frac{10^{-35}}{1.60218 \times 10^{-19}}$$

$$\Delta m_e \approx -2.2742 \times 10^{-46} \text{ kg}$$

Agrees with the brief's stated value to within rounding (0.2%).

## Limit Cases

- **$\Delta e \to 0$:** $\Delta m_e \to 0$. The constraint is satisfied trivially. ✓
- **$\Delta m_e \to 0$:** $\Delta e \to 0$. Same. ✓
- **$\Delta e \neq 0, \Delta m_e = 0$ (one changes, not the other):** the constraint is violated — $E_1$ shifts, so hydrogen spectroscopy would be sensitive to a floating charge with a fixed mass. This is precisely the empirical signature an emergent-parameter theory must avoid.

## Beyond Bohr

For a more complete treatment of hydrogen (Dirac, QED, hyperfine structure), additional parameters enter: $c$ (via the fine-structure constant $\alpha$), the proton-electron mass ratio, and the anomalous magnetic moment. Those extensions *modify* the ratio away from $-4$; the coherence paper should present E7 at the Bohr level and flag the extension as future work.
