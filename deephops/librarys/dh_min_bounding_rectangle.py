import numpy as np
import rhino3dm
from scipy.spatial import ConvexHull
from deephops.librarys.dh_rh_provide import _get_points, _set_points
from deephops.librarys.default import ints, floats, string, bools, prms_py, prms_hs, outppt
import inspect

__privat__ = ['_minimum_bounding_rectangle', '_base_decoration', '_get_points', '_set_points']
__description__ = 'base geometry'

def _minimum_bounding_rectangle(points):

    """
    Find the smallest bounding rectangle for a set of points.
    Returns a set of points representing the corners of the bounding box.

    :param points: a nx2 matrix of coordinates
    :rval: a nx2 matrix of coordinates
    """

    pi2 = np.pi / 2.

    # get the convex hull for the points
    hull_points = points[ConvexHull(points).vertices]

    # calculate edge angles
    edges = np.zeros((len(hull_points) - 1, 2))
    edges = hull_points[1:] - hull_points[:-1]

    angles = np.zeros((len(edges)))
    angles = np.arctan2(edges[:, 1], edges[:, 0])

    angles = np.abs(np.mod(angles, pi2))
    angles = np.unique(angles)

    # find rotation matrices
    # XXX both work
    rotations = np.vstack([
        np.cos(angles),
        np.cos(angles - pi2),
        np.cos(angles + pi2),
        np.cos(angles)]).T

    rotations = rotations.reshape((-1, 2, 2))

    # apply rotations to the hull
    rot_points = np.dot(rotations, hull_points.T)

    # find the bounding points
    min_x = np.nanmin(rot_points[:, 0], axis=1)
    max_x = np.nanmax(rot_points[:, 0], axis=1)
    min_y = np.nanmin(rot_points[:, 1], axis=1)
    max_y = np.nanmax(rot_points[:, 1], axis=1)

    # find the box with the best area
    areas = (max_x - min_x) * (max_y - min_y)
    best_idx = np.argmin(areas)

    # return the best box
    x1 = max_x[best_idx]
    x2 = min_x[best_idx]
    y1 = max_y[best_idx]
    y2 = min_y[best_idx]
    r = rotations[best_idx]

    rval = np.zeros((4, 2))
    rval[0] = np.dot([x1, y2], r)
    rval[1] = np.dot([x2, y2], r)
    rval[2] = np.dot([x2, y1], r)
    rval[3] = np.dot([x1, y1], r)

    return rval

kwda = []

def _base_decoration(func):
    kwdict = list(inspect.getcallargs(func))
    local_args =[]
    py_args = []
    for i in kwdict:
        local_args.append(dict(prms_hs)[i])
    kwda.append((func.__qualname__, local_args))

def base_convexhull(points, run = prms_py['run']):
    if run:
        np_pointlist = _get_points(points)

        hull = ConvexHull(np_pointlist)
        #pt_out = _set_points(hull.vertices)


        sortedpt = []
        for i in hull.vertices:
            sortedpt.append(points[i])


        return f'hull:{print(np_pointlist )}', sortedpt

    else:
        return [0]


def base_min_bound_rect(points, run = prms_py['run']):

    if run:
        np_pointlist = _get_points(points)

        rect = _minimum_bounding_rectangle(np_pointlist)
        print(rect)
        pt_out = _set_points(rect)
        print(pt_out)

        return f'rectangle:{print(rect)}', pt_out
    else:
        return [0]


#_base_decoration(base_convexhull)
