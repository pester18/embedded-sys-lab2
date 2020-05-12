from pseudo_rand_signal import generate_signal
from time import perf_counter
import matplotlib.pyplot as plt
from dft_thread import DFTthread
#from fourier_trans import fft, dft


def Rxx(arr, t):
    list = [x[1] for x in arr]
    N = len(arr) / 2
    M = sum(list) / len(list)

    if t > N:
        print('t exceeds range')
        return 0
    else:
        Rxx = 0
        for j in range(int(N)):
            Rxx += (list[j] - M) * (list[j + t] - M) / (N - 1)

        return Rxx


def Rxy(arr1, arr2, t):
    list1 = [x[1] for x in arr1]
    list2 = [x[1] for x in arr2]

    N = len(arr1) / 2
    M1 = sum(list1) / len(list1)
    M2 = sum(list2) / len(list2)

    if t > N:
        print('t exceeds range')
        return 0
    else:
        Rxy = 0
        for j in range(int(N)):
            Rxy += (list1[j] - M1) * (list2[j + t] - M2) / (N - 1)

        return Rxy


class main:
    n = 6
    w = 1700
    N = 1024

    points1 = generate_signal(n, w, N)
    RxxList = []

    for tau in range(int(N / 2)):
        RxxList.append(Rxx(points1, tau))

    points2 = generate_signal(n, w, N)
    RxyList = []

    for tau in range(int(N / 2)):
        RxyList.append(Rxy(points1, points2, tau))

    signalValues = [point[1] for point in points1]

    #DFTList = dft(signalValues)
    #print(DFTList)
    #FFTList = fft(signalValues)
    #print(FFTList)

    dft_thr1 = DFTthread(signalValues, 0, 512)
    dft_thr2 = DFTthread(signalValues, 512, 1024)

    dtf_sublist1 = dft_thr1.run()
    dtf_sublist2 = dft_thr2.run()
    DFTList = dtf_sublist1 + dtf_sublist2

    plt.plot([x for x in range(N)], DFTList, color='b')
    #plt.plot([x for x in range(N)], FFTList, color='r')
    plt.show()