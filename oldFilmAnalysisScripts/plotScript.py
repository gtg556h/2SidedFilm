import loadData
import findEvents
import numpy as np
import matplotlib.pyplot as plt
import syncLib2

plt.rcParams.update({'font.size':11})


t1, t2, t3, b1, b2, b3, b4, t, refx, refy = loadData.loadTrack2()

t1 = loadData.flattenVector(t1)
t2 = loadData.flattenVector(t2)
t3 = loadData.flattenVector(t3)
b1 = loadData.flattenVector(b1)
b2 = loadData.flattenVector(b2)
b3 = loadData.flattenVector(b3)
b4 = loadData.flattenVector(b4)
t = loadData.flattenVector(t)
refx = loadData.flattenVector(refx)
refy = loadData.flattenVector(refy)

t1 = t1-np.mean(t1)
b1 = b1-np.mean(b1)
l1 = b1   # Falling into line with new notation of leading, trailing
tix = findEvents.findEvents2(t1,t)
lix = findEvents.findEvents2(b1,t)

tPhase, tixDiff = syncLib2.phaseGen(tix,t)
lPhase, lixDiff = syncLib2.phaseGen(lix,t)

plotRange = range(np.max([tix[0],lix[0]]),np.min([tix[-1],lix[-1]])+1)
dPhase = (lPhase[plotRange] - tPhase[plotRange])%1


#######################################################
# PLOTS

if 0:
    fig = plt.figure()
    plt.hold(True)
    ax = plt.axes()
    ax.set_xlim([0,2])
    plt.plot(t,l1,linewidth=1.0)
    plt.plot(t[ix],l1[ix],'r.')
    plt.show()

#######################################################

if 0:
    #fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(3,5))
    fig = plt.figure(figsize=(3,5))
    #fig.tight_layout()
    #fig.suptitle('filmAlpha_analysis', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.95, bottom=0.1, left=0.21, right=0.95, wspace=0.26, hspace=0.2)

    ax1 = fig.add_subplot(211)
    ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.',t,l1/np.max(l1),'b',t[lix],l1[lix]/np.max(l1),'r.')
    #ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.')
    ax1.set_xlim([0,np.max(t)])
    ax1.set_ylim([-0.3,1])
    #ax1.set_xlabel('t [s]')
    ax1.set_ylabel('Cell contraction (scaled)')
    
    ax2 = fig.add_subplot(212)
    ax2.plot(t[plotRange],dPhase,linewidth=1.0)
    ax2.axis([np.min(t[plotRange]),np.max(t[plotRange]),0,1])
    ax2.set_xlabel('t [s]')
    #ax2.set_xticks(np.arange(0,8))
    ax2.set_ylabel('Phase diff (cycles)')
    
    plt.savefig('filmAlphaPhaseDifferential.eps', dpi=300, facecolor='w')
    plt.show()


############################################################

if 0:
    plotRange0 = plotRange
    #plotRange = plotRange[0:np.int(len(plotRange)/2)]
    plotRange = plotRange[np.int(len(plotRange)/2):len(plotRange)]
    t0 = t[plotRange[0]]
    fig = plt.figure(figsize=(6,2))

    fig.subplots_adjust(top=0.93, bottom=0.1, left=0.06, right=0.98, wspace=0.56, hspace=0.2)

    ax1 = fig.add_subplot(131)
    ax1.plot(t[plotRange]-t0,t1[plotRange]/np.max(t1),'g',t[tix]-t0,t1[tix]/np.max(t1),'r.')
    #ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.')
    ax1.set_xlim([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0])
    ax1.set_ylim([-0.4,1])
    #ax1.set_xlabel('t [s]')
    ax1.set_xticks(np.arange(0,4))
    #ax1.set_ylabel('Cell contraction (scaled)')
    ax1.set_yticks(np.arange(-.4,1,.4))
    
    ax2 = fig.add_subplot(132)
    ax2.plot(t[plotRange]-t0,tPhase[plotRange],linewidth=1.0)
    ax2.axis([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0,0,1])
    #ax2.set_xlabel('t [s]')
    ax2.set_xticks(np.arange(0,4))
    #ax2.set_ylabel('Phase diff (cycles)')
    ax2.set_yticks(np.arange(0,1.2,.5))

    ax3 = fig.add_subplot(133)
    ax3.plot(t[plotRange0]-t[plotRange0[0]],dPhase,linewidth=1.0)
    ax3.axis([np.min(t[plotRange0])-t[plotRange0[0]],np.max(t[plotRange0])-t[plotRange0[0]],0,1])
    #ax3.set_xlabel('t [s]')
    ax3.set_xticks(np.arange(0,8,2))
    ax3.set_yticks(np.arange(0,1.2,.5))
    #ax3.set_ylabel('Phase diff (cycles)')
 
    
    plt.savefig('conferenceOutput.eps', dpi=300, facecolor='w')
    plt.show()


