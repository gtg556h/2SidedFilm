import numpy as np
import matplotlib.pyplot as plt
import postprocessPIVLib as pppl

side = 0
pivN = 3
nFrames = 199
dt = 1

t = np.arange(0,dt*nFrames,dt)

path = "/Users/brian/working/seq_" + str(1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
x_, y_, ux1_, uy1_, mag1_ = pppl.process(path)

nPreallocate = x_.shape[0]

x = np.zeros([nPreallocate, nFrames])
y = np.zeros([nPreallocate, nFrames])
ux1 = np.zeros([nPreallocate, nFrames])
uy1 = np.zeros([nPreallocate, nFrames])
mag1 = np.zeros([nPreallocate, nFrames])




for ii in range(0,nFrames):
    
    path = "/Users/brian/working/seq_" + str(ii+1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
    x_, y_, ux1_, uy1_, mag1_ = pppl.process(path)
    x[:,ii] = x_
    x[:,ii] = y_
    ux1[:,ii] = ux1_
    uy1[:,ii] = uy1_
    mag1[:,ii] = mag1_

repIndex = np.argmax(np.sum(np.abs(mag1), axis=1))
v = ux1[repIndex, :]
c = np.zeros(v.shape)
for ii in range(0, c.shape[0]):
	c[ii] = np.sum(v[0:ii]) * dt


plt.plot(t, np.mean(mag1, axis=0), t, np.mean(uy1, axis=0))
plt.show()


# path = "samplePIV.txt"

#x, y, ux1, uy1, mag1 = pppl.process(path)

