#!/bin/python3


####################
# MODULES ##########
####################

import numpy as np
import matplotlib.pyplot as plt
import PIVLib
import sys
import pdb
import re
import pickle


####################
# PROCESSING #######
####################

filename = sys.argv[1]
print(filename)
p1 = PIVLib.PIV(filename)
if len(sys.argv)==3:
    scale = np.int(sys.argv[2])
else:
    scale=30
    

p1.quiver(scale)

p1.selectRegionSet(scale, 'set1')
p1.selectRegionSet(scale, 'set2')

set1 = PIVLib.RSOI(p1, len(p1.rsoi)-2)
set2 = PIVLib.RSOI(p1, len(p1.rsoi)-1)

t = set1.t
tt = t[np.max([set1.ix[0], set2.ix[0]]):np.min([set1.ix[-1],set2.ix[-1]])]
dtheta = np.mod(set1.theta-set2.theta, 1)
dtheta = dtheta[np.max([set1.ix[0], set2.ix[0]]):np.min([set1.ix[-1],set2.ix[-1]])]



#####################
# DATA MGT ##########
#####################


# Save pickle:
data = {'p1': p1, 'set1': set1, 'set2': set2, 'dtheta': dtheta, 'tt': tt, 't':t}
output=re.sub(r'.npz', '.pkl', filename)
pickle.dump(data, open( output, "wb" ) )
# Load pickle:
# data = pickle.load( open( filename, "rb" ) )



# Save numpy arrays:
output=re.sub(r'.npz', '_syncAnalysis.npz', filename)
np.savez(output,dtheta=dtheta, tt=t, t=t, ix1=set1.ix, theta1=set1.theta, ix2=set2.ix, theta2=set2.theta)
# Load numpy array:
# data = np.load(filename)
# t = data['t']
# ...



######################
# PLOTS ##############
######################


# Plot dtheta:

def plotResults(tt,dtheta,filename):
    fig = plt.figure(figsize=(12,5.2))
    fig.subplots_adjust(top=0.84, bottom=0.1, left=0.06, right=0.98, wspace=0.24, hspace=0.24)
    fig.suptitle(re.sub(r'.npz', '', filename), fontsize=16)

    ax1 = fig.add_subplot(131)
    ax1.plot(tt-tt[0],dtheta)
    ax1.set_xlabel("t")
    ax1.set_ylabel("dtheta")
    ax1.set_ylim([0,1])
    
    ax2 = fig.add_subplot(132)
    ax2.hist(dtheta,20)
    ax2.set_xlabel('dtheta')
    ax2.set_ylabel("frequency")

    ax3 = fig.add_subplot(133)
    ax3.scatter(dtheta[1:],np.diff(dtheta)/(tt[2]-tt[1]))
    ax3.set_xlabel('dtheta')
    ax3.set_xlabel("dtheta$_t$")
                 
    #p = re.compile('.npz')
    #string = p.sub('dtheta.eps', filename)
    #plt.savefig(string)

    plt.savefig(re.sub(r'.npz', '_dtheta.eps', filename))
    plt.show()

plotResults(tt,dtheta,filename)




