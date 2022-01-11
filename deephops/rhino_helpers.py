import numpy as np
import rhino3dm
from func_layers import FuncLayer


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







