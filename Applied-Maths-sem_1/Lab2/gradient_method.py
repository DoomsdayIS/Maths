from math import sqrt
import sympy
from sympy import symbols, diff
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# def func(x):
#     return x[0] ** 2 + x[1] ** 2


# def func(x):
#     return 5 * x[0] * sympy.exp((-1) * (x[0] ** 2 + x[1] ** 2) / 4)

# def func(x):
#     return sympy.sin(x[0]) + sympy.cos(x[1])

#
# def func(x):
#     return 9*x[0]**2 + x[1]**2
#
# def func(x):
#     return x[0]**2 + x[1]**2 - x[0]*x[1] + x[0] - x[1]

def func(x):
    return 2*x[0]**2 + 4*x[1]**2 + 3


def gradient_method(eps: float, n: int, x0, m_type: str):
    counter = 1
    if m_type == 'a':
        alpha = 0.1
    elif m_type == 'b':
        alpha = 1.0
        orig_alpha = 1.0
        coef = 0.5

    while True:
        points.append(x0.copy())
        x_gradient = []  # 0 - n -1
        x0_dict = {}
        for i in range(n):
            x0_dict.update({x[i]: x0[i]})
        for i in range(n):
            x_gradient.append(diff(func(x), x[i]).subs(x0_dict))
        x_prev = x0.copy()
        if m_type == 'a':
            for k in range(n):
                x0[k] = x0[k] - alpha * x_gradient[k]
        elif m_type == 'b':
            while True:
                x_next = [0 for k in range(n)]
                for k in range(n):
                    x_next[k] = x0[k] - alpha * x_gradient[k]
                if func(x_next) - func(x0) > -alpha * coef * sum(x_gradient[j] ** 2 for j in range(n)):
                    alpha *= 0.5
                else:
                    alpha = orig_alpha
                    x0 = x_next.copy()
                    break
        elif m_type == 'c':
            alpha = golden_section(x0, x_gradient)
            for k in range(n):
                x0[k] = x0[k] - alpha * x_gradient[k]
        elif m_type == 'd':
            alpha = fibonacci(x0, x_gradient)
            for k in range(n):
                x0[k] = x0[k] - alpha * x_gradient[k]

        print(counter)
        counter += 1
        norm = sqrt(sum((x0[i] - x_prev[i]) ** 2 for i in range(n)))
        if norm <= eps:
            return x0


def golden_section(cur_point, grad):
    a = 0
    b = 10
    e = 0.00001
    x1 = a + ((-sqrt(5) + 3) / 2) * (b - a)
    x2 = a + ((sqrt(5) - 1) / 2) * (b - a)
    new_x1 = [0] * n
    for i in range(n):
        new_x1[i] = cur_point[i] - x1 * grad[i]
    new_x2 = [0] * n
    for i in range(n):
        new_x2[i] = cur_point[i] - x2 * grad[i]
    f1 = func(new_x1)
    f2 = func(new_x2)
    while b - a > e:
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = a + ((sqrt(5) - 1) / 2) * (b - a)
            for i in range(n):
                new_x2[i] = cur_point[i] - x2 * grad[i]
            f1 = f2
            f2 = func(new_x2)
        else:
            b = x2
            x2 = x1
            x1 = a + ((-sqrt(5) + 3) / 2) * (b - a)
            for i in range(n):
                new_x1[i] = cur_point[i] - x1 * grad[i]
            f2 = f1
            f1 = func(new_x1)
    return (a + b) / 2


def fibonacci(cur_point, grad):
    a = 0
    b = 10
    e = 0.0001
    fibonacci_list = [1, 1]
    while fibonacci_list[-1] <= (b - a) / e:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    x1 = a + fibonacci_list[-3] * (b - a) / fibonacci_list[-1]
    x2 = a + fibonacci_list[-2] * (b - a) / fibonacci_list[-1]
    new_x1 = [0] * n
    for i in range(n):
        new_x1[i] = cur_point[i] - x1 * grad[i]
    new_x2 = [0] * n
    for i in range(n):
        new_x2[i] = cur_point[i] - x2 * grad[i]
    f1 = func(new_x1)
    f2 = func(new_x2)
    for i in range(len(fibonacci_list) - 2):
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - x1 + a
            for i in range(n):
                new_x2[i] = cur_point[i] - x2 * grad[i]
            f1 = f2
            f2 = func(new_x2)
        else:
            b = x2
            x2 = x1
            x1 = b - x2 + a
            for i in range(n):
                new_x1[i] = cur_point[i] - x1 * grad[i]
            new_x2 = [0] * n
            f2 = f1
            f1 = func(new_x1)
    return (a + b) / 2


n = int(input())
x0 = list(map(float, input().split()))

x = [0] * n
for i in range(n):
    x[i] = symbols(f'x{i + 1}')

e = float(input())
m_type = input()

points = []

print(gradient_method(e, n, x0, m_type))

xvec = np.linspace(-5.0, 6.0, 100)
yvec = np.linspace(-5.0, 6.0, 100)
x, y = np.meshgrid(xvec, yvec)

z = x**2 + y**2 - x*y + x - y

fig, ax = plt.subplots()

cntr = ax.contour(x, y, z, [(j / 2) for j in range (-200,200)],
                  colors='black',linewidths = 1.5)

# ax.clabel(cntr, fmt="%2.1f", use_clabeltext=True)


for i in range(len(points) - 1):
    p1, p2 = [points[i][0],points[i+1][0]],[points[i][1],points[i+1][1]]
    plt.plot(p1, p2,linewidth = 2)
fig.set_figwidth(5)  # ширина и
fig.set_figheight(5)  # высота "Figure"

plt.show()
