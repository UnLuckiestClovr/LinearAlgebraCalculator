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

    def magnitude(self) -> float:
        return self.pythagorean_theorem(self.data)
    
    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot compute unit vector of zero vector")
        return Vector(self.data / mag)
    
    def addition(self, other):
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for addition")
        
        self.data += other.data
        return self
    
    def subtraction(self, other):
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for subtraction")
        
        self.data -= other.data
        return self
    
    def scalar_multiplication(self, scalar: float):
        self.data *= scalar
        return self
    
    def scalar_division(self, scalar: float):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        
        self.data /= scalar
        return self
    
    