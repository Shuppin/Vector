# Vector
A small module for vector operations in python.

This program was an experiment into dunder (double underscore) methods in python and is not fully tested.

### Example usage:
```py
from vector import *

vector1 = Vector3(20, 30, 40)
vector2 = Vector3.two()

print("distance(vector1, vector2):", distance(vector1, vector2))
print("lerp(vector1, vector2, 0.5):", lerp(vector1, vector2, 0.5))
print("vector1.magnitude():", vector1.magnitude())
print("dot(vector1, vector2):", dot(vector1, vector2))
print("vector2.norm():", vector2.norm())

vector3 = Vector3.two()

vector3 += Vector3.one()
vector3 -= Vector3(.1,.1,.1)
vector3 *= 3
vector3 /= 0.5

print(vector3)

vector4 = Vector3(12.2, 4, "0")
vector4.y += 3
print("vector4 X:", vector4.x)
print("vector4 Y:", vector4.y)
print("vector4 Z:", vector4.z)
```