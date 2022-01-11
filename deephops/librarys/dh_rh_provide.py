import numpy as np
import rhino3dm


def _get_points(points):
    to_np = []


    for point in points:

        to_np.append([point.X, point.Y])

    print(to_np)
    np_pointlist = np.array(to_np)
    return np_pointlist


def _set_points(np_pointlist: np.ndarray):
    args = np_pointlist
    points = []
    for arg in args:
        x_new = arg[0]
        y_new = arg[1]
        points.append(rhino3dm.Point3d(x_new, y_new, 0))
    return points