############################################################
if 0:
    plotRange0 = plotRange
    plotRange = plotRange[0:np.int(len(plotRange)*.6)]
    #plotRange = plotRange[np.int(len(plotRange)/2):len(plotRange)]
    t0 = t[plotRange[0]]
    fig = plt.figure(figsize=(6,2))

    fig.subplots_adjust(top=0.93, bottom=0.1, left=0.06, right=0.98, wspace=0.56, hspace=0.2)

    ax1 = fig.add_subplot(131)
    ax1.plot(t[plotRange]-t0,t1[plotRange]/np.max(t1),'g',t[tix]-t0,t1[tix]/np.max(t1),'b.',t[plotRange]-t0,b1[plotRange]/np.max(b1),'r',t[lix]-t0,b1[lix]/np.max(b1),'b.')
    #ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.')
    ax1.set_xlim([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0])
    ax1.set_ylim([-0.4,1])
    #ax1.set_xlabel('t [s]')
    ax1.set_xticks(np.arange(0,4))
    #ax1.set_ylabel('Cell contraction (scaled)')
    ax1.set_yticks(np.arange(-.4,1,.4))
    
    ax2 = fig.add_subplot(132)
    ax2.plot(t[plotRange]-t0,tPhase[plotRange],'g',t[plotRange]-t0,lPhase[plotRange],'r',linewidth=1.0)
    ax2.axis([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0,0,1])
    #ax2.set_xlabel('t [s]')
    ax2.set_xticks(np.arange(0,4))
    #ax2.set_ylabel('Phase diff (cycles)')
    ax2.set_yticks(np.arange(0,1.2,.5))

    ax3 = fig.add_subplot(133)
    ax3.plot(t[plotRange0]-t[plotRange0[0]],dPhase,linewidth=1.0)
    ax3.axis([np.min(t[plotRange0])-t[plotRange0[0]],np.max(t[plotRange0])-t[plotRange0[0]],0,1])
    #ax3.set_xlabel('t [s]')
    ax3.set_xticks(np.arange(0,8,2))
    ax3.set_yticks(np.arange(0,1.2,.5))
    #ax3.set_ylabel('Phase diff (cycles)')
 
    
    plt.savefig('conferenceOutput_2waveform.eps', dpi=300, facecolor='w')
    plt.show()


# WCB plot:
if 1:
    plotRange0 = plotRange
    plotRange = plotRange[0:np.int(len(plotRange)*.6)]
    #plotRange = plotRange[np.int(len(plotRange)/2):len(plotRange)]
    t0 = t[plotRange[0]]
    fig = plt.figure(figsize=(3,6))

    fig.subplots_adjust(top=0.93, bottom=0.1, left=0.21, right=0.98, wspace=0.56, hspace=0.2)

    ax1 = fig.add_subplot(311)
    ax1.plot(t[plotRange]-t0,t1[plotRange]/np.max(t1),'b',t[tix]-t0,t1[tix]/np.max(t1),'r.',t[plotRange]-t0,b1[plotRange]/np.max(b1),'g',t[lix]-t0,b1[lix]/np.max(b1),'r.')
    #ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.')
    ax1.set_xlim([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0])
    ax1.set_ylim([-0.4,1])
    #ax1.set_xlabel('t [s]')
    ax1.set_xticks(np.arange(0,4))
    ax1.set_ylabel('Displacement (scaled)')
    ax1.set_yticks(np.arange(-.4,1,.4))
    ax1.set_yticklabels(['-.4','0.0','0.4','0.8'])
    
    ax2 = fig.add_subplot(312)
    ax2.plot(t[plotRange]-t0,tPhase[plotRange],'b',t[plotRange]-t0,lPhase[plotRange],'g',linewidth=1.0)
    ax2.axis([np.min(t[plotRange])-t0,np.max(t[plotRange])-t0,0,1])
    #ax2.set_xlabel('t [s]')
    ax2.set_xticks(np.arange(0,4))
    ax2.set_ylabel('Phase (cycles)')
    ax2.set_yticks(np.arange(0,1.2,.5))

    ax3 = fig.add_subplot(313)
    ax3.plot(t[plotRange0]-t[plotRange0[0]],dPhase,linewidth=1.0)
    ax3.axis([np.min(t[plotRange0])-t[plotRange0[0]],np.max(t[plotRange0])-t[plotRange0[0]],0,1])
    ax3.set_xlabel('t [s]')
    ax3.set_xticks(np.arange(0,8,2))
    ax3.set_yticks(np.arange(0,1.2,.5))
    ax3.set_ylabel('Phase diff (cycles)')
 
    
    plt.savefig('phaseConversion.eps', dpi=300, facecolor='w')
    plt.show()



