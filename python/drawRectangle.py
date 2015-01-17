from matplotlib import pyplot as plt
import matplotlib.patches as patches


class RectangleBuilder:
    def __init__(self, ax):
        #self.fig = fig
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
        rect = ax.add_patch(patches.Rectangle((x0_,y0_),(x1_-x0_),(y1_-y0_)))
        self.fig.canvas.draw()

    
    #def releaseDraw(self):


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('Click and drag to draw rectangle masks:')
r = RectangleBuilder(ax)

r.connect()
plt.show()


