import loadData
import findEvents
import numpy as np
import matplotlib.pyplot as plt
import syncLib2


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

if 1:
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
    fig.tight_layout()
    fig.suptitle('filmAlpha_analysis', fontsize=14, fontweight='bold')
    fig.subplots_adjust(top=0.9, bottom=0.1, left=0.1, right=0.95, wspace=0.26, hspace=0.2)

    ax1 = fig.add_subplot(121)
    ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.',t,l1/np.max(l1),'b',t[lix],l1[lix]/np.max(l1),'r.')
    #ax1.plot(t,t1/np.max(t1),'g',t[tix],t1[tix]/np.max(t1),'r.')
    ax1.set_xlim([0,np.max(t)])
    ax1.set_ylim([-0.3,1])
    ax1.set_xlabel('t [s]')
    ax1.set_ylabel('Cell contraction (scaled)')
    
    ax2 = fig.add_subplot(122)
    ax2.plot(t[plotRange],dPhase,linewidth=1.0)
    ax2.axis([np.min(t[plotRange]),np.max(t[plotRange]),0,1])
    ax2.set_xlabel('t [s]')
    ax2.set_ylabel('Phase diff (cycles)')
    
    plt.savefig('filmAlphaPhaseDifferential.eps', dpi=300, facecolor='w')
    plt.show()




