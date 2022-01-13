import ghhops_server as hs
from itertools import *

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

_ints_input = [
    ('axis', 0),
    ('num', 50),
    ('a', 2),
    ('p', 21),
    ('u_count', 16),
    ('v_count', 16)
]

_floats_input = [
    ('start', 1),
    ('stop', 10),
    ('step', 1),
    ('base', 10.0),
    ('u', 1.5),
    ('v', 1.0)
]
_string_input = [('indexing', 'xy')]

_bools_input = [
    ('endpoint', True),
        ('retstep', False),
        ('sparse',False),
        ('copy',True),
         ('run',True)
]

_points_input = [
    ('points', list)
]

_array_input = [('in_array')]
_array_out = [('out_np_array')]

prms_hs, prms_hs_list, num_out = [], [], []
_prms_py = list(chain(_ints_input, _floats_input, _bools_input, _string_input, _points_input))


for i in _ints_input:
    prms_hs.append((i[0], hs.HopsInteger(i[0], i[0], i[0], default=i[1])))
    prms_hs_list.append((i[0], hs.HopsInteger(i[0], i[0], i[0], default=i[1], access=hs.HopsParamAccess.LIST)))

for i in _floats_input:
    prms_hs.append((i[0], hs.HopsNumber(i[0], i[0], i[0], default=i[1])))
    prms_hs_list.append((i[0], hs.HopsNumber(i[0], i[0], i[0], default=i[1], access=hs.HopsParamAccess.LIST)))
for i in _bools_input:
    prms_hs.append((i[0], hs.HopsBoolean(i[0], i[0], i[0], default=i[1])))
    prms_hs_list.append((i[0], hs.HopsBoolean(i[0], i[0], i[0], default=i[1], access=hs.HopsParamAccess.LIST)))
for i in _string_input:
    prms_hs.append((i[0], hs.HopsString(i[0], i[0], i[0], default=i[1])))
    prms_hs_list.append((i[0], hs.HopsString(i[0], i[0], i[0], default=i[1], access=hs.HopsParamAccess.LIST)))

prms_hs.append(('points', hs.HopsPoint('pts', 'pts', 'pts', access=hs.HopsParamAccess.LIST)))


for i in _array_out:
    num_out.append(hs.HopsNumber(i[0], i[0], i[0], access=hs.HopsParamAccess.LIST, optional=True))

points_out = [hs.HopsPoint('a_pt_out', 'a_pt_out', 'a_pt_out', access=hs.HopsParamAccess.LIST, optional=True),
              hs.HopsPoint('b_pt_out', 'b_pt_out', 'b_pt_out', access=hs.HopsParamAccess.LIST, optional=True)]

_int_out = [hs.HopsInteger("integer_val", "r", "r to r", hs.HopsParamAccess.ITEM)]

_prms_py = dict(_prms_py)

