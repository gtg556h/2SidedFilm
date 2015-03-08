import loadData
import numpy as np
import matplotlib.pyplot as plt


t1, t2, t3, b1, b2, b3, b4, t, refx, refy = loadData.loadTrack2()

#t1 = t1-np.mean(t1)
#t2 = t2-np.mean(t2)
#t3 = t3-np.mean(t3)

# Plot ALL Waveforms
if 0:
    fig = plt.figure(figsize=(7,4))
    ax = plt.subplot(111)
    ax.plot(t,t1,'b',t,t3,'b',t,t3,'b',t,b1,'r',t,b2,'r',t,b3,'r',t,b4,'r')
    ax.set_xlim([0,np.max(t)])
    ax.set_xlabel('t [s]')
    ax.set_ylabel('Displacement [' + r'$\mu $'+ 'm]')
    plt.subplots_adjust(bottom=.15,top=.9)
    ax.set_title('Tracked cell displacements')



    plt.savefig('allWaveforms.png', dpi=300, facecolor='w')
    plt.show()

# Plot mean waveforms
if 1:
    fig = plt.figure(figsize=(7,4))
    ax = plt.subplot(111)
    top = (t1+t2+t3)/3.0
    bot = (b1+b2)/2.0 # Only using 2 waveforms: there appear to be distinct patterns  on the bottom (while both lagging), and meaning the two (with such small sample size) gives a gross appearance

    ax.plot(t,top,'b',t,bot,'r')
    ax.set_xlim([0,np.max(t)])
    ax.set_xlabel('t [s]')
    ax.set_ylabel('Dispplacement [' + r'$\mu $' + 'm]')
    plt.subplots_adjust(bottom=0.15, top=0.85)
    ax.set_title('Tracked mean displacements \n (handpicked trailing waveforms)')

    plt.savefig('meanWaveforms.png',dpi=300,facecolor='w')
    plt.show()

# Plot leading waveforms
if 0:
    fig = plt.figure(figsize=(7,4))
    ax = plt.subplot(111)

    ax.plot(t,t1,'b',t,t2,'r',t,t3,'g')
    ax.set_xlim([0,np.max(t)])
    ax.set_xlabel('t [s]')
    ax.set_ylabel('Dispplacement [' + r'$\mu $' + 'm]')
    plt.subplots_adjust(bottom=0.15, top=0.9)
    ax.set_title('Leading side tracked waveforms')

    plt.savefig('leadingWaveforms.eps',dpi=300,facecolor='w')
    plt.show()

# Plot trailing waveforms
if 0:
    fig = plt.figure(figsize=(7,4))
    ax = plt.subplot(111)

    ax.plot(t,b1,'b',t,b2,'r',t,b3,'g',t,b4,'c')
    ax.set_xlim([0,np.max(t)])
    ax.set_xlabel('t [s]')
    ax.set_ylabel('Dispplacement [' + r'$\mu $' + 'm]')
    plt.subplots_adjust(bottom=0.15, top=0.9)
    ax.set_title('Trailing side tracked waveforms')

    plt.savefig('trailingWaveforms.eps',dpi=300,facecolor='w')
    plt.show()
    

if 0:
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7,7))
    fig.tight_layout()
    fig.suptitle('Relationship of individual trailing \n waveforms to leading waveform',fontsize=14,fontweight='bold')
    fig.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, wspace=0.2, hspace=0.2)
    plt.hold(True)

    top = (t1+t2+t3)/3.0

    ax1 = fig.add_subplot(221)
    #ax1.set_title('Title')
    ax1.plot(t,top,'b',t,b1,'r')
    leg = ax1.legend(('Leading','Trailing'),'upper right', shadow=True, fancybox=True, labelspacing=0.2)
    ax1.set_ylim([-0.1,1.3])
    for tt in leg.get_texts():
        tt.set_fontsize('small')

    ax2 = fig.add_subplot(222)
    ax2.set_ylim([-0.1,1.3])
    #ax1.set_title('Title')
    ax2.plot(t,top,'b',t,b2,'r')

    ax3 = fig.add_subplot(223)
    ax3.set_ylim([-0.1,1.3])
    #ax1.set_title('Title')
    ax3.plot(t,top,'b',t,b3,'r') 

    ax4 = fig.add_subplot(224)
    ax4.set_ylim([-0.1,1.3])
    #ax1.set_title('Title')
    ax4.plot(t,top,'b',t,b4,'r')

    plt.savefig('individualTrailingWaveforms.eps',dpi=300,facecolor='w')
    plt.show()




