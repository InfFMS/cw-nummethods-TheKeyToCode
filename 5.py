import matplotlib.pyplot as plt
import numpy as np
import math
r=8.314
a = 0.1382
b = 3.19/100000 # P(V,T) = RT/(V-b) - a/V**2
t=-130 + 273.15
p_r = 3664186.998 #Паскалей
def get_answer(between, how_many, v):
    answers = []
    i=0
    while i<len(v)-1 and how_many>len(answers):
        if v[i]*v[i+1]<=0: #It will be true, if "y" has different signs, or one of them equals 0
            answers.append(float(i)*float(between)) #As result, we have answer +- delta/2
            # print(answers)
        i+=1
        # print("Present i:", i, "From:", from_, answers)
    return answers
def get_maximums(v):
    for i in range(1,len(v)-1):
        if  v[i-1]<v[i] and v[i] > v[i+1]:
            return i


#
def get_minimums(v):
    for i in range(1,len(v)-1):
        if  v[i-1]>v[i] and v[i] < v[i+1]:
            return i
def intagrall1(v,between):
    answer = 0
    i=0
    while i < len(v)-1:
        answer+=(v[i]+v[i+1])/2*between
        i+=1
    return answer
def intagrall2(p, from_, to_):
    return p*(to_-from_)

def test_Maxvel(v, between, p, from_, to_):
    print(intagrall1(v,between), intagrall2(p, from_, to_))
def write_griphics():
    v = np.linspace(b + 0.00001, 0.001, 5000)  # 100 точек от -10 до 10
    y1 = r*t/(v-b)-a/v**2
    max_ = get_maximums(y1)
    min_ = get_minimums(y1)

    between = v[1]-v[0] #Считаем разницу между нашими делениями
    answers = get_answer(between,3 , y1)
    # print("V1:", answers[0],", V центральный:", answers[1],", Vg:", answers[2],)
    test_Maxvel(y1, between, p_r, b + 0.00001, 0.001)
    plt.plot(v, y1, label=str(round(t,2)) + " K, " + str(round(t-273.15)) + " C", color="red")
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()
write_griphics()