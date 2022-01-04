from flask import Flask
import numpy as np
import rhino3dm
import ghhops_server as hs
from deephops.func_layers import FL_PolygonRead, dec_tor_shp
from deephops.rhino_helpers import InputRhinoHelper, OutputRhinoHelper, get_point_list, rh_generator
from deephops.tensor_base import Tensor
from deephops.app_content.f_ import foo_deephops, help_deephops
from random import random

# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)


@app.route("/help")
def help():
    return "Huge thanks to Andrew for this tool"


@hops.component(
    foo_deephops.rule,
    name=foo_deephops.name,
    nickname=foo_deephops.nickname,
    description=foo_deephops.description,
    inputs=foo_deephops.input,
    outputs=foo_deephops.output
)
def foo(run=True):
    if run:
        return foo_deephops.f()

@hops.component(
    help_deephops.rule,
    name=help_deephops.name,
    nickname=help_deephops.nickname,
    description=help_deephops.description,
    inputs=help_deephops.input,
    outputs=help_deephops.output
)
def help_dh(run=True):
    if run:
        print('help run')
        res = help_deephops.f()

        res.append('/funcshape')
        res.append('/getnparray')
        res.append('/polygonread')
        return res
    else:
        return 'enabled'


@hops.component(
    '/polygonread',
    name='Polygon Read',
    nickname='pr',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsPoint("Master plan n-gon points", "MN", "Geometry to computation model", hs.HopsParamAccess.LIST),
        hs.HopsInteger("parameter", "p", "p to fl", hs.HopsParamAccess.ITEM, default=1),
    ],
    outputs=[
        hs.HopsCurve("A", "A", "A", hs.HopsParamAccess.LIST),
        hs.HopsCurve("B", "B", "B", hs.HopsParamAccess.LIST)
    ]
)
def polygon_read(in_points, in_p ):
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
    '/getnparray',
    name='getnparray',
    nickname='pr',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsBoolean("run", "run", "run", hs.HopsParamAccess.ITEM, default=True),

    ],
    outputs=[
        hs.HopsString("out", "out", "out", hs.HopsParamAccess.LIST, default='some problem'),
        hs.HopsPoint("A", "A", "A", hs.HopsParamAccess.LIST)

    ]
)
def some(run = True):
    print('get array run')
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

        return np.ndarray.tolist(o), pts


@hops.component(
    '/funcshape',
    name='funcshape',
    nickname='fs',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsBoolean("run", "run", "run", hs.HopsParamAccess.ITEM, default=True),
        hs.HopsInteger("steps", "steps", "steps", hs.HopsParamAccess.ITEM, default=12),
        hs.HopsInteger("p", "p", "p", hs.HopsParamAccess.ITEM, default=3)

    ],
    outputs=[
        hs.HopsString("out", "out", "out", hs.HopsParamAccess.LIST, default='some problem'),
        hs.HopsPoint("pt", "pt", "pt", hs.HopsParamAccess.LIST)


    ]
)
def func_shape(run = True , steps = 12, p = 3):
    if run:
        print('tor run')
        result = dec_tor_shp(steps, p)
        print(result, np.array(result).shape)
        pts = get_point_list(result)
    else:
        print('problem')

    return np.ndarray.tolist(result), pts


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    app.run()

