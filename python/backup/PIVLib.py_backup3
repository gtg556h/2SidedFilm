import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import pdb


# Notes:

# Current status: Functional ROI and RSOI classes.  Plot flipping for
# consistent peak orientation by visual inspection implemented.  Now 
# just need to integrate post processing!  Peak detection, averaging of 
# individual ROIs in RSOI representative functions, phase conversion,
# and relative phase analysis!!!!

# Current status: Works!
# Initialize piv object
# Execute 'p1.analyze(scale, screenID0
# View resultant data via p1.screen[i]

# The skeleton of the framework below has been laid.
# Currently, we can instantiate a member of piv class
# Then: varname = pivInstance.analyzed(pivInstance, 100) generates an instance of class roi, with all required vars
# Need to restructure class layout to make it run more logically!


# Implemented ROI selection in Slider method
# Generate new routine, using Slider base, where integer selection of multiple ROIs generates a list of ROIs.
# After ROI list generation, sieve function is performed on EACH roi, generating mean ux1, uy1 etc... computations on each ROI

# Need to organize code better with multiple class additions and proper inheritence


########################################################
########################################################
########################################################
########################################################
########################################################


class ROI:
    def zeroMean(self,attr):
        attr = attr - np.mean(attr)

    def __init__(self, t, piv, roiParam, roiIndex):
        self.t = t

        self.x0 = roiParam.x0[roiIndex]
        print(self.x0)
        self.x1 = roiParam.x1[roiIndex]
        self.y0 = roiParam.y0[roiIndex]
        self.y1 = roiParam.y1[roiIndex]

        self.ux0 = np.zeros_like(piv.t); self.uy0 = np.zeros_like(piv.t)
        self.ux1 = np.zeros_like(piv.t); self.uy1 = np.zeros_like(piv.t)
        self.ux2 = np.zeros_like(piv.t); self.uy2 = np.zeros_like(piv.t)

        self.indices = np.where((piv.x[:,0] < self.x1) & (piv.x[:,0] > self.x0) & (piv.y[:,0] < self.y1) & (piv.y[:,0] > self.y0))[0]

        for i in range(0, piv.t.shape[0]):
            self.ux0[i] = np.mean(piv.ux0[self.indices, i])
            self.uy0[i] = np.mean(piv.uy0[self.indices, i])
            self.ux1[i] = np.mean(piv.ux1[self.indices, i])
            self.uy1[i] = np.mean(piv.uy1[self.indices, i])
            self.ux2[i] = np.mean(piv.ux2[self.indices, i])
            self.uy2[i] = np.mean(piv.uy2[self.indices, i])
    
        self.zeroMean(self.ux0); self.zeroMean(self.ux1); self.zeroMean(self.ux2)
        self.zeroMean(self.uy0); self.zeroMean(self.uy1); self.zeroMean(self.uy2)



def plotFlip(roi):
    # Need to add buttons for flip x, flip y, complete,
    # Need to adjust formatting

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
   

        

class RSOI:
    def __init__(self, piv, setIndex):
        print('processing roi')
        self.rsoiID = piv.rsoi[setIndex].analysisID
        self.roiParam = piv.rsoi[setIndex].roiParam
        self.piv = piv
        self.t = piv.t
        self.ux0 = np.zeros_like(piv.t); self.uy0 = np.zeros_like(piv.t)
        self.ux1 = np.zeros_like(piv.t); self.uy1 = np.zeros_like(piv.t)
        self.ux2 = np.zeros_like(piv.t); self.uy2 = np.zeros_like(piv.t)
        
        self.roi = []
        
        for roiIndex in range(0,self.roiParam.x0.shape[0]):
            print('add content!')
            self.roi.append(ROI(self.t, self.piv, self.roiParam, roiIndex))

        self.roi = np.asarray(self.roi)

        # Script to flip contractile functions....
        nRoi = self.roi.shape[0]
        print(nRoi)

        plotFlip(self.roi)


        for i in range(0, nRoi):
            self.ux0 = self.ux0 + self.roi[i].ux0/nRoi
            self.ux1 = self.ux1 + self.roi[i].ux1/nRoi
            self.ux2 = self.ux2 + self.roi[i].ux2/nRoi
            self.uy0 = self.uy0 + self.roi[i].uy0/nRoi
            self.uy1 = self.uy1 + self.roi[i].uy1/nRoi
            self.uy2 = self.uy2 + self.roi[i].uy2/nRoi




