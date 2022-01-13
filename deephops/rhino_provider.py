import numpy as np
import rhino3dm


def _get_points_2d(points):
    to_np = []


    for point in points:

        to_np.append([point.X, point.Y])

    np_pointlist = np.array(to_np)
    return np_pointlist

def _get_points_3d(points):
    to_np = []

    for point in points:

        to_np.append([point.X, point.Y, point.Z])

    np_pointlist = np.array(to_np)
    return np_pointlist

def _set_points_2d(np_pointlist: np.ndarray):
    args = np_pointlist
    points = []
    for arg in args:
        x_new = arg[0]
        y_new = arg[1]
        points.append(rhino3dm.Point3d(x_new, y_new, 0))
    return points


def _set_points_3d(np_pointlist: np.ndarray):
    args = np_pointlist
    points = []
    for arg in args:
        x_new = arg[0]
        y_new = arg[1]
        z_new = arg[2]
        points.append(rhino3dm.Point3d(x_new, y_new, z_new))
    return points
