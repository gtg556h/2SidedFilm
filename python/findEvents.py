import numpy as np
import pdb




def findEvents2(r, t, zeroWindow=3, smoothIndex = 3):
    dt = t[1]-t[0]
    amp = np.max(r) - np.min(r)

    zeroVal = np.zeros(r.shape)
    w = zeroWindow

    for i in range(0,np.int(np.round(w/dt))):
        zeroVal[i] = np.mean(r[0:np.round(w/dt)])
        
    for i in range(np.int(np.round(w/dt))+1,np.int(r.shape[0]-np.round(w/dt))):
        zeroVal[i] = np.mean(r[i-np.round(w/2/dt):i+np.round(w/2/dt)+1])

    for i in range(np.int(r.shape[0]-np.round(w/dt)+1),r.shape[0]):
        zeroVal[i] = np.mean(r[r.shape[0]-np.round(w/dt)+1:r.shape[0]])

    r1 = np.zeros([r.shape[0]+1])
    r2 = np.zeros([r.shape[0]+1])

    r1[0:r.shape[0]] = r
    r2[1:r.shape[0]+1] = r

    trig = np.zeros(r.shape[0])
    for i in range(0,r.shape[0]):
        trig[i] = zeroVal[i] + amp/6.0

    trig1 = np.zeros(r1.shape[0])
    trig2 = np.zeros(r1.shape[0])
    trig1[0:r.shape[0]] = trig
    trig2[1:r.shape[0]+1] = trig

    set1 = np.zeros(trig1.shape)
    set2 = np.zeros(trig2.shape)
    set1[np.where(r1-trig1>0)]=1 
    set2[np.where(r2-trig2<0)]=1
    rising = np.where(set1*set2==1)
    rising = rising[0]
    
    ix = np.zeros(rising.shape[0]-1)
    for i in range(0,rising.shape[0]-1):
        #pdb.set_trace() 
        temp = r[np.array(range(rising[i],rising[i+1]))]
        ix[i] = temp.argmax() + rising[i]

    ix = ix.astype(int)

    return ix




