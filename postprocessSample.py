import numpy as np
import postprocessPIVLib2 as PL

side = 0   # Side of film index.  For 2sided film analyses.
pivN = 1   # PIV Pass to import.  Lowest resolution is 1.
nFrames = 200  # Number of frames to process
dt = 0.01 # sec
baseDirectory = "/Users/brian/working/1sFilmPIV/"  

outFilename = "trial"

PL.process(baseDirectory, outFilename, side, pivN, nFrames, dt)

