import numpy as np
import rhino3dm
import ghhops_server as hs
from deephops.func_layers import FL_PolygonRead
from deephops.rhino_helpers import InputRhinoHelper, OutputRhinoHelper
from deephops.tensor_base import Tensor

# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


hops = hs.Hops()


@hops.component(
    '/polygon_read',
    name='Polygon Read',
    nickname='pr',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsPoint("Master plan n-gon points", "MN", "Geometry to computation model", hs.HopsParamAccess.LIST),
        hs.HopsInteger("parameter", "p", "p to fl", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsCurve("A", "A", "A", hs.HopsParamAccess.LIST),
        hs.HopsCurve("B", "B", "B", hs.HopsParamAccess.LIST)
    ]
)
def polygon_read(in_points, in_p):
    """

    :param in_points:
    :param in_p:
    :return:
    """

    in_helper = InputRhinoHelper(in_points)
    data = in_helper.get_points(['X', 'Y'], FL_PolygonRead, True)

    results = FL_PolygonRead.__f__(data, in_p)

    out_helper = OutputRhinoHelper(results)
    out_rectangles = out_helper.get_rectangle(0)
    out_cluster_curves = out_helper.get_clusters_curves(1)

    return out_rectangles, out_cluster_curves


@hops.component(
    '/get_np_array',
    name='get_np_array',
    nickname='pr',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsBoolean("RUN", "RUN", "RUN", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
        hs.HopsPoint("A", "A", "A", hs.HopsParamAccess.LIST)
    ]
)
def some(run: bool):
    if run:

        a = Tensor([[2, 1, 0],
                    [1, 2, 1],
                    [0, 1, 2],
                    [1, 2, 4]])

        b = Tensor([[2, 0, 0],
                    [1, 1, 2],
                    [2, 0, 0],
                    [4, 2, 2]])

        d = np.tensordot(a.array, b.array, axes=0)
        n = 3
        s = int(round(np.size(d) / n))
        o = np.reshape(d, (s, n))
        pts = []
        for i in range(s):
            pts.append(rhino3dm.Point3d(o[i,0], o[i,1], o[i,2]))

        return pts


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hops.start(debug=True)

