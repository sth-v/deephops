import operator as op
import inspect
from itertools import *
import numpy as np
import ghhops_server as hs
import sys
from deephops.librarys.default import ints, floats, string, bools, in_array, out_array, prms_py, prms_hs, outp

np.set_printoptions(threshold=sys.maxsize)

__privat__= ['_np_decoration']
__description__ = 'npumpy'

kwd = []

print(prms_py)


def _np_decoration(func):
    kwdict = list(inspect.getcallargs(func))
    local_args =[]
    py_args = []
    for i in kwdict:
        local_args.append(dict(prms_hs)[i])
    kwd.append((func.__qualname__, local_args))


def np_arange(run = prms_py['run'], start=prms_py['start'], stop=prms_py['stop'], step=prms_py['step']):
    if run:
        n = np.arange(start, stop, step)
        print(n)
        return f'{print(n)}', n.tolist()
    else:
        return [0]


def np_linspace(run = prms_py['run'], start=prms_py['start'], stop=prms_py['stop'], num=prms_py['num'], endpoint=prms_py['endpoint'], retstep=prms_py['retstep']):
    if run:
        n = np.linspace(start, stop, num, endpoint, retstep)
        return f'{print(n)}', n.tolist()
    else:
        return  [0]


def np_logspace(run = prms_py['run'], start=prms_py['start'], stop=prms_py['stop'], num=prms_py['num'], endpoint=prms_py['endpoint'], base=prms_py['base']):
    if run:
        n = np.logspace(start, stop, num, endpoint, base)
        return f'{print(n)}', n.tolist()
    else:
        return [0]


_np_decoration(np_arange)
_np_decoration(np_linspace)
_np_decoration(np_logspace)

print(kwd)
print(np_linspace())


""" 
def np_create(run, kwargs):
    l = []
    h = []
    for i in kwargs:
        l.append((i, prms_py[i]))
        h.append((i, prms_hs[i], prms_py[i], func))

    kw_dict=dict(l)

    def functor(func):
        if run:
            print(f'{func.__qualname__}({kwargs}) -> list(np.array)')
            return _to_list(func(**kw_dict))
        else:
            return[0]

    return ['y'], functor



['run', 'start', 'stop', 'num', 'endpoint', 'axis']

def geomspace(run, *args, **kwargs):
    if run:
        return np.geomspace(*args, **kwargs)
    else:
        return [0]


np_create()()

"""

'''
geometry pointlist
'''

'''
@rh_generator
def f_random_rhino_point():
    return rhino3dm.Point3d(random(), random(), 0)


def f_min_bound_rectangle(run, *args):
    if run:
        return print(*args), min_bound_rect(*args)


def f_polygon_read(run, *args):
    if run:
        return print(*args), poly_read(*args)


def f_tor_uv(run, *args):
    if run:
        return func_shape_tor(*args)


def f_meb_uv(run, *args):
    if run:
        return func_shape_mebius(*args)'''

'''
_geo_pl_category = 'geometry'
_geo_pl_subcategory = 'pointlist'
_param_pointlist = hs.HopsPoint("pointlist", "ptlist", "pointlist", hs.HopsParamAccess.LIST, optional=False, default=f_random_rhino_point(6))
_param_pointlist_out = hs.HopsPoint("pointlist", "ptlist", "pointlist", hs.HopsParamAccess.LIST)
_param_curvelist = hs.HopsCurve("C", "C", "C", hs.HopsParamAccess.LIST),
_param_p = hs.HopsInteger("parameter", "p", "p to fl", hs.HopsParamAccess.ITEM, default=1)
_param_range = hs.HopsInteger("steps", "steps", "steps", hs.HopsParamAccess.ITEM, default=12)

_geo_surf_category = 'geometry'
_geo_surf_subcategory = 'func_surface'
'''
'''
min_bound_rectangle = Function(func=f_min_bound_rectangle,
                         name='f_polygon_read',
                         description='read some n-gon for master plane site',
                         category= _geo_pl_subcategory,
                         subcategory= _geo_pl_subcategory,
                         inputs=[_param_pointlist, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])


polygon_read = Function(func=f_polygon_read,
                         name='f_polygon_read',
                         description='read some n-gon for master plane site',
                         category= _geo_pl_subcategory,
                         subcategory= _geo_pl_subcategory,
                         inputs=[_param_pointlist, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])


tor_uv = Function(func=f_tor_uv,
                         name='f_tor_uv',
                         description='tor_uv',
                         category= _geo_surf_category,
                         subcategory= _geo_surf_subcategory,
                         inputs=[_param_range, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])




meb_uv = Function(func=f_meb_uv,
                     name='f_meb_uv',
                     description='meb_uv',
                     category=_geo_surf_category,
                     subcategory=_geo_surf_subcategory,
                     inputs=[_param_range, _param_p],
                     outputs=[_param_curvelist, _param_curvelist])'''
