import numpy as np
import postprocessPIVLib as PL
import sys
import pdb

baseDirectory = sys.argv[1]
outFilename = sys.argv[2]
side = int(sys.argv[3])
pivN = int(sys.argv[4])
nFrames = int(sys.argv[5])
dt = float(sys.argv[6])
dx = float(sys.argv[7])


#side = 0   # Side of film index.  For 2sided film analyses.
#pivN = 1   # PIV Pass to import.  Lowest resolution is 1.
#nFrames = 200  # Number of frames to process
#dt = 0.01 # sec
#dx = 0.650 # microns/pixel
#baseDirectory = "/Users/brian/working/1sFilmPIV/"  

outFilename = "trial"



#print(sys.argv[1])
#print(sys.argv[2])
#print(2*int(sys.argv[3]))
#print(sys.argv[4])
#print(sys.argv[5])
#print(sys.argv[6])
#print(sys.argv[7])

PL.process(baseDirectory, outFilename, side, pivN, nFrames, dt, dx)

