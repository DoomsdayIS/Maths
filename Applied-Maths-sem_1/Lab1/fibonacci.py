from math import sin

from numpy import double, math


def func(x):
    return double(sin(x) * x ** 2)

# def func(x):
#     return double(sin(x) * (1 - math.e - x)**2 + x**2*math.e**(-(x**2)))


def fibonacci(a, b, e):
    fibonacci_list = [1, 1]
    while fibonacci_list[-1] <= (b-a)/e:
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    x1 = a + fibonacci_list[-3]*(b - a)/fibonacci_list[-1]
    x2 = a + fibonacci_list[-2]*(b - a)/fibonacci_list[-1]
    f1 = func(x1)
    f2 = func(x2)
    iter_counter = 0
    func_counter = 2
    lengths = [b - a]
    for i in range(len(fibonacci_list) - 2):
        if f1 > f2:
            a = x1
            x1 = x2
            x2 = b - x1 + a
            f1 = f2
            f2 = func(x2)
        else:
            b = x2
            x2 = x1
            x1 = b - x2 + a
            f2 = f1
            f1 = func(x1)
        iter_counter += 1
        func_counter += 1
        lengths.append(b - a)
    return (a + b) / 2, iter_counter, func_counter, lengths


a, b, e = map(double, input().split())
print("======fibonacci======")
print("Eps = ", e)
minimum, iter_counter, func_counter, lengths = (fibonacci(a, b, e))
print("Minimum point is " + str(minimum) + "\nIteration number : " + str(iter_counter) + "\nFunction calculation "
                                                                                         "number : " + str(
    func_counter))
print("Values step by step :")
print(lengths)

for i in range(1, len(lengths)):
    print(lengths[i] / lengths[i - 1], "  ", i)




