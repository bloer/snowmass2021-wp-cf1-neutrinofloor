#!/usr/bin/env python
import numpy as np
import pathlib
import io
import re

def extractpoints(filename):
    with open(filename) as f:
        contents = f.read()
        #sub = contents.split('{{')[2].split('}}')[0]
        #sub = sub.replace('\n','').replace('{','').replace('},','\n')
        #sub = sub.replace(',','').replace('*^','e')
        match = re.match(r'<data-values>\n(.*)</data-values>',contents)
        return np.loadtxt(io.StringIO(match.groups()[0]))
        
def filename(infix):
    return f'orig/NRDM_{infix}_bkgSNOLAB_detSNOLAB_7tower.limit'

def findmin(data1, data2):
    x = np.sort(np.concatenate([data1[:,0], data2[:,0]]))
    y1 = np.interp(x, data1[:, 0], data1[:,1], left=np.inf, right=np.inf)
    y2 = np.interp(x, data2[:, 0], data2[:,1], left=np.inf, right=np.inf)
    return np.array([x, np.minimum(y1, y2)]).T

if __name__ == '__main__':
    import sys
    
    dtypes = ('Ge_HV', 'Ge_iZIP', 'Si_iZIP', 'Si_HV')
    data = {}
    for dt in dtypes:
        data[dt] = extractpoints(filename(dt))
        np.savetxt(f'SuperCDMS_SNOLAB_{dt}.tsv', data[dt])
        
    data['Ge'] = findmin(data['Ge_iZIP'], data['Ge_HV'])
    np.savetxt(f'SuperCDMS_SNOLAB_Ge_Combined.tsv', data['Ge'])
    data['Si'] = findmin(data['Si_iZIP'], data['Si_HV'])
    np.savetxt(f'SuperCDMS_SNOLAB_Si_Combined.tsv', data['Si'])
    data['all'] = findmin(data['Ge'], data['Si'])
    np.savetxt(f'SuperCDMS_SNOLAB_Combined.tsv', data['all'])
    
    
    

    
