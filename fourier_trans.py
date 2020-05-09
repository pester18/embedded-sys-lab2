import math


def dft(x):
    N = len(x)
    F_Re = []
    F_Im = []
    F = []
    wRe = []
    wIm = []

    for p in range(N):
        wRe.append([])
        wIm.append([])
        for k in range(N):
            wRe[p].append(math.cos(2 * math.pi * p * k / N))
            wIm[p].append(math.sin(2 * math.pi * p * k / N))

    for p in range(N):
        F_Re.append(0.0)
        F_Im.append(0.0)

        for k in range(N):
            F_Re[p] += x[k] * wRe[p][k]
            F_Im[p] -= x[k] * wIm[p][k]

        F.append(F_Re[p] * F_Re[p] + F_Im[p] * F_Im[p])
    return F_Re

def fft(x):
    N = len(x)
    F_Re1 = []
    F_Im1 = []
    F_Re2 = []
    F_Im2 = []
    F_Re = [None] * N
    F_Im = [None] * N

    for p in range(int(N / 2)):
        F_Re1.append(0.0)
        F_Im1.append(0.0)
        F_Re2.append(0.0)
        F_Im2.append(0.0)

        for m in range(int(N / 2)):
            F_Re1[p] += x[2 * m + 1] * math.cos(4 * math.pi * p * m / N)
            F_Re2[p] += x[2 * m] * math.cos(4 * math.pi * p * m / N)
            F_Im1[p] -= x[2 * m + 1] * math.sin(4 * math.pi * p * m / N)
            F_Im2[p] -= x[2 * m] * math.sin(4 * math.pi * p * m / N)

        F_Re[p] = F_Re2[p] + F_Re1[p] * math.cos(2 * math.pi * p / N)
        F_Re[p + int(N / 2)] = F_Re2[p] + F_Re1[p] * math.cos(2 * math.pi * (p + N / 2) / N)
        F_Im[p] = F_Im2[p] + F_Im1[p] * math.sin(2 * math.pi * p / N)
        F_Im[p + int(N / 2)] = F_Im2[p] + F_Im1[p] * math.sin(2 * math.pi * (p + N / 2) / N)
    return F_Re
