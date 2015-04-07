import numpy as np
import matplotlib.pyplot as plt
import PIVLib
import sys

filename = sys.argv[0]

p1 = PIVLib.PIV(filename)
if len(sys.argv)==2:
    scale = sys.argv[1]
else:
    scale=30
    

p1.quiver(scale)

p1.selectRegionSet(scale, 'set1')
p1.selectRegianSet(scale, 'set2')

set1 = PIVLib.RSOI(p1, len(p1.rsoi)-2)
set2 = PIVLib.RSOI(p1, len(p1.rsoi)-1)

dtheta = np.mod(set1-set2, 1)

plt.plot(dtheta)

#p = re.compile('.npz')
#string = p.sub('dtheta.eps', filename)
#plt.savefig(string)

plt.savefig(re.sub(r'.npz', '_dtheta.eps', filename))
plt.show()
