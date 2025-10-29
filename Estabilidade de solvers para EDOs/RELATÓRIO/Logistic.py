class Logistic:
    def __init__(self, alpha, R):
        self.alpha = alpha
        self.R = R

    def __call__(self, t, u):
        return self.alpha * u * (1 - u / self.R)

