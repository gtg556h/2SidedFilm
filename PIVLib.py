import numpy as np
# from io import StringIO

def readFrame(path):

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


def process(baseDirectory, outFilename, side, pivN, nFrames, dt):

    t = np.arange(0, dt*nFrames, dt)

    path = baseDirectory + "seq_" + str(1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
    x_, y_, ux1_, uy1_, mag1_, ang1_, p1_, ux2_, uy2_, mag2_, p2_, ux0_, mag0_ = readFrame(path)

    nPreallocate = x_.shape[0]

    x = np.zeros([nPreallocate, nFrames])
    y = np.zeros([nPreallocate, nFrames])
    ux1 = np.zeros([nPreallocate, nFrames])
    uy1 = np.zeros([nPreallocate, nFrames])
    mag1 = np.zeros([nPreallocate, nFrames])
    ang1 = np.zeros([nPreallocate, nFrames])
    p1 = np.zeros([nPreallocate, nFrames])
    ux2 = np.zeros([nPreallocate, nFrames])
    uy2 = np.zeros([nPreallocate, nFrames])
    mag2 = np.zeros([nPreallocate, nFrames])
    p2 = np.zeros([nPreallocate, nFrames])
    ux0 = np.zeros([nPreallocate, nFrames])
    uy0 = np.zeros([nPreallocate, nFrames])
    mag0 = np.zeros([nPreallocate, nFrames])

    for ii in range(0,nFrames):
        
        path = baseDirectory + "seq_" + str(ii+1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
        x_, y_, ux1_, uy1_, mag1_, ang1_, p1_, ux2_, uy2_, mag2_, p2_, ux0_, uy0_, mag0_ = readFrame(path)
        x[:,ii] = x_
        y[:,ii] = y_
        ux1[:,ii] = ux1_
        uy1[:,ii] = uy1_
        mag1[:,ii] = mag1_
        ang1[:,ii] = ang1_
        p1[:,ii] = p1_
        ux2[:,ii] = ux2_
        uy2[:,ii] = uy2_
        mag2[:,ii] = mag2_
        p2[:,ii] = p2_
        ux0[:,ii] = ux0_
        uy0[:,ii] = uy0_
        mag0[:,ii] = mag0_

    np.savez(outputFilename, x=x, y=y, ux1=ux1, uy1=uy1, mag1=mag1, ang1=ang1, p1=p1, ux2=ux2, uy2=uy2, mag2=mag2, p2=p2, ux0=ux0, uy0=uy0, mag0=mag0)


