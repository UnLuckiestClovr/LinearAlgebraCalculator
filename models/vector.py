import numpy as np
from fractions import Fraction

class Vector:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = np.array(data)
            self.length = self.data.shape[0]
        elif isinstance(data, np.ndarray):
            self.data = data
            self.length = self.data.shape[0]
        else:
            raise TypeError("Invalid data type for Vector")

    def pythagorean_theorem(self, values: np.ndarray) -> float:
        return np.sqrt(np.sum(np.array(values) ** 2))

