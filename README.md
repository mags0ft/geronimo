<p align="center">
    <img src="./docs/assets/icon-white-box.png" height=128 />
</p>

Geronimo is a minimal and easy-to-learn Python library for your quick and dirty everday math calculations, especially regarding high-dimensional geometry calculations.

> [!IMPORTANT]
>
> The geronimo project does, contrary to my other projects, not accept any AI-generated contributions at all; please refrain from submitting vibe-coded pull requests.
>
> Intent of the library is to give room for some "recreational" and mindful coding, a.e. implementing math concepts or fun little optimizations.
> Thus, this project does **not** prioritize performance and does **not** encourage you to use it in production. There are many, many better alternatives for that.

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

## License

`geronimo` is an open source project. You can take a look at the `LICENSE` file [here](./LICENSE).
