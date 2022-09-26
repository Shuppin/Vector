"""
This module provides basic vector mathematical functionality
"""
from __future__ import annotations
import math


def distance(vec1: Vector, vec2: Vector) -> float:
    """
    Calculate the distance between 2 vectors

    Arguments:
    - `vec1` (Vector)
    - `vec2` (Vector)

    Returns:
    - `distance` (float)
    """
    if (isinstance(vec1, Vector3) and isinstance(vec2, Vector3)) or (isinstance(vec1, Vector2) and isinstance(vec2, Vector2)):
        return vec1.distance_to(vec2)
    else:
        raise TypeError(f"unsupported operand type(s) for <funciton 'distance'>: '{type(vec1).__name__}' and '{type(vec2).__name__}'")


def lerp(vec1: Vector, vec2: Vector, factor: float) -> Vector:
    """
    Linear interpolation of 2 vectors and a given factor

    Arguments:
    - `vec1` (Vector)
    - `vec2` (Vector)

    Returns:
    - `lerped_vec` (Vector)
    """
    if (isinstance(vec1, Vector3) and isinstance(vec2, Vector3)) or (isinstance(vec1, Vector2) and isinstance(vec2, Vector2)):
        return vec1.lerp(vec2, factor)
    else:
        raise TypeError(f"unsupported operand type(s) for <funciton 'lerp'>: '{type(vec1).__name__}' and '{type(vec2).__name__}'")


def dot(vec1: Vector, vec2: Vector) -> float:
    """
    Calculates the dot product of 2 vectors

    Arguments:
    - `vec1` (Vector)
    - `vec2` (Vector)

    Returns:
    - `dot_product` (float)
    """
    if (isinstance(vec1, Vector3) and isinstance(vec2, Vector3)) or (isinstance(vec1, Vector2) and isinstance(vec2, Vector2)):
        return vec1.dot(vec2)
    else:
        raise TypeError(f"unsupported operand type(s) for <funciton 'dot'>: '{type(vec1).__name__}' and '{type(vec2).__name__}'")


class Vector:
    """
    Serves as base class for other vector classes
    """
    pass


class Vector2(Vector):
    """
    This class provides a 2 dimensional vector type supporting basic math operations and more advanced vector operations such as `lerp()` and `dot()`
    """

    def __init__(self, x: float, y: float):
        if not self._isnum(x):
            raise TypeError(f"cannot convert value '{x}' to float")
        elif not self._isnum(y):
            raise TypeError(f"cannot convert value '{y}' to float")

        self.x = x
        self.y = y


    def __add__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            return Vector2(self.x+v2.x, self.y+v2.y)
        elif isinstance(v2, tuple) or isinstance(v2, list):
            if len(v2) == 2:
                return Vector2(self.x+v2[0], self.y+v2[1])
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v2).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(v2).__name__}'")


    def __iadd__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            self.x += v2.x
            self.y += v2.y
        elif isinstance(v2, tuple) or isinstance(v2, list):
            if len(v2) == 2:
                self.x += v2[0]
                self.y += v2[1]
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v2).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for +=: '{type(self).__name__}' and '{type(v2).__name__}'")
        return self


    def __sub__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            return Vector2(self.x-v2.x, self.y-v2.y)
        elif isinstance(v2, tuple) or isinstance(v2, list):
            if len(v2) == 2:
                return Vector2(self.x-v2[0], self.y-v2[1])
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v2).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(v2).__name__}'")


    def __isub__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            self.x -= v2.x
            self.y -= v2.y
        elif isinstance(v2, tuple) or isinstance(v2, list):
            if len(v2) == 2:
                self.x -= v2[0]
                self.y -= v2[1]
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v2).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v2).__name__}'")
        return self


    def __mul__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            return Vector2(self.x*v2.x, self.y*v2.y)
        elif self._isnum(v2):
            return Vector2(self.x*v2, self.y*v2)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v2).__name__}'")


    def __imul__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            self.x *= v2.x
            self.y *= v2.y
        elif self._isnum(v2):
            self.x *= v2
            self.y *= v2
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v2).__name__}'")
        return self


    def __truediv__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            return Vector2(self.x/v2.x, self.y/v2.y)
        elif self._isnum(v2):
            return Vector2(self.x/v2, self.y/v2)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v2).__name__}'")


    def __itruediv__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            self.x /= v2.x
            self.y /= v2.y
        elif self._isnum(v2):
            self.x /= v2
            self.y /= v2
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v2).__name__}'")
        return self


    def __floordiv__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            return Vector2(self.x//v2.x, self.y//v2.y)
        elif self._isnum(v2):
            return Vector2(self.x//v2, self.y//v2)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v2).__name__}'")


    def __ifloordiv__(self, v2) -> Vector2:
        if isinstance(v2, Vector2):
            self.x //= v2.x
            self.y //= v2.y
        elif self._isnum(v2):
            self.x //= v2
            self.y //= v2
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v2).__name__}'")
        return self


    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


    def _isnum(self, num) -> bool:
        """
        Check if given value is a number (float, decimal, complex etc..)
        
        Arguments:
        - `num` (number)

        Returns:
        - `is_num` (bool)
        """
        try:
            float(num)
        except ValueError:
            return False
        except TypeError:
            return False
        return True


    @classmethod
    def zero(cls):
        return cls(0, 0)


    @classmethod
    def one(cls):
        return cls(1, 1)


    @classmethod
    def two(cls):
        return cls(2, 2)


    def magnitude(self) -> float:
        """
        Returns:
        - `magnitude` (float): Magnitude of the vector
        """
        return math.sqrt(self.x**2+self.y**2)


    def norm(self) -> Vector2:
        """
        Returns:
        - `norm_vec` (Vector2): Normalised vector
        """
        if self.magnitude() == 0:
            raise ZeroDivisionError("Zero vector cannot be normalised")
        return self / self.magnitude()


    def normalise(self) -> Vector2:
        """
        Returns:
        - `norm_vec` (Vector2): Normalised vector
        """
        return self.norm()


    def lerp(self, v2: Vector2, factor: float) -> Vector2:
        """
        Linear interpolation between `self` and `v2`

        Arguments:
        - `v2` (Vector2): The end vector of the interpolation
        - `factor` (float): The factor of the interpolation

        Returns:
        - `lerp_vector` (Vector2)

        Example Usage:
        ```
        ------------------------
        v1 = Vector2(1, 1)
        v2 = Vector2(2, 2)
        v1.lerp(v2, 0.5)
        >>> (1.5, 1.5)
        ------------------------
        ```
        """
        return self + (v2 - self) * factor


    def distance_to(self, v2: Vector2) -> float:
        """
        Calculates the distance to `v2`

        Arguments:
        - `v2` (Vector2)

        Returns:
        - `distance` (float)
        """
        return math.sqrt((v2.x-self.x)**2 + (v2.y-self.y)**2)


    def dot(self, v2: Vector2) -> float:
        """
        Calculates the dot product of `self` and `v2`

        Arguments:
        - `v2` (Vector2)

        Returns:
        - `dot_product` (float)
        """
        return (self.x*v2.x)+(self.y*v2.y)


