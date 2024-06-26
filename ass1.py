class MathTools:
    def __init__(self):
        self.total_calls = 0
    
    def derivative(self, func, x, h=1e-7):
        self.total_calls += 1
        return (func(x + h) - func(x)) / h
    
    def gradient(self, func, point, h=1e-7):
        self.total_calls += 1
        grad = []
        for i in range(len(point)):
            def func_partial(xi):
                point_copy = point[:]
                point_copy[i] = xi
                return func(point_copy)
            grad.append((func_partial(point[i] + h) - func_partial(point[i])) / h)
        return grad
