import numpy as np
import matplotlib.pyplot as plt

def main():
    X = [i for i in np.arange(-2, 2, 0.1)]
    Y = []
    Z = []
    for i in X:
        Y.append(i**3+i**2-2*i-1)
        Z.append(0)
    plt.plot(X, Y, label = 'Функция')
    plt.plot(X, Z, label = 'Ось Х')
    plt.legend()
    plt.grid()
    plt.savefig('func.png')

if __name__ == '__main__':
    main()