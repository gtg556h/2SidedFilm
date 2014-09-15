import numpy as np
import matplotlib.pyplot as plt
import postprocessPIVLib as pppl

path = "samplePIV.txt"

x, y, ux1, uy1, mag1 = pppl.process(path)

