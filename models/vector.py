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
    
    def dot_product(self, other) -> float:
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for dot product")
        
        dp = 0.0
        for i in range(self.length):
            dp += self.data[i] * other.data[i]

        return dp
    
    def angle_between(self, other) -> float:
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for angle calculation")
        
        dot_prod = self.dot_product(other)

        mag_self = self.magnitude()
        mag_other = other.magnitude()

        if mag_self != 0 and mag_other != 0:
            cos_angle = dot_prod / (mag_self * mag_other)
            cos_angle = max(min(cos_angle, 1.0), -1.0)  # Clamp value to avoid numerical issues
            return np.arccos(cos_angle)
        else:
            raise ValueError("Cannot calculate angle with zero magnitude vector")
        
    def projection_onto(self, other):
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for projection")
        
        other_unit = other.unit_vector()
        scalar_proj = self.dot_product(other_unit)
        proj_vector = other_unit.scalar_multiplication(scalar_proj)
        
        return proj_vector

    def finding_projection_parallelandorthogonal(self, other):
        if self.length != other.length:
            raise ValueError("Vectors must be of the same length for projection")
        
        parallel_comp = self.projection_onto(other)
        orthogonal_comp = Vector(self.data - parallel_comp.data)
        
        return parallel_comp, orthogonal_comp
    
    def cross_product(self, other):
        if self.length != 3 or other.length != 3:
            raise ValueError("Cross product is only defined for 3-dimensional vectors")
        
        output = Vector([
            self.data[1] * other.data[2] - self.data[2] * other.data[1],
            self.data[2] * other.data[0] - self.data[0] * other.data[2],
            self.data[0] * other.data[1] - self.data[1] * other.data[0]
        ])

        return output