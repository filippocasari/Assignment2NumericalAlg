import numpy as np
import matplotlib as plt


def create_b_matrix(n):
    b = []
    for i in range(n):
        if (i == 0 or i == n - 1):
            b.append(7)
        elif i == (n / 2) - 1 or i == (n / 2):
            b.append(10)
        else:
            b.append(9)
    return b


def gaussMethod(n, b, iterations):
    x = []
    for i in range(n):
        x.append(0.0)
    counter=0
    while True:
        max_value_differ = 0.0
        for i in range(n):
            x_i = x[i]
            s = 0.0
            if i > 0:
                s += 2.0 * x[i - 1]
            if (i > n / 2) or i < (n / 2) - 1:
                s += -1.0 * x[i - 1 - i]
            if i + 1 < n:
                s += 2.0 * x[i + 1]

            x[i] = (b[i] - s) / 6.0
            if abs(x_i - x[i]) > max_value_differ:
                max_value_differ = abs(x_i - x[i])
        print("MEX DIFFER: ", max_value_differ)
        counter += 1
        if max_value_differ < 10 ** (-16):
            break

    return x


if __name__ == '__main__':
    n = 1
    counter = 0
    while n % 2 == 1 and counter < 5:
        n = int(input("Insert the value of n: "))
        if n % 2 == 1:
            print("n is not even, retry")
        counter += 1
    b = create_b_matrix(n)
    print("Vector b is: \n", b)
    x = gaussMethod(n, b, 100000)
    print(x)
