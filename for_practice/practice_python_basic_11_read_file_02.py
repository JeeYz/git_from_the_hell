import numpy as np

fout = open("input_BAS.txt", "r", encoding="utf-8")

while True:

    line = fout.readline()
    if not line: break
    a = [int(x) for x in line.split()]
    b = np.array(a)


data = np.loadtxt("input_BAS.txt", dtype=float)
print(data)
