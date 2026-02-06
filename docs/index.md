<p align="center">
    <img src="https://raw.githubusercontent.com/mags0ft/geronimo/refs/heads/main/docs/assets/icon.png" width=256 />
</p>

`geronimo` is a minimal and easy-to-learn Python library for your quick and dirty everday math calculations, especially regarding high-dimensional geometry calculations.

## Get started

Read the instructions on [how to install](./installation.md) `geronimo`, or start right off by reading the [documentation](./documentation.md) of the library's classes.

## Example

```python
from geronimo.geometry.point import Point
from geronimo.geometry.vector import Vector

# define points in three-dimensional space:
p0 = Point([0, 0, 0])   # (works with higher dimensions too!)
p1 = Point([8, 4, 2])

# create a vector from the points:
v0 = Vector.from_points(p0, p1)

# get the length of a vector:
print(v0.length())  # ≈ 9.165

# use pure Python math syntax for operations:
v1, v2 = v0 * 0.25, v0.normalize()

print(v1.length(), v2.length()) # ≈ 2.291, 1.0
```
