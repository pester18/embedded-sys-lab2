import math

class DFTthread:
    def __init__(self, x, start_idx, end_idx):
        self.x = x
        self.N = len(x)
        self.start_idx = start_idx
        self.end_idx = end_idx

    def run(self):
        print('Starting thread for dft')
        res = self.calculate()
        if(res):
            print('Finished thread for dft')
            return res

    def calculate(self):
        F_Re = []
        F_Im = []
        w_Re = []
        w_Im = []
        num_of_points = self.end_idx - self.start_idx

        for p in range(num_of_points):
            w_Re.append([])
            w_Im.append([])
            for k in range(self.N):
                w_Re[p].append(math.cos(2 * math.pi * (self.start_idx + p) * k / self.N))
                w_Im[p].append(math.sin(2 * math.pi * (self.start_idx + p) * k / self.N))

        for p in range(num_of_points):
            F_Re.append(0.0)
            F_Im.append(0.0)

            for k in range(self.N):
                F_Re[p] += self.x[k] * w_Re[p][k]
                F_Im[p] -= self.x[k] * w_Im[p][k]

        return F_Re