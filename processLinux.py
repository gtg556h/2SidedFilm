import numpy as np
import matplotlib.pyplot as plt
import postprocessPIVLib as pppl

side = 0
pivN = 1
nFrames = 19
dt = 1

t = np.arange(0,dt*nFrames,dt)

path = "/Users/brian/working/seq_" + str(1) + "_" + str(side) + "_PIV" + str(pivN) + "_disp.txt"
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

repIndex = np.argmax(np.sum(np.abs(mag1), axis=1))
v = ux1[repIndex, :]
c = np.zeros(v.shape)
for ii in range(0, c.shape[0]):
	c[ii] = np.sum(v[0:ii]) * dt


#plt.plot(t, np.mean(mag1, axis=0), t, np.mean(uy1, axis=0))
if 0:
    jj = 10
    fig = plt.figure(figsize=(8,8))
    ax1 = fig.add_subplot(111)
    ax1.quiver(x[:,jj], -y[:,jj], ux1[:,jj], -uy1[:,jj], scale=4)

    #ax2 = fig.add_subplot(132)
    #ax2.quiver(x[:,jj], y[:,jj], ux2[:,jj], uy2[:,jj], scale=None)

    #ax3 = fig.add_subplot(133)
    #ax3.quiver(x[:,jj], y[:,jj], ux0[:,jj], uy0[:,jj], scale=None)
    plt.show()

if 1:
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import animation

    fig,ax = plt.subplots(1,1)
    Q = ax.quiver( x[:,0], -y[:,0], ux1[:,0], -uy1[:,0], pivot='mid', color='r', units='inches', scale=1)

    #ax.set_xlim(-1, 7)
    #ax.set_ylim(-1, 7)

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
    anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, ux1, uy1, nFrames),
        interval=10, blit=False)

    plt.show()


# path = "samplePIV.txt"

#x, y, ux1, uy1, mag1 = pppl.process(path)

