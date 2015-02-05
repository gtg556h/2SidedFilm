import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
import pdb




def plotFlip(cargo):
    # Need to add buttons for flip x, flip y, complete,
    # Need to adjust formatting

    x = np.array([1,2,3,4])
    y = x**2

    flipXState = 0
    flipYState = 0

    fig = plt.figure(figsize=(8,8))
    #fig, ax = plt.subplots()
    fig.subplots_adjust(top=0.9, bottom=0.15, left=0.1, right=0.95, wspace=0.1, hspace=0.1)
    axcolor = 'lightgoldenrodyellow'

    ax1 = fig.add_subplot(111)
    line1, = ax1.plot(x,y)
    #ax1.title = 'Flip x?'

    xFlipAx = plt.axes([0.6, 0.025, 0.1, 0.04])
    completeAx = plt.axes([0.4, 0.025, 0.1, 0.04])

    button3 = Button(completeAx, 'Complete', color=axcolor, hovercolor='0.975')
    button2 = Button(xFlipAx, 'Flip X', color=axcolor, hovercolor='0.975')
    print('Need to embed',cargo)

    pdb.set_trace()


    def flipX(event):
        # Need to integrate a lambda function or something here...
        # See http://stackoverflow.com/questions/173687/is-it-possible-to-pass-arguments-into-event-bindings
        print('Flip X!')
        #pdb.set_trace()
        #if flipXState == 0:
        #    line1.set_ydata(-roi[i].ux1)
        #    flipXState = 1
        #else:
        #    line1.set_ydata(roi[i].ux1)
        #    flipXState = 0
        #fig.canvas.draw_idle()


    def completeSelection(event):
        if flipXState == 1:
            roi[i].ux1 = -roi[i].ux1
        if flipYState == 1:
            roi[i].uy1 = -roi[i].uy1
        plt.close(fig)

    button3.on_clicked(completeSelection)
    button2.on_clicked(flipX)

    plt.show()
    plt.close(fig)
    return 
   

        
plotFlip('hello')
        

