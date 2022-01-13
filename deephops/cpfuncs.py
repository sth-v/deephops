from compython.geometry_base import *
from compython.consts import _TOR_PROPS, _pi
import math
import numpy as np
from scipy.spatial import ConvexHull
from deephops.rhino_provider import _get_points_2d, _set_points_2d, _get_points_3d, _set_points_3d
from deephops.default import _prms_py
import inspect
import itertools

__privat__ = ['_minimum_bounding_rectangle', '_base_decoration', '_get_points', '_set_points']
__description__ = 'compython'


_u_count, _v_count = 'u_count', 'v_count'


def base_convexhull(points, run = _prms_py['run']):
    if run:
        np_pointlist = _get_points_2d(points)

        hull = ConvexHull(np_pointlist)

        sortedpt = []
        for i in hull.vertices:
            sortedpt.append(points[i])

        return f'hull:{print(np_pointlist )}', sortedpt

    else:
        return [0]


def base_min_bound_rect(points, run = _prms_py['run']):

    if run:
        np_pointlist = _get_points_2d(points)

        rect = min_bound(np_pointlist)
        print(rect)
        pt_out = _set_points_2d(rect)
        print(pt_out)

        return f'rectangle:{print(rect)}', pt_out
    else:
        return [0]


def base_primitive_toroid(u=_prms_py['u'], v=_prms_py['v'], u_count=_prms_py[_u_count],v_count=_prms_py[_v_count], run: bool = True):
    if run:
        tr = ParamFunc(**_TOR_PROPS)

        at = tr.multiply_interpolate( u_count, v_count).array()
        rhpta = _set_points_3d(at)
        al = str(at.tolist())
        print(al)

        bt = tr.single_interpolate(u, v).array()
        rhptb = _set_points_3d(bt)
        bl = str(bt.tolist())
        print(bl)
        log = list(itertools.chain(al, bl))

        return log, rhpta, rhptb

    else:
        return 'None'


base_primitive_toroid()