# Quantum Algorithms for Financial Applications

This repository implements quantum algorithms for financial problems, including portfolio optimization and option pricing with CUDA-Q.

For information on installing the CUDA-Q package, please refer to the official documentation: https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html

### GM-QAOA for Portfolio Optimization
In `GM_QAOA_Portfolio.ipynb`, I implement the Grover-Mixer QAOA (GM-QAOA). This approach combines the structure of Grover Adaptive Search with the Quantum Alternating Operator Ansatz (QAOA) to solve constrained optimization problems.

#### How it works:

- Constraint Satisfaction: Instead of using a standard mixer that explores the entire Hilbert space, the Grover-Mixer projects the search onto the feasible subspace (solutions that satisfy the budget constraint).

- Optimization: The QAOA layers then evolve the state within this subspace to minimize the financial objective function (risk/return). 

### QAE for European Option Pricing
In `QAE_OptionPricing.ipynb`, I implement Quantum Amplitude Estimation (QAE) to price a European call option. This approach utilizes a Quantum Monte Carlo simulation to achieve a quadratic speedup over classical methods.

#### How it works:

- State Preparation: The algorithm begins by loading a normal distribution into a quantum state using the Grover-Rudolph method. This represents the discretized probability function $p_T(x)$ of the stock price at maturity.

- Payoff Encoding: The European option payoff function $f(S_T) = \max(S_T - K, 0)$ is mapped onto the amplitude of an ancilla qubit. This is achieved through a series of controlled RY-rotations.

- Amplitude Estimation: Instead of direct sampling, I utilize the Grover rotation operator $Q$ and Quantum Phase Estimation (QPE). By measuring the phase $\theta$ of the eigenvalues of $Q$, we can infer the expectation value $\mathbb{E}[f(S_T)]$ with high precision.

- Validation: The final discounted price $V_0 = e^{-rT}\mathbb{E}[f(S_T)]$ is validated against the analytical solution of the Black-Scholes model.