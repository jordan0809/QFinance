import math
import numpy as np

def num_feasible(N,m):
    """Number of feasible solutions given the number of assets N and the resolution m"""
    return (math.factorial(2**m+N-2)/math.factorial(2**m-1))/math.factorial(N-1)

def ideal_iterations(N,m):
    '''Optimal number of Grover iterations for amplitude amplification.'''
    return int(np.pi/4*(2**(N*m)/num_feasible(N,m))**0.5)

def generate_correlation_matrix(d):
    """
    Generate a symmetric, positive definite correlation matrix using a recursive 
    geometric approach.

    This method samples from a beta distribution to build the matrix row-by-row 
    while maintaining the positive definiteness required for portfolio covariance.

    Args:
        d (int): The dimension (number of assets) of the matrix.

    Returns:
        np.ndarray: A d x d symmetric positive definite correlation matrix.
        
    Source: https://stats.stackexchange.com/q/125017
    """
    S = np.eye(1)
    for k in range(2, d+1):
        y = np.random.beta(a=(k-1)/2, b=(d+1-k)/2)     # sampling from beta distribution
        r = math.sqrt(y)
        theta = np.random.randn(k-1, 1)
        theta = theta/np.linalg.norm(theta)
        w = r*theta
        E,U = np.linalg.eig(S)
        R = U @ np.diag(E**(1/2)) @ np.transpose(U)    # R is a square root of S
        q = R @ w
        S = np.vstack((
                np.hstack((S, q)),
                np.hstack((np.transpose(q), [[1]]))))  # increasing the matrix size
    return S