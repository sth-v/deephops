
import deephops.func_content as fc
import numpy as np
import math




# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.






class Func:
    def __init__(self, definition):
        self.f = definition


class FuncLayer(Func):
    def __init__(self, definition, layer_name: str) -> None:
        super().__init__(definition)
        self.name = layer_name

    def __f__(self, data, p):
        return self.f(data, p)


def f_polygon_read(data, p):
    fa = fc.p_kmeans(data, p)
    labels = fa.labels_
    fb = fc.get_clusters(data, labels)
    min_bound_rec_results = []
    for i in fb:
        min_bound_rec_results.append(fc.minimum_bounding_rectangle(i))
    return min_bound_rec_results, fb


FL_PolygonRead = FuncLayer(f_polygon_read, 'polygon_read')



class domain:

    def __init__(self, start=float, end=float):
        self.start = start
        self.end = end
        self.length = end - start

    def __str__(self):
        return f'Domain: {self.start} to {self.end}'

    def divide_float(self, parts):
        rng = []
        for i in parts:
            rng.append(self.length * i + self.start)
        return rng

    def divide_steps(self, steps):
        step = self.length / steps
        rng = []
        for i in range(steps):
            rng.append(self.start + (i * step))
        return rng

class Func_Shapes:
    def __init__(self):
        pass

    def shape_uv(steps, p, u_min, v_min, u_max, v_max):
        cos = math.cos
        sin = math.sin
        dmn_u = domain(u_min, u_max)
        dmn_v = domain(v_min, v_max)
        u = dmn_u.divide_steps(steps)
        v = dmn_v.divide_steps(steps)
        uv = []
        for i in u:
            for j in v:
                x=cos(i)*(cos(j)+ p)
                y=sin(i)*(cos(j)+ p)
                z=sin(j)
                uv.append([x, y, z])
        return np.array(uv)

    def toroid_shape(func):
        import math
        pi = math.pi

        def wrapper(*args, **kwargs):
            u_min, u_max = -pi, pi
            v_min, v_max = -pi, pi
            return_val = func(*args, u_min, v_min, u_max, v_max)
            return return_val

        return wrapper

    def mebius_shape(func):
        import math
        pi = math.pi

        def wrapper(*args, **kwargs):
            u_min, u_max = -pi, 3
            v_min, v_max = -1, 1
            return_val = func(*args, u_min, v_min, u_max, v_max)
            return return_val

        return wrapper

    def logoriphm_shape(func):
        import math
        pi = math.pi

        def wrapper(*args, **kwargs):
            u_min, u_max = -pi, 3
            pi
            v_min, v_max = -pi, pi
            return_val = func(*args, u_min, v_min, u_max, v_max)
            return return_val

        return wrapper


fsh = Func_Shapes
tor_shape = fsh.toroid_shape
uv = fsh.shape_uv

@tor_shape
def dec_tor_shp(steps, p, u_min, v_min, u_max, v_max):
    return uv(steps, p, u_min, v_min, u_max, v_max)