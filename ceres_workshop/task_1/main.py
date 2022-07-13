import matplotlib.pyplot as plt

grid_min = complex(-2, -1.1)
grid_max = complex(0.6, 1.1)
res = 0.1
julia_c = complex(0.36, 0.1)


class Fractals:
    def __init__(self, max_iter: int = 255, colourmap: str = "viridis") -> None:
        self.max_iter = max_iter
        self.colourmap = colourmap

    @staticmethod
    def complex_grid(
        min_: complex, max_: complex, res: float
    ) -> list[list[complex]]:
        xmin, ymin = min_.real, min_.imag
        xmax, ymax = max_.real, max_.imag
        x, y = xmin, ymin
        grid = []
        while x < xmax:
            inner = []
            while y < ymax:
                inner.append(complex(x, y))
                y += res
            grid.append(inner)
            x += res
            y = ymin
        return grid

    @staticmethod
    def quadratic_map(c: complex, z0: complex) -> complex:
        z = z0
        while True:
            yield z
            z = z ** 2 + c

    def iterate(self, c: complex, z0: complex) -> int:
        for n, z in zip(range(self.max_iter), self.quadratic_map(c, z0)):
            if abs(z) >= 2:
                break
        return n

    def mandelbrot(
        self, cmin: complex, cmax: complex, res: float
    ) -> plt.Figure:

        grid = self.complex_grid(cmin, cmax, res)
        cmax = grid[-1][-1]

        values = [[self.iterate(c, 0) for c in row] for row in grid]

        fig, ax = plt.subplots()
        ax.imshow(
            values,
            cmap=self.colourmap,
            extent=(cmin.real, cmax.real, cmin.imag, cmax.imag),
        )
        ax.set_title("Mandelbrot Set")
        ax.set_xlabel("Re(C)")
        ax.set_ylabel("Im(C)")

        return fig

    def julia(
        self, zmin: complex, zmax: complex, res: float, c: complex
    ) -> plt.Figure:
        grid = self.complex_grid(zmin, zmax, res)
        zmax = grid[-1][-1]

        values = [[self.iterate(c, z) for z in row] for row in grid]

        fig, ax = plt.subplots()
        ax.imshow(
            values,
            cmap=self.colourmap,
            extent=(zmin.real, zmax.real, zmin.imag, zmax.imag),
        )
        ax.set_title(f"Julia Set (C = {c.real} + {c.imag}i)")
        ax.set_xlabel("Re(z0)")
        ax.set_ylabel("Im(z0)")

        return fig


fractals = Fractals()
print("Computing Mandelbrot set")
fig_1 = fractals.mandelbrot(grid_min, grid_max, res)
print("Computing Julia set")
fig_2 = fractals.julia(grid_min, grid_max, res, julia_c)
#plt.show()
