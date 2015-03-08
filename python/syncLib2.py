import numpy as np
# Take ix, t vector, output phase vector, assuming linear phase propagation between discrete set of events

def phaseGen(ix,t):
    phase = np.zeros(t.shape)
    ixDiff = np.diff(ix,n=1,axis=0)
    for ii in range(0,ix.shape[0]-1):
        #phase[ix[ii,0],0] = 0
        for jj in range(0,ixDiff[ii]+1):
            phase[ix[ii]+jj] = (jj)/float(ixDiff[ii])


    return phase, ixDiff

#######################################################
def cyclicData(r, t, min, max):
    r1 = np.concatenate((np.zeros((1,)), r))
    r2 = np.concatenate((r, np.zeros((1,))))
    if np.mean(np.diff(r)/np.abs(np.diff(r))) < 0:
        sign = -1
        r_array, t_array = negPhase(r1, r2, t, min, max)    
    else:
        sign = 1
        r_array, t_array = posPhase(r1, r2, t, min, max)

    return r_array, t_array

#######################################################
def negPhase(r1, r2, t, min, max):
    k1 = 1
    r_array = np.array([], dtype=object)
    t_array = np.array([], dtype=object)
    phaseRange = max-min

    for ii in range(1,r1.shape[0]):
        if r2[ii] > 0.7*phaseRange and r1[ii] < 0.3*phaseRange:
            k2 = ii+1
            r_array = np.concatenate((r_array, np.zeros((1,))))
            r_array[r_array.shape[0]-1] = r1[k1:k2]
            t_array = np.concatenate((t_array, np.zeros((1,))))
            t_array[t_array.shape[0]-1] = t[k1-1:k2-1]
            k1 = ii+1 
             
    if k1 < r1.shape[0]-1:
        r_array = np.concatenate((r_array, np.zeros((1,))))
        r_array[r_array.shape[0]-1] = r1[k1:r1.shape[0]-1]
        t_array = np.concatenate((t_array, np.zeros((1,))))
        t_array[t_array.shape[0]-1] = t[k1-1:k2-1]

    return r_array, t_array

#######################################################
def posPhase(r1, r2, t, min, max):
    k1 = 1
    r_array = np.array([], dtype=object)
    t_array = np.array([], dtype=object)
    phaseRange = max-min

    for ii in range(1,r1.shape[0]):
        if r2[ii] < 0.7*phaseRange and r1[ii] > 0.3*phaseRange:
            k2 = ii+1
            r_array = np.concatenate((r_array, np.zeros((1,))))
            r_array[r_array.shape[0]-1] = r1[k1:k2]
            t_array = np.concatenate((t_array, np.zeros((1,))))
            t_array[t_array.shape[0]-1] = t[k1-1:k2-1]
            k1 = ii+1 
             
    if k1 < r1.shape[0]-1:
        r_array = np.concatenate((r_array, np.zeros((1,))))
        r_array[r_array.shape[0]-1] = r1[k1:r1.shape[0]-1]
        t_array = np.concatenate((t_array, np.zeros((1,))))
        t_array[t_array.shape[0]-1] = t[k1-1:k2-1]

    return r_array, t_array

#######################################################

#def phaseEndpoints(r, t)
#    for ii in range(1:r.shape[0]-1):
#        lowSlop 


