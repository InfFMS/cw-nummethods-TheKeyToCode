import matplotlib.pyplot as plt
import numpy as np


r=8.314
a = 0.1382
b = 3.19/100000 # P(V,T) = RT/(V-b) - a/V**2
t1=-140 + 273.15
t2=-130 + 273.15
t3=-120 + 273.15
t4=-110 + 273.15
t5=-100 + 273.15
colors = ["grey", "grey", "grey", "grey", "grey"]
def get_min_extreme_bool(v):
    m = v[0]
    for i in v:
        # print(i,m)
        if i<=m:
            m=i
        else:
            return True
    return False

def get_this_T(v):
    i=0
    while(get_min_extreme_bool(v[i])):
        i+=1
    colors[i]="red"
def write_griphics():
    v = np.linspace(b + 0.00001, 0.001, 5000)  # 100 точек от -10 до 10
    y1 = r*t1/(v-b)-a/v**2
    y2 = r*t2/(v-b)-a/v**2
    y3 = r*t3/(v-b)-a/v**2
    y4 = r*t4/(v-b)-a/v**2
    y5 = r*t5/(v-b)-a/v**2
    get_this_T([y1, y2, y3, y4, y5])
    plt.plot(v, y1, label=str(round(t1,2)) + " K, " + str(round(t1-273.15)) + " C", color=colors[0])
    plt.plot(v, y2, label=str(round(t2,2)) + " K, " + str(round(t2-273.15)) + " C", color=colors[1])
    plt.plot(v, y3, label=str(round(t3,2)) + " K, " + str(round(t3-273.15)) + " C", color=colors[2])
    plt.plot(v, y4, label=str(round(t4,2)) + " K, " + str(round(t4-273.15)) + " C", color=colors[3])
    plt.plot(v, y5, label=str(round(t5,2)) + " K, " + str(round(t5-273.15)) + " C", color=colors[4])
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    # get_min(b+0.00001, 0.001, get_value_for_140)
    # print(get_min_extreme_bool(y1))
    # print(get_min_extreme_bool(y2))
    # print(get_min_extreme_bool(y3))
    # print(get_min_extreme_bool(y4))
    # print(get_min_extreme_bool(y5))

    plt.show()
write_griphics()