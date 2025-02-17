import matplotlib.pyplot as plt
import numpy as np

def get_maximums(v):
    maximums = []
    for i in range(1,len(v)-1):
        if  v[i-1]<v[i] and v[i] > v[i+1]:
            return i
def get_minimums(v):
    for i in range(1,len(v)-1):
        if  v[i-1]>v[i] and v[i] < v[i+1]:
            return i
r=8.314
a = 0.1382
b = 3.19/100000 # P(V,T) = RT/(V-b) - a/V**2
t=-130 + 273.15

def write_griphics():
    v = np.linspace(b + 0.00001, 0.001, 5000)  # 100 точек от -10 до 10
    between = v[1]-v[0] #Считаем разницу между нашими делениями
    y1 = r*t/(v-b)-a/v**2
    print(get_maximums(y1), get_maximums(y1)*between + b + 0.00001)
    print(get_minimums(y1), get_minimums(y1)*between + b + 0.00001)
    plt.plot(v, y1, label=str(round(t,2)) + " K, " + str(round(t-273.15)) + " C", color="red")
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()
write_griphics()