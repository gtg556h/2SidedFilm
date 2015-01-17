import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle

# from io import StringIO

class piv(object):
    def __init__(self, filename):
        print('Importing data:')

        # Import data from .npz:
        data = np.load(filename)
        self.t=data['t']; self.x=data['x']; self.y=data['y']; self.ux1=data['ux1']; self.uy1=data['uy1']; self.mag1=data['mag1']
        self.ang1=data['ang1']; self.p1=data['p1']; self.ux2=data['ux2']; self.uy2=data['uy2']; self.mag2=data['mag2']
        self.p2=data['p2']; self.ux0=data['ux0']; self.uy0=data['uy0']; self.mag0=data['mag0']; self.side=data['side']
        self.pivN=data['pivN']; self.nFrames=data['nFrames']; self.dt=data['dt']; self.dx=data['dx']

    #####################################################
    #####################################################




    def slider(self, scale=1):
    
        

        class RectangleBuilder:
            def __init__(self, ax):
                self.fig = ax.get_figure()
                self.ax = ax
                self.x0 = []
                self.y0 = []
                self.x1 = []
                self.y1 = []

            def connect(self):
                self.cidpress = fig.canvas.mpl_connect('button_press_event', self.on_press)
                self.cidpress = fig.canvas.mpl_connect('button_release_event', self.on_release)

            def on_press(self, event):
                print('click', event)
                if event.inaxes!=self.ax: return
                self.x0.append(event.xdata)
                self.y0.append(event.ydata)

            def on_release(self, event):
                print('release', event)
                if event.inaxes!=self.ax: return
                self.x1.append(event.xdata)
                self.y1.append(event.ydata)
                self.draw_rectangle()

            def draw_rectangle(self):
                x0_ = self.x0[len(self.x0)-1]; y0_ = self.y0[len(self.y0)-1];
                x1_ = self.x1[len(self.x1)-1]; y1_ = self.y1[len(self.y1)-1];
                rect = ax.add_patch(patches.Rectangle((x0_,y0_),(x1_-x0),(y1_-y0)))
                self.fig.canvas.draw()

            
        
        
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.12, bottom=0.2)

        #l, = plt.plot(t,s, lw=2, color='red')
        Q = ax.quiver( self.x[:,0], -self.y[:,0], self.ux1[:,0], -self.uy1[:,0], pivot='mid', color='r', units='inches', scale=scale)
        #plt.axis([0, 1, -10, 10])

        axcolor = 'lightgoldenrodyellow'
        #axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
        axframe  = plt.axes([0.12, 0.1, 0.78, 0.03], axisbg=axcolor)

        #sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
        sframe = Slider(axframe, 'Frame', 0, self.nFrames, valinit=0)

        def update(val):
            n = np.round(sframe.val)
            #freq = sfreq.val

            U = self.ux1[:,n]
            V = -self.uy1[:,n]
            Q.set_UVC(U,V)
            #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
            fig.canvas.draw_idle()

        #sfreq.on_changed(update)
        sframe.on_changed(update)

        resetAx = plt.axes([0.8, 0.025, 0.1, 0.04])
        roiAx = plt.axes([0.6, 0.025, 0.1, 0.04])
        button2 = Button(resetAx, 'Reset', color=axcolor, hovercolor='0.975')
        button1 = Button(roiAx, 'ROI', color=axcolor, hovercolor='0.975')
        def reset(event):
            #sfreq.reset()
            sframe.reset()

        def roiSelect(event):
            print('Select ROI')
            self.roi = RectangleBuilder(ax)

        button2.on_clicked(reset)
        button1.on_clicked(roiSelect)

        #rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
        #radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)
        #def colorfunc(label):
        #    l.set_color(label)
        #    fig.canvas.draw_idle()
        #radio.on_clicked(colorfunc)

        plt.show()


    #####################################################
    #####################################################

    #def annotate(self):


    #    class Annotate(object):
    #        def __init__(self):
    #            self.ax = plt.gca()
    #            self.rect = Rectangle((0,0), 1, 1)
    #            self.x0 = None
    #            self.y0 = None
    #            self.x1 = None
    #            self.y1 = None
    #            self.ax.add_patch(self.rect)
    #            self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
    #            self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)

    #        def on_press(self, event):
    #            print('press')
    #            self.x0 = event.xdata
    #            self.y0 = event.ydata

    #        def on_release(self, event):
    #            print('release')
    #            self.x1 = event.xdata
    #            self.y1 = event.ydata
    #            self.rect.set_width(self.x1 - self.x0)
    #            self.rect.set_height(self.y1 - self.y0)
    #            self.rect.set_xy((self.x0, self.y0))
    #            self.ax.figure.canvas.draw()

    #    a = Annotate()
    #    plt.show()

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



#class Annotate(object):
#    def __init__(self):
#        self.ax = plt.gca()
#        self.rect = Rectangle((0,0), 1, 1)
#        self.x0 = None
#        self.y0 = None
#        self.x1 = None
#        self.y1 = None
#        self.ax.add_patch(self.rect)
#        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
#        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)

#    def on_press(self, event):
#        print('press')
#        self.x0 = event.xdata
#        self.y0 = event.ydata

#    def on_release(self, event):
#        print('release')
#        self.x1 = event.xdata
#        self.y1 = event.ydata
#        self.rect.set_width(self.x1 - self.x0)
#        self.rect.set_height(self.y1 - self.y0)
#        self.rect.set_xy((self.x0, self.y0))
#        self.ax.figure.canvas.draw()
