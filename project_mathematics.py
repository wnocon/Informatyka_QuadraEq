from math import sqrt


def quadratic_eqiation(a, b, c):
    delta = b*b-4*a*c
    if delta < 0:
        return []
    elif delta == 0:
        return [-b*(2*a)]
    else:
        x1 = (-b-sqrt(delta))/(2*a)
        x2 = (-b+sqrt(delta))/(2*a)
        return [x1, x2]


def compute_function(a, b, c, xmin, xmax, dx):
    xx = []
    yy = []
    n = int((xmax - xmin)/dx + 1)
    for i in range(n):
        x = xmin + i*dx
        xx.append(x)

        y = a*x*x + b*x + c
        yy.append(y)

    # zwrócenie wyników (xx i yy)
    return xx, yy