class Vector3(Vector):
    """
    This class provides a 3 dimensional vector type supporting basic math operations and more advanced vector operations such as `lerp()` and `dot()`
    """

    def __init__(self, x: float, y: float, z: float):
        if not self._isnum(x):
            raise TypeError(f"cannot convert value '{x}' to float")
        elif not self._isnum(y):
            raise TypeError(f"cannot convert value '{y}' to float")
        elif not self._isnum(z):
            raise TypeError(f"cannot convert value '{z}' to float")

        self.x = x
        self.y = y
        self.z = z


    def __add__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            return Vector3(self.x+v3.x, self.y+v3.y, self.z+v3.z)
        elif isinstance(v3, tuple) or isinstance(v3, list):
            if len(v3) == 3:
                return Vector3(self.x+v3[0], self.y+v3[1], self.z+v3[2])
            elif len(v3) == 2:
                return Vector3(self.x+v3[0], self.y+v3[1], self.z)
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v3).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(self).__name__}' and '{type(v3).__name__}'")


    def __iadd__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            self.x += v3.x
            self.y += v3.y
            self.z += v3.z
        elif isinstance(v3, tuple) or isinstance(v3, list):
            if len(v3) == 3:
                self.x += v3[0]
                self.y += v3[1]
                self.z += v3[2]
            elif len(v3) == 2:
                self.x += v3[0]
                self.y += v3[1]
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v3).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for +=: '{type(self).__name__}' and '{type(v3).__name__}'")
        return self


    def __sub__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            return Vector3(self.x-v3.x, self.y-v3.y, self.z-v3.z)
        elif isinstance(v3, tuple) or isinstance(v3, list):
            if len(v3) == 3:
                return Vector3(self.x-v3[0], self.y-v3[1], self.z-v3[2])
            elif len(v3) == 2:
                return Vector3(self.x-v3[0], self.y-v3[1], self.z)
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v3).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for -: '{type(self).__name__}' and '{type(v3).__name__}'")


    def __isub__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            self.x -= v3.x
            self.y -= v3.y
            self.z -= v3.z
        elif isinstance(v3, tuple) or isinstance(v3, list):
            if len(v3) == 3:
                self.x -= v3[0]
                self.y -= v3[1]
                self.z -= v3[2]
            elif len(v3) == 2:
                self.x -= v3[0]
                self.y -= v3[1]
            else:
                raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v3).__name__}'")
        else:
            raise TypeError(f"unsupported operand type(s) for -=: '{type(self).__name__}' and '{type(v3).__name__}'")
        return self


    def __mul__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            return Vector3(self.x*v3.x, self.y*v3.y, self.z*v3.z)
        elif self._isnum(v3):
            return Vector3(self.x*v3, self.y*v3, self.z*v3)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v3).__name__}'")


    def __imul__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            self.x *= v3.x
            self.y *= v3.y
            self.z *= v3.z
        elif self._isnum(v3):
            self.x *= v3
            self.y *= v3
            self.z *= v3
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v3).__name__}'")
        return self


    def __truediv__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            return Vector3(self.x/v3.x, self.y/v3.y, self.z/v3.z)
        elif self._isnum(v3):
            return Vector3(self.x/v3, self.y/v3, self.z/v3)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v3).__name__}'")


    def __itruediv__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            self.x /= v3.x
            self.y /= v3.y
            self.z /= v3.z
        elif self._isnum(v3):
            self.x /= v3
            self.y /= v3
            self.z /= v3
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v3).__name__}'")
        return self


    def __floordiv__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            return Vector3(self.x//v3.x, self.y//v3.y, self.z//v3.z)
        elif self._isnum(v3):
            return Vector3(self.x//v3, self.y//v3, self.z//v3)
        else:
            raise TypeError(f"unsupported operand type(s) for *: '{type(self).__name__}' and '{type(v3).__name__}'")


    def __ifloordiv__(self, v3) -> Vector3:
        if isinstance(v3, Vector3):
            self.x //= v3.x
            self.y //= v3.y
            self.z //= v3.z
        elif self._isnum(v3):
            self.x //= v3
            self.y //= v3
            self.z //= v3
        else:
            raise TypeError(f"unsupported operand type(s) for *=: '{type(self).__name__}' and '{type(v3).__name__}'")
        return self


    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


    def _isnum(self, num) -> bool:
        """
        Check if given value is a number (float, decimal, complex etc..)
        
        Arguments:
        - `num` (number)

        Returns:
        - `is_num` (bool)
        """
        try:
            float(num)
        except ValueError:
            return False
        except TypeError:
            return False
        return True


    @classmethod
    def zero(cls):
        return cls(0, 0, 0)


    @classmethod
    def one(cls):
        return cls(1, 1, 1)


    @classmethod
    def two(cls):
        return cls(2, 2, 2)


    def magnitude(self) -> float:
        """
        Returns:
        - `magnitude` (float): Magnitude of the vector
        """
        return math.sqrt(self.x**2+self.y**2+self.z**2)


    def norm(self) -> Vector3:
        """
        Returns:
        - `norm_vec` (Vector3): Normalised vector
        """
        if self.magnitude() == 0:
            raise ZeroDivisionError("Zero vector cannot be normalised")
        return self / self.magnitude()


    def normalise(self) -> Vector3:
        """
        Returns:
        - `norm_vec` (Vector3): Normalised vector
        """
        return self.norm()


    def lerp(self, v3: Vector3, factor) -> Vector3:
        """
        Linear interpolation between `self` and `v3`

        Arguments:
        - `v3` (Vector3): The end vector of the interpolation
        - `factor` (float): The factor of the interpolation

        Returns:
        - `lerp_vector` (Vector3)

        Example Usage:
        ```
        ------------------------
        v1 = Vector3(1, 1, 1)
        v2 = Vector3(2, 2, 2)
        v1.lerp(v2, 0.5)
        >>> (1.5, 1.5, 1.5)
        ------------------------
        ```
        """
        return self + (v3 - self) * factor


    def distance_to(self, v3: Vector3) -> Vector3:
        """
        Calculates the distance to `v3`

        Arguments:
        - `v3` (Vector2)

        Returns:
        - `distance` (float)
        """
        return math.sqrt((v3.x-self.x)**2 + (v3.y-self.y)**2 + (v3.z-self.z)**2)


    def dot(self, v3: Vector3) -> float:
        """
        Calculates the dot product of `self` and `v3`

        Arguments:
        - `v3` (Vector2)

        Returns:
        - `dot_product` (float)
        """
        return (self.x*v3.x)+(self.y*v3.y)+(self.z*v3.z)


# Demonstration code
if __name__ == '__main__':

    v1 = Vector2.zero()

    v2 = Vector2.two()

    print("distance(v1, v2):", distance(v1, v2))
    print("lerp(v1, v2, 0.5):", lerp(v1, v2, 0.5))
    print("v1.magnitude():", v1.magnitude())
    print("dot(v1, v2):", dot(v1, v2))
    print("v2.norm():", v2.norm())

    v3 = Vector3.two()

    v3 += Vector3.one()
    v3 -= Vector3(.1,.1,.1)
    v3 *= 3
    v3 /= 0.5

    print("v3:", v3)

    v4 = Vector3(12.2, 4, "0")
    v4.y += 3
    print("v4 X:", v4.x)
    print("v4 Y:", v4.y)
    print("v4 Z:", v4.z)