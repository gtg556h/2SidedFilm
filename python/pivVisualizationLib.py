import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets  import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import pdb




class VelocityField(object):
    def __init__(self):
        print('PIV visualization tools included')

    def slider(self, scale=1):
        """Generates quiver plot with slider control
           of current frame
        """
    
        class RectangleBuilder:
            def __init__(self, ax):
                print('rectangle builder time')
                self.fig = ax.get_figure()
                self.ax = ax

            def connect(self):
                self.cidpress = fig.canvas.mpl_connect('button_press_event', self.on_press)
                self.cidpress = fig.canvas.mpl_connect('button_release_event', self.on_release)

            def on_press(self, event):
                print('click', event)
                if event.inaxes!=self.ax: return
                self.x0_ = event.xdata    
                self.y0_ = -event.ydata

            def on_release(self, event):
                print('release', event)
                if event.inaxes!=self.ax: return
                self.x1_ = event.xdata
                self.y1_ = -event.ydata
                self.x0 = np.min([self.x0_, self.x1_])
                self.x1 = np.max([self.x0_, self.x1_])
                self.y0 = np.min([self.y0_, self.y1_]) 
                self.y1 = np.max([self.y0_, self.y1_])
                del [self.x0_, self.x1_, self.y0_, self.y1_]
                self.draw_rectangle()

            def draw_rectangle(self):
                rect = ax.add_patch(patches.Rectangle((self.x0,-self.y0),(self.x1-self.x0),(-self.y1 + self.y0)))
                self.fig.canvas.draw()


        
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.12, bottom=0.2)

        Q = ax.quiver( self.x[:,0], -self.y[:,0], self.ux1[:,0], -self.uy1[:,0], pivot='mid', color='r', units='inches', scale=scale)

        axcolor = 'lightgoldenrodyellow'
        axframe  = plt.axes([0.12, 0.1, 0.78, 0.03], axisbg=axcolor)

        sframe = Slider(axframe, 'Frame', 0, self.nFrames, valinit=0)

        def update(val):
            n = np.round(sframe.val)

            U = self.ux1[:,n]
            V = -self.uy1[:,n]
            Q.set_UVC(U,V)
            fig.canvas.draw_idle()

        sframe.on_changed(update)

        resetAx = plt.axes([0.8, 0.025, 0.1, 0.04])
        roiAx = plt.axes([0.6, 0.025, 0.1, 0.04])
        button2 = Button(resetAx, 'Reset', color=axcolor, hovercolor='0.975')
        button1 = Button(roiAx, 'ROI', color=axcolor, hovercolor='0.975')
        def reset(event):
            sframe.reset()

        def roiSelect(event):
            print('Select ROI')
            self.roi = RectangleBuilder(ax)
            self.roi.connect()

        button2.on_clicked(reset)
        button1.on_clicked(roiSelect)

        plt.show()


    #####################################################
    #####################################################


    #####################################################
    #####################################################

    def quiver(self, scale=1):
        # Animation of quiver
        fig,ax = plt.subplots(1,1)
        Q = ax.quiver( self.x[:,0], -self.y[:,0], self.ux1[:,0], -self.uy1[:,0], pivot='mid', color='r', units='inches', scale=scale)

        def update_quiver(n, Q, X, Y, nFrames):
            """
            updates the horizontal and vertical vector components by a
            fixed increment on each frame
            """
            nn = np.mod(n, self.nFrames)
            U = self.ux1[:,nn]
            V = -self.uy1[:,nn]

            Q.set_UVC(U,V)

            return Q,

        # you need to set blit=False, or the first set of arrows never gets
        # cleared on subsequent frames
        anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, self.ux1, self.uy1, self.nFrames), interval=10, blit=False)

        plt.show()

    ######################################################
    ######################################################

    def quiverPlusContour(self, scale=1):
        # Coplot animation of quiver and contourf
        # Initiate figure and quiver
        fig = plt.figure(figsize=(10,5))
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122)
        Q = ax1.quiver( self.x[:,0], -self.y[:,0], self.ux1[:,0], -self.uy1[:,0], pivot='mid', color='r', units='inches', scale=scale)

        ######
        # Preprocessing for contour plot:
        XC_ = self.x[:,0]
        YC_ = self.y[:,0]
        nRow = np.where(XC_==XC_[0])[0].size
        nCol = np.where(YC_==YC_[0])[0].size

        XC = np.zeros((nRow,nCol))
        YC = np.zeros((nRow,nCol))
        YC2 = np.zeros((nRow,nCol))
        mag = np.zeros((nRow,nCol))

        minMag = np.min(self.mag1)
        maxMag = np.max(self.mag1)
        dLevel = (maxMag - minMag)/10
        levels = np.arange(minMag,maxMag + dLevel, dLevel)
        levels = np.arange(minMag, minMag + 6*dLevel, dLevel)

        for ii in range(0,nRow):
            XC[ii,:] = XC_[ii*nCol:(ii+1)*nCol]
            YC[ii,:] = YC_[ii*nCol:(ii+1)*nCol]
            mag[ii,:] = self.mag1[ii*nCol:(ii+1)*nCol,0]

        C = ax2.contourf(XC, -YC, mag, levels)

        #####
        def update_quiver(n, Q, C, X, Y, nFrames, nRow, nCol, levels):
            """
            updates the horizontal and vertical vector components by a
            fixed increment on each frame
            """
            nn = np.mod(n, self.nFrames)
            U = self.ux1[:,nn]
            V = -self.uy1[:,nn]


            for ii in range(0,nRow):
                mag[ii,:] = self.mag1[ii*nCol:(ii+1)*nCol, np.mod(n, self.nFrames)]


            Q.set_UVC(U,V)
            #C.set_cmap(mag)
            C = ax2.contourf(XC, -YC, mag, levels)

            return Q,C

        # you need to set blit=False, or the first set of arrows never gets
        # cleared on subsequent frames
        anim = animation.FuncAnimation(fig, update_quiver, fargs=(Q, C, self.ux1, self.uy1, self.nFrames, nRow, nCol, levels), interval=10, blit=False)

        plt.show()




