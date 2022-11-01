import numpy as np
import matplotlib.pyplot as plt
import sympy
from matplotlib import patheffects


fig, ax = plt.subplots(figsize=(6, 6))

nx = 100
ny = 100

# Set up survey vectors
xvec = np.linspace(-10.0, 10.0, nx)
yvec = np.linspace(-10.0, 10.0, ny)
print(xvec)

# Set up survey matrices.  Design disk loading and gear ratio.
x1, x2 = np.meshgrid(xvec, yvec)

# Evaluate some stuff to plot
obj = 5 * x1 * np.exp((-1) * (x1 ** 2 + x2 ** 2) / 4)

g1 = -(3*x1 + x2 - 5.5)


cntr = ax.contour(x1, x2, obj, [-3,-2,-1,0.01, 0.1, 0.5, 1, 2, 4, 8, 16],
                  colors='black')
cg1 = ax.contour(x1, x2, g1, [0], colors='sandybrown')

x1, y1 = [0, 1], [1, 4]
plt.plot(x1, y1, marker = 'o')

ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)


ax.set_xlim(-5,6)
ax.set_ylim(-5,6)

plt.show()