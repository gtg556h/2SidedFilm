import numpy as np

def step_c(c,c_coupled,s,f,coupling, staticCa, randCa, leakageCoeff,fireThresh,fireAdd,flushRate,minThresh):
    if s == 1:
        c_out = c + fireAdd
        s = 0
        f = 1
    elif f == 1 and s == 0:
        c_out = c*(1-flushRate) + coupling
        if c_out < minThresh:
            s=0
            f=0
        else:
            s=0
            f=1
    else:
        c_out = c + coupling + randCa*np.random.rand() + staticCa - leakageCoeff*c
        if c_out > fireThresh:
            s=1
            f=0
        else:
            s=0
            f=0

    return c_out,s,f








