from random import random
from math import sin
    
def generate_signal(harm_num, w_max, pointsCount = 1024):
    pointsList = []
    w_step = w_max / harm_num
    
    for i in range(harm_num):
        w = w_step * i
        A = random()
        phi = random()
        result = generate_harmonic(A, phi, w, pointsCount, 1)
        for j in range(len(result)):
            if len(pointsList) == j:
                pointsList.append(result[j])
            else :
                pointsList[j][1] += result[j][1]

    return pointsList

def generate_harmonic(A, phi, w, pointsCount, accuracy = 0.1):
    result = []
    for i in range(pointsCount):
        result.append([i * accuracy, A * sin(w * i * accuracy + phi)])
    return result
