import ghhops_server as hs
from itertools import *

import rhino3dm

_INPUTS_DEF = {'run': hs.HopsBoolean(
        'run',
        'run',
        'default test input,'
        ' default=True,'
        ' if want enable this hops, set False',
        hs.HopsParamAccess.ITEM,
        False,
        True)}

_OUTPUTS_DEF = {'strings': [
    ('out', hs.HopsString(
        'out',
        'out',
        'output field for text data, errors and other messages, and python console',
        hs.HopsParamAccess.LIST,
        False,
        'no output'))
]
}

ints = [
    ('axis', 0),
        ('num', 50)]
floats = [
    ('start', 1),
        ('stop', 10),
        ('step', 1),
        ('base', 10.0)]
string = [('indexing', 'xy')]
bools = [
    ('endpoint', True),
        ('retstep', False),
        ('sparse',False),
        ('copy',True),
         ('run',True)
]
points = [
    ('points', list)
]

in_array = [('in_array')]
out_array = [('out_np_array')]

prms_hs, outp, outppt =[], [], []
prms_py = list(chain(ints, floats, bools, string, points))


for i in ints:
    prms_hs.append((i[0], hs.HopsInteger(i[0], i[0], i[0], default=i[1])))

for i in floats:
    prms_hs.append((i[0], hs.HopsNumber(i[0], i[0], i[0], default=i[1])))

for i in bools:
    prms_hs.append((i[0], hs.HopsBoolean(i[0], i[0], i[0], default=i[1])))

for i in string:
    prms_hs.append((i[0], hs.HopsString(i[0], i[0], i[0], default=i[1])))


prms_hs.append(('points', hs.HopsPoint('pts', 'pts', 'pts', access=hs.HopsParamAccess.LIST)))


for i in out_array:
    outp.append(hs.HopsNumber(i[0], i[0], i[0], access=hs.HopsParamAccess.LIST, optional=True))

outppt.append(hs.HopsPoint('pt_out', 'pt_out', 'pt_out', access=hs.HopsParamAccess.LIST, optional=True))

prms_py = dict(prms_py)