def plotFlip(roi):
    # Need to add buttons for flip x, flip y, complete,
    # Need to adjust formatting

    print('Flip plots to match orientation')
    nRoi = roi.shape[0]
    for i in range(0,nRoi):
        #fig = plt.figure(figsize=(8,8))
        fig = plt.figure()
        fig.flipXState = 0
        fig.flipYState = 0
        fig.subplots_adjust(top=0.9, bottom=0.16, left=0.1, right=0.95, wspace=0.1, hspace=0.1)
        axcolor = 'lightgoldenrodyellow'
        ax1 = fig.add_subplot(221)
        ax1.set_xticklabels([])
        ax1.set_ylim([-np.max(np.abs(roi[i].ux1)),np.max(np.abs(roi[i].ux1))])
        line1, = ax1.plot(roi[0].t, roi[i].ux1)
        ax2 = fig.add_subplot(222)
        ax2.set_xticklabels([])
        ax2.set_ylim([-np.max(np.abs(roi[i].uy1)),np.max(np.abs(roi[i].uy1))])
        line2, = ax2.plot(roi[0].t, roi[i].uy1)
        ax3 = fig.add_subplot(223)

        ax3.set_ylim([-np.max(np.abs(roi[0].ux1)),np.max(np.abs(roi[0].ux1))])
        line3, = ax3.plot(roi[0].t, roi[0].ux1)
        ax4 = fig.add_subplot(224)
        ax4.set_ylim([-np.max(np.abs(roi[0].uy1)),np.max(np.abs(roi[0].uy1))])
        line4, = ax4.plot(roi[0].t, roi[0].uy1)

        xFlipAx = plt.axes([0.23, 0.065, 0.1, 0.04])
        yFlipAx = plt.axes([0.7, 0.065, 0.1, 0.04])
        completeAx = plt.axes([0.45, 0.025, 0.1, 0.04])
        button3 = Button(completeAx, 'Complete', color=axcolor, hovercolor='0.975')
        button2 = Button(xFlipAx, 'Flip X', color=axcolor, hovercolor='0.975')
        button1 = Button(yFlipAx, 'Flip Y', color=axcolor, hovercolor='0.975')

        def flipX(event):
            # Need to integrate a lambda function or something here...
            # See http://stackoverflow.com/questions/173687/is-it-possible-to-pass-arguments-into-event-bindings
            print('Flip X!')
            #pdb.set_trace()
            if fig.flipXState == 0:
                line1.set_ydata(-roi[i].ux1)
                fig.flipXState = 1
            else:
                line1.set_ydata(roi[i].ux1)
                fig.flipXState = 0
            fig.canvas.draw_idle()

        def flipY(event):
            print('Flip Y!')
            if fig.flipYState == 0:
                line2.set_ydata(-roi[i].uy1)
                fig.flipYState = 1
            else:
                line2.set_ydata(roi[i].uy1)
                fig.flipYState = 0
            fig.canvas.draw_idle()
 

        def completeSelection(event):
            if fig.flipXState == 1:
                roi[i].ux1 = -roi[i].ux1
            if fig.flipYState == 1:
                roi[i].uy1 = -roi[i].uy1
            plt.close(fig)


        button3.on_clicked(completeSelection)
        button2.on_clicked(flipX)
        button1.on_clicked(flipY)
        plt.show()
    return 



