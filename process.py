import numpy as np
import matplotlib.pyplot as plt
import postprocessPIVLib as pppl
from matplotlib import animation

#####################################################
# Set processing parameters:

side = 0   # Side of film index.  For 2sided film analyses.
pivN = 1   # PIV Pass to import.  Lowest resolution is 1.
nFrames = 599  # Number of frames to process
dt = 0.01 # sec
baseDirectory = "/Users/brian/working/"   # OSX
#baseDirectory = "/home/brian/ssd/working/"   # Linux


#####################################################
# Admin and preallocation of arrays:

t = np.arange(0,dt*nFrames,dt)

path = baseDirectory + "seq_" + str(1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
x_, y_, ux1_, uy1_, mag1_, ang1_, p1_, ux2_, uy2_, mag2_, p2_, ux0_, uy0_, mag0_ = pppl.process(path)

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


######################################################
# Read data into arrays:

for ii in range(0,nFrames):
    
    path = "/Users/brian/working/seq_" + str(ii+1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
    x_, y_, ux1_, uy1_, mag1_, ang1_, p1_, ux2_, uy2_, mag2_, p2_, ux0_, uy0_, mag0_ = pppl.process(path)
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


####################################################
####################################################
# Animation of quiver

if 1:
    fig,ax = plt.subplots(1,1)
    Q = ax.quiver( x[:,0], -y[:,0], ux1[:,0], -uy1[:,0], pivot='mid', color='r', units='inches', scale=1)

    def update_quiver(n, Q, X, Y, nFrames):
        """
        updates the horizontal and vertical vector components by a
        fixed increment on each frame
        """
        nn = np.mod(n, nFrames)
        U = ux1[:,nn]
        V = -uy1[:,nn]

        Q.set_UVC(U,V)

        return Q,

    # you need to set blit=False, or the first set of arrows never gets
    # cleared on subsequent frames
    anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, ux1, uy1, nFrames), interval=10, blit=False)


    plt.show()

######################################################
######################################################
# Coplot animation of quiver and contourf

if 0:
    ####
    # Initiate figure and quiver
    fig = plt.figure(figsize=(10,5))
    ax1 = fig.add_subplot(121)
    ax2 = fig.add_subplot(122)
    Q = ax1.quiver( x[:,0], -y[:,0], ux1[:,0], -uy1[:,0], pivot='mid', color='r', units='inches', scale=1)

    ######
    # Preprocessing for contour plot:
    XC_ = x[:,0]
    YC_ = y[:,0]
    nRow = np.where(XC_==XC_[0])[0].size
    nCol = np.where(YC_==YC_[0])[0].size

    XC = np.zeros((nRow,nCol))
    YC = np.zeros((nRow,nCol))
    YC2 = np.zeros((nRow,nCol))
    mag = np.zeros((nRow,nCol))

    minMag = np.min(mag1)
    maxMag = np.max(mag1)
    dLevel = (maxMag - minMag)/10
    levels = np.arange(minMag,maxMag + dLevel, dLevel)
    levels = np.arange(minMag, minMag + 6*dLevel, dLevel)

    for ii in range(0,nRow):
        XC[ii,:] = XC_[ii*nCol:(ii+1)*nCol]
        YC[ii,:] = YC_[ii*nCol:(ii+1)*nCol]
        mag[ii,:] = mag1[ii*nCol:(ii+1)*nCol,0]

    C = ax2.contourf(XC, -YC, mag, levels)

    #####
    def update_quiver(n, Q, C, X, Y, nFrames, nRow, nCol, levels):
        """
        updates the horizontal and vertical vector components by a
        fixed increment on each frame
        """
        nn = np.mod(n, nFrames)
        U = ux1[:,nn]
        V = -uy1[:,nn]


        for ii in range(0,nRow):
            mag[ii,:] = mag1[ii*nCol:(ii+1)*nCol, np.mod(n, nFrames)]


        Q.set_UVC(U,V)
        #C.set_cmap(mag)
        C = ax2.contourf(XC, -YC, mag, levels)

        return Q,C

    # you need to set blit=False, or the first set of arrows never gets
    # cleared on subsequent frames
    anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, C, ux1, uy1, nFrames, nRow, nCol, levels), interval=10, blit=False)

    plt.show()

######################################################
######################################################


