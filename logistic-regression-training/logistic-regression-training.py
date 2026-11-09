import numpy as np

def _sigmoid(z: np.ndarray) -> np.ndarray:
    """
    Returns elementwise sigmoid values.
    """
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X: np.ndarray, y: np.ndarray, lr: float = 0.1, steps: int = 1000) -> tuple[np.ndarray, float]:
    """
    Returns the trained weights and bias as (w, b).
    """
    N,D = X.shape
    w,b = np.zeros(D),0.0
    while steps>0:
        preds = _sigmoid(X@w + b)
        #loss = compute_loss(y, preds, N)
        grad_w = np.dot(X.T, (preds - y))/N
        grad_b = np.mean(preds-y)
        w -= lr * grad_w   
        b -= lr * grad_b
        steps-=1
    return (w,b)