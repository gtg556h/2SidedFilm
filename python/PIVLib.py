import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import pdb
import findEvents
import syncLib2
#from pivVisualization import VelocityField
from pivVisualizationLib import plotFlip,RectangleBuilder2,VelocityField,setPeakLimits

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

        # Flip contractile functions to match orientation:...
        nRoi = self.roi.shape[0]
        print(nRoi)
        plotFlip(self.roi)


        # Average waveforms:
        for i in range(0, nRoi):
            self.ux0 = self.ux0 + self.roi[i].ux0/nRoi
            self.ux1 = self.ux1 + self.roi[i].ux1/nRoi
            self.ux2 = self.ux2 + self.roi[i].ux2/nRoi
            self.uy0 = self.uy0 + self.roi[i].uy0/nRoi
            self.uy1 = self.uy1 + self.roi[i].uy1/nRoi
            self.uy2 = self.uy2 + self.roi[i].uy2/nRoi

        # Change of waveform basis:
        ampx = np.max(self.ux1) - np.min(self.ux1)
        ampy = np.max(self.uy1) - np.min(self.uy1)
        theta = np.arctan(ampy/ampx)
        self.u1 = np.cos(theta)*self.ux1 + np.sin(theta)*self.uy1
        self.v1 = -np.sin(theta)*self.ux1 + np.cos(theta)*self.uy1


        # Find events and compute phase conversion
        self.peakThreshold = setPeakLimits(self.t,self.u1)
        print('cool. the threshold is set.')
        print('Now modify findEvents.findEvents2 to utilize this parameter as a sieve!')
        print('Or just sieve as a postProcessing step.')
        print('In fact, it will be even better to detect events, then forward that plot, PEAK DOTS INCLUDED, to the peak threshold script!')
        self.ix = findEvents.findEvents2(self.u1, self.t, (np.max(self.t)-self.t[1]+self.t[0]))

        self.ix = self.ix[np.where(self.u1[self.ix] > self.peakThreshold)]

        self.theta, self.ixDiff = syncLib2.phaseGen(self.ix,self.t)

        # Plot resultant phase plot:
        self.plotMeanFuncs()



    ##############################################################
    def plotMeanFuncs(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(131)
        line1 = ax1.plot(self.t, self.ux1)
        ax2 = fig.add_subplot(132)
        line2 = ax2.plot(self.t, self.uy1)
        ax3 = fig.add_subplot(133)
        line3 = ax3.plot(self.t, self.u1)
        line4 = ax3.plot(self.t[self.ix], self.u1[self.ix], 'ro')
        plt.show()

    ##############################################################
    def plotPhaseGen(self):
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        line1a = ax1.plot(self.t, self.u1)
        line1b = ax1.plot(self.t[self.ix], self.u1[self.ix], 'ro')
        ax2 = fig.add_subplot(122)
        line2 = ax2.plot(self.theta)
        plt.show()




########################################################
########################################################
########################################################
########################################################
########################################################


class PIV(VelocityField):
    """Class documentation here...
    """
    def __init__(self, filename):
        print('Importing data:')
        VelocityField.__init__(self)

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


#
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
        

        

