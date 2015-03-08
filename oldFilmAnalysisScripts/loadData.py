import numpy as np
stem = '/home/brian/Dropbox/doc/research/projects/cardiac/20130630_MAIN_trackFilmAlpha/track2/numpySource/' 


def loadRefSource():

    x = np.load(stem+'refSource.npz')

    refx1 = x['refx1']
    refx2 = x['refx2']
    refx3 = x['refx3']

    refx = x['refx']
    refy = x['refy']
    t = x['t']

    return refx1, refx2, refx3, refx, refy, t

def loadRef():
    x = np.load('ref.npz')

    refx = x['refx']
    refy = x['refy']
    t = x['t']

    return refx, refy, t

def loadTrack2():
    x = np.load(stem+'track2.npz')
    t1 = x['t1']
    t2 = x['t2']
    t3 = x['t3']
    b1 = x['b1']
    b2 = x['b2']
    b3 = x['b3']
    b4 = x['b4']
    t = x['t']
    t=t.T
    refx = x['refx']
    refy = x['refy']

    return t1, t2, t3, b1, b2, b3, b4, t, refx, refy

def flattenVector(r):
    if r.shape[0]>r.shape[1]:
        r2 = np.zeros(r.shape[0])
        r2[0:r2.shape[0]] = r[0:r2.shape[0],0]
    elif r.shape[1]>r.shape[0]:
        r2 = np.zeros(r.shape[1])
        r2[0:r2.shape[0]] = r[0,0:r2.shape[0]]

    return r2




