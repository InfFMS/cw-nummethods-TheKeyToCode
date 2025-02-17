import matplotlib.pyplot as plt
import numpy as np
import math

def get_length(from_, to_, v, between):
    i=from_ #present number
    length = 0
    delta = v[i+1]-v[i] #высота столбика
    while i<to_:
        length += math.sqrt(between**2+delta**2)
        # print(length)
        i+=1
    return round(length,4)

def get_maximums(v):
    for i in range(1,len(v)-1):
        if  v[i-1]<v[i] and v[i] > v[i+1]:
            return i


#
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
    y1 = r*t/(v-b)-a/v**2
    max_ = get_maximums(y1)
    min_ = get_minimums(y1)
    between = v[1]-v[0] #Считаем разницу между нашими делениями
    # print(min_, max_)
    print(get_length(min_, max_, y1, between))
    plt.plot(v, y1, label=str(round(t,2)) + " K, " + str(round(t-273.15)) + " C", color="red")
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()
write_griphics()