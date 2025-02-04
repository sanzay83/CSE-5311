import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f(n):
    x = 1
    for i in range(1, n):
        for j in range(1, n):
            x += 1
    return x

def fit_function(n, a, b):
    return a * (n ** 2) + b

if __name__ == '__main__':
    arr = []
    for i in range(1, 800):
        start_time = time.time()
        f(i)
        end_time = time.time()
        arr.append((i, end_time - start_time))

    n_values, time_values = zip(*arr)

    popt, povc = curve_fit(fit_function, n_values, time_values)

    fit_values = [fit_function(n, popt[0], popt[1]) for n in n_values]
    upper_value = [1.5*fit_values[i] for i in range(len(fit_values))]
    lower_value = [0.5*fit_values[i] for i in range(len(fit_values))]
    plt.scatter(n_values, time_values, marker='o', label='Measured Time', color='blue')

    plt.plot(n_values, fit_values, linestyle='--', color='r', label='Fitted Curve')
    plt.plot(n_values, upper_value, linestyle='--', color='g', label='Upper Bound')
    plt.plot(n_values, lower_value, linestyle='--', color='y', label='Lower Bound')
    plt.xlabel('n')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time vs n')
    plt.legend()
    plt.grid(True)
    plt.show()
