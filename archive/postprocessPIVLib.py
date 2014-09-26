import numpy as np
# from io import StringIO

def process(path):
    f = open(path, 'r')
    x = []
    y = []
    ux1 = []
    uy1 = []
    mag1 = []
    ang1 = []
    p1 = [] 
    ux2 = [] 
    uy2 = [] 
    mag2 = [] 
    ang2 = []
    p2 = []
    ux0 = []
    uy0 = []
    mag0 = []
    # flag = 



    for line in f:
        line = line.strip()
        columns = line.split()
        x.append(columns[0])
        y.append(columns[1])
        ux1.append(columns[2])
        uy1.append(columns[3])
        mag1.append(columns[4])
        ang1.append(columns[4])
        p1.append(columns[4])
        ux2.append(columns[4])
        uy2.append(columns[4])
        mag2.append(columns[4])
        ang2.append(columns[4]) 
        p2.append(columns[4])
        ux0.append(columns[4]) 
        uy0.append(columns[4])
        mag0.append(columns[4]) 
 

    f.close()
    x = np.asarray(x).astype(float)
    y = np.asarray(y).astype(float)
    ux1 = np.asarray(ux1).astype(float)
    uy1 = np.asarray(uy1).astype(float)
    mag1 = np.asarray(mag1).astype(float)
    ang1 = np.asarray(ang1).astype(float)
    p1 = np.asarray(p1).astype(float)
    ux2 = np.asarray(ux2).astype(float)
    uy2 = np.asarray(uy2).astype(float)
    mag2 = np.asarray(mag2).astype(float)
    ang2 = np.asarray(ang2).astype(float)
    p2 = np.asarray(p2).astype(float)
    ux0 = np.asarray(ux0).astype(float)
    uy0 = np.asarray(uy0).astype(float)
    mag0 = np.asarray(mag0).astype(float)
    # flag = 

    return x, y, ux1, uy1, mag1, ang1, p1, ux2, uy2, mag2, p2, ux0, uy0, mag0