########################################################
########################################################
########################################################
########################################################
########################################################


class PIV(object):
    """Class documentation here...
    """
    def __init__(self, filename):
        print('Importing data:')

        # Import data from .npz:
        data = np.load(filename)
        self.t=data['t']; self.x=data['x']; self.y=data['y']; self.ux1=data['ux1']; self.uy1=data['uy1']; self.mag1=data['mag1']
        self.ang1=data['ang1']; self.p1=data['p1']; self.ux2=data['ux2']; self.uy2=data['uy2']; self.mag2=data['mag2']
        self.p2=data['p2']; self.ux0=data['ux0']; self.uy0=data['uy0']; self.mag0=data['mag0']; self.side=data['side']
        self.pivN=data['pivN']; self.nFrames=data['nFrames']; self.dt=data['dt']; self.dx=data['dx']




    def selectRegionSet(self, plotScale=1, rsoiID='default'):

        try:
            self.rsoi
        except AttributeError:
            self.rsoi = []
        
        self.rsoi.append(RegionSet(self, plotScale, rsoiID))
        self.rsoi[-1].roiParam.x0 = np.asarray(self.rsoi[-1].roiParam.x0)
        self.rsoi[-1].roiParam.x1 = np.asarray(self.rsoi[-1].roiParam.x1)
        self.rsoi[-1].roiParam.y0 = np.asarray(self.rsoi[-1].roiParam.y0)
        self.rsoi[-1].roiParam.y1 = np.asarray(self.rsoi[-1].roiParam.y1)
        nRsoi = len(self.rsoi)


    ######################################################  


    #####################################################
    #####################################################
    #####################################################
    #####################################################
    #####################################################
    #####################################################
    #  DATA VISUALIZATION
    #####################################################
    #####################################################
    #####################################################
    #####################################################

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


#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#####################################################
#  CLASS TOOLBOX
#####################################################
#####################################################
#####################################################
#####################################################



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

      


class RegionSet:

    def __init__(self, piv, scale=1, screenID='default'):

        print('analysis loop')
        self.analysisID = screenID
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.12, bottom=0.2)

        Q = ax.quiver(piv.x[:,0], -piv.y[:,0], piv.ux1[:,0], -piv.uy1[:,0], pivot='mid', color='r', units='inches', scale=scale)
    
        axcolor = 'lightgoldenrodyellow'
        axframe = plt.axes([0.12, 0.1, 0.78, 0.03], axisbg=axcolor)
        sframe = Slider(axframe, 'Frame', 0, piv.nFrames, valinit=0)
    
        def update(val):
            n = np.round(sframe.val)
            U = piv.ux1[:,n]
            V = -piv.uy1[:,n]
            Q.set_UVC(U,V)
            fig.canvas.draw_idle()

        sframe.on_changed(update)

        resetAx = plt.axes([0.8, 0.025, 0.1, 0.04])
        roiAx = plt.axes([0.6, 0.025, 0.1, 0.04])
        completeAx = plt.axes([0.4, 0.025, 0.1, 0.04])
        button3 = Button(completeAx, 'Complete', color=axcolor, hovercolor='0.975')
        button2 = Button(resetAx, 'Reset', color=axcolor, hovercolor='0.975')
        button1 = Button(roiAx, 'ROI', color=axcolor, hovercolor='0.975')
    
        def reset(event):
            sframe.reset()
        def roiSelect(event):
            print('Select ROI')
            self.roiParam = RectangleBuilder2(ax)
            self.roiParam.connect()

        def completeSelection(event):
            plt.close(fig)

        button3.on_clicked(completeSelection)
        button2.on_clicked(reset)
        button1.on_clicked(roiSelect)

        plt.show()
        

        

