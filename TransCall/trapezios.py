import math
import numpy as np
import matplotlib.pyplot as plt

def polinomio(x):
    return 0.2 + 25*x - 200*(x**2) + 675*(x**3) - 900*(x**4) + 400*(x**5)

def main():
    n = 2
    erros = {}
    valor_real = 1.640533
    x_ss = []
    y_ss = []

    while n < 11:
        trapezios = []
        intervalos = np.linspace(0, 0.8, n+1)
        cont = 0
        x_s = []
        y_s = []

        while cont < len(intervalos)-1:

            x = intervalos[cont]
            x1 = intervalos[cont+1]
            
            f_x = polinomio(x)
            f_x1 = polinomio(x1)
            trapezio = (1/2) * (f_x1 + f_x) * (x1 - x)
            trapezios.append(trapezio)

            if cont == len(intervalos)-2:
                x_s.append(x1)
                y_s.append(f_x1)

            else:
                x_s.append(x)
                y_s.append(f_x)

            cont += 1

        erros[n] = float (round((abs(valor_real - sum(trapezios))/valor_real)*100, 3))
        y_ss.append(y_s)
        x_ss.append(x_s)

        n += 1

    print(erros)

    i = 0
    intervalo = np.linspace(0, 0.8, 200)
    x_s = []
    y_s = []
    while i < len(intervalo):
        f_x = polinomio(intervalo[i])

        y_s.append(f_x)
        x_s.append(intervalo[i])

        i += 1

    plt.figure()
    plt.title('F(x) Original')
    plt.plot(x_s, y_s)

    plt.figure()
    plt.title('Erros')
    plt.plot(erros.keys(), erros.values())

    plt.show()

    

main()

