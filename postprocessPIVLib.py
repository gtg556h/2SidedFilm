import numpy as np
# from io import StringIO

def process(path):
    f = open(path, 'r')
    x = []
    y = []
    ux1 = []
    uy1 = []
    mag1 = []


    for line in f:
        line = line.strip()
        columns = line.split()
        x.append(columns[0])
        y.append(columns[1])
        ux1.append(columns[2])
        uy1.append(columns[3])
        mag1.append(columns[4])

    f.close()
    x = np.asarray(x).astype(float)
    y = np.asarray(y).astype(float)
    ux1 = np.asarray(ux1).astype(float)
    uy1 = np.asarray(uy1).astype(float)
    mag1 = np.asarray(mag1).astype(float)

    return x, y, ux1, uy1, mag1


