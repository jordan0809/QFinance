# Quantum Algorithms for Financial Applications

This repository implements quantum algorithms for financial problems, including portfolio optimization and option pricing with CUDA-Q.

For information on installing the CUDA-Q package, please refer to the official documentation: https://nvidia.github.io/cuda-quantum/latest/using/quick_start.html

### GM-QAOA for Portfolio Optimization
In `GM_QAOA_Portfolio.ipynb`, I implement the Grover-Mixer QAOA (GM-QAOA). This approach combines the structure of Grover Adaptive Search with the Quantum Alternating Operator Ansatz (QAOA) to solve constrained optimization problems.

#### How it works:

- Constraint Satisfaction: Instead of using a standard mixer that explores the entire Hilbert space, the Grover-Mixer projects the search onto the feasible subspace (solutions that satisfy the budget constraint).

- Optimization: The QAOA layers then evolve the state within this subspace to minimize the financial objective function (risk/return). 