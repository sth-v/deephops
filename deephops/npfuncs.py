import inspect
import numpy as np
import sys
from deephops.default import _ints_input, _floats_input, _string_input, _bools_input, _array_input, _array_out, _prms_py, prms_hs, num_out

np.set_printoptions(threshold=sys.maxsize)

__privat__= ['_np_decoration']
__description__ = 'numpy'

kwd = []

print(_prms_py)


def _np_decoration(func):
    kwdict = list(inspect.getcallargs(func))
    local_args =[]
    py_args = []
    for i in kwdict:
        local_args.append(dict(prms_hs)[i])
    kwd.append((func.__qualname__, local_args))


def np_arange(run = _prms_py['run'], start=_prms_py['start'], stop=_prms_py['stop'], step=_prms_py['step']):
    if run:
        n = np.arange(start, stop, step)
        print(n)
        return f'{print(n)}', n.tolist()
    else:
        return [0]


def np_linspace(run = _prms_py['run'], start=_prms_py['start'], stop=_prms_py['stop'], num=_prms_py['num'], endpoint=_prms_py['endpoint'], retstep=_prms_py['retstep']):
    if run:
        n = np.linspace(start, stop, num, endpoint, retstep)
        return f'{print(n)}', n.tolist()
    else:
        return  [0]


def np_logspace(run = _prms_py['run'], start=_prms_py['start'], stop=_prms_py['stop'], num=_prms_py['num'], endpoint=_prms_py['endpoint'], base=_prms_py['base']):
    if run:
        n = np.logspace(start, stop, num, endpoint, base)
        return f'{print(n)}', n.tolist()
    else:
        return [0]


_np_decoration(np_arange)
_np_decoration(np_linspace)
_np_decoration(np_logspace)