def setPeakLimits(t,u):
    print('Set Peak Limits!')
    a = setPeakLimitsClass(t,u)
    return a.peakThreshold




class setPeakLimitsClass(object):

    def __init__(self,t,u):
        print('Inside peak limit class definition...')
        self.t = t
        self.u = u
        self.fig, self.ax = plt.subplots()
        self.line1, = self.ax.plot(self.t,self.u,'b')
        self.line2, = self.ax.plot([], [], 'r')

        self.connect()
        plt.show()

    def connect(self):
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_press)

    def on_press(self, event):
        print('click', event)
        if event.inaxes!=self.ax: return
        self.peakThreshold = event.ydata
        print(self.peakThreshold)
        self.drawLine()

    def drawLine(self):
        
        self.y = np.ones_like(self.t) * self.peakThreshold
        self.line2.set_data(self.t, self.y)
        self.fig.canvas.draw()
        #self.fig.canvas.draw_idle()





class RectangleBuilder2:
    def __init__(self, ax):
        print('Select roi')
        self.fig = ax.get_figure()
        self.ax = ax
        self.x0 = []
        self.y0 = []
        self.x1 = []
        self.y1 = []

    def connect(self):
        self.cidpress = self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.cidpress = self.fig.canvas.mpl_connect('button_release_event', self.on_release)

    def on_press(self, event):
        print('click', event)
        if event.inaxes!=self.ax: return
        self.x0_ = event.xdata
        self.y0_ = -event.ydata

    def on_release(self, event):
        print('release', event)
        if event.inaxes!=self.ax: return
        self.x1_ = event.xdata
        self.y1_ = -event.ydata
        self.x0.append(np.min([self.x0_, self.x1_]))
        self.y0.append(np.min([self.y0_, self.y1_]))
        self.x1.append(np.max([self.x0_, self.x1_]))
        self.y1.append(np.max([self.y0_, self.y1_]))
        del [self.x0_, self.x1_, self.y0_, self.y1_]
        self.draw_rectangle()

    def draw_rectangle(self):
        print(self.x0[-1],self.y0[-1])
        rect = self.ax.add_patch(patches.Rectangle((self.x0[-1], -self.y0[-1]), (self.x1[-1] - self.x0[-1]), (-self.y1[-1] + self.y0[-1])))
        self.fig.canvas.draw()

