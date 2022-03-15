#!/usr/bin/env python
import numpy as np
import pathlib

def convertfile(filename):
    data = np.loadtxt(filename, delimiter='\t')
    data[:,1] *= 1.e-36
    np.savetxt(pathlib.Path(filename).with_suffix('.csv').name, data,
               delimiter=',')

if __name__ == '__main__':
    import sys
    for filename in sys.argv[1:]:
        convertfile(filename)

    
