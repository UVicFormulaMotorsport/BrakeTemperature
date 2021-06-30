import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def heat_function(x, a, b, c):
    temp = a * np.log(x + b) + c
    #print(temp)
    return temp


if __name__ == "__main__":
    x = np.array([0, 3, 5, 9])
    y = np.array([30, 60, 84, 100])
    fitting_parameters, pcov = curve_fit(heat_function, x, y)
    a, b, c = fitting_parameters

    next_x = 12
    next_y = heat_function(next_x, a, b, c)

    plt.plot(x, y, 'r--')
    plt.plot(np.append(x, next_x), np.append(y, next_y), 'ro')
    plt.xlabel('Time (m)')
    plt.ylabel('Temperature (C)')
    plt.show()
