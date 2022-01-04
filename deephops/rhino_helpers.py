import numpy as np
import rhino3dm
from deephops.func_layers import FuncLayer


def save_array(data, func_layer: FuncLayer):
    """

    :param data:
    :param func_layer:
    :return:
    """
    mess = np.save(func_layer.name, data)
    if mess:
        return True
    else:
        return False


class InputRhinoHelper:

    def __init__(self, rhino_geometry):
        self.geometry = rhino_geometry

    def get_points(self, mask: list[str], func_layer: FuncLayer, save=True) -> np.array:
        """

        :param mask:
        :param func_layer:
        :param save:
        :return:
        """
        in_points = self.geometry
        to_np_old = []
        to_np = []

        for point in in_points:
            mask_dict = {'X': point.X, 'Y': point.Y, 'Z': point.Z}
            to_np.append(list(map((lambda x: mask_dict.pop(x)), mask)))

        print(to_np)
        array = np.array(to_np)

        if save:
            save_array(array, func_layer)

        return array


def get_point_list(pointlist):
    args = pointlist
    rhino_pointlist = []
    for arg in args:
        x_new = arg[0]
        y_new = arg[1]
        z_new = arg[2]
        rhino_pointlist.append(rhino3dm.Point3d(x_new, y_new, z_new))
    return rhino_pointlist


class OutputRhinoHelper:
    def __init__(self, array: iter):
        self.ndarray = array

    def get_rectangle(self, yield_index: int):
        """

        :return: rhino_rectangles -> list[rhino3dm.PolylineCurve]:
        """

        args = self.ndarray[yield_index]
        rhino_rectangles = []

        for arg in args:
            x_new = arg[:, 0]
            y_new = arg[:, 1]
            point_a = rhino3dm.Point3d(x_new[0], y_new[0], 0)
            point_b = rhino3dm.Point3d(x_new[1], y_new[1], 0)
            point_c = rhino3dm.Point3d(x_new[2], y_new[2], 0)
            point_d = rhino3dm.Point3d(x_new[3], y_new[3], 0)
            crv = rhino3dm.PolylineCurve.CreateControlPointCurve([point_a, point_b, point_c, point_d], 1)
            rhino_rectangles.append(crv)

        return rhino_rectangles

    def get_clusters_curves(self, yield_index: int):

        args = self.ndarray[yield_index]
        rhino_curves = []
        for arg in args:
            x_new = arg[:, 0]
            y_new = arg[:, 1]
            points = list(map((lambda x, y: rhino3dm.Point3d(x, y, 0)), x_new, y_new))
            crv = rhino3dm.PolylineCurve.CreateControlPointCurve(points, 1)
            rhino_curves.append(crv)

        return rhino_curves



def rh_generator(func):

    def generic_wrapper(func):
        yield func

    def wrap(count):
        result = []
        for c in range(count):
            result.extend(generic_wrapper(func()))
        return result
    return wrap







