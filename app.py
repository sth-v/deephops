import numpy as np
import rhino3dm
import ghhops_server as hs
from deephops.func_layers import FL_PolygonRead, dec_tor_shp
from deephops.rhino_helpers import InputRhinoHelper, OutputRhinoHelper, get_point_list, rh_generator
from deephops.tensor_base import Tensor
from deephops.app_content.f_ import foo_deephops, help_deephops
from random import random

hops = hs.Hops()






@rh_generator
def random_rhino_point():
    return rhino3dm.Point3d(random()*10, random()*10, 0)

default_pt=random_rhino_point(6)
print(default_pt)
@hops.component(
    foo_deephops.rule,
    name=foo_deephops.name,
    nickname=foo_deephops.nickname,
    description=foo_deephops.description,
    inputs=foo_deephops.input,
    outputs=foo_deephops.output
)
def foo_dh(run: bool):
    if run:
        return foo_deephops.f()
    else:
        return 'enabled'


@hops.component(
    help_deephops.rule,
    name=help_deephops.name,
    nickname=help_deephops.nickname,
    description=help_deephops.description,
    inputs=help_deephops.input,
    outputs=help_deephops.output
)
def help_dh(run: bool):
    if run:
        res = help_deephops.f()

        res.append('/func_shape')
        res.append('/get_np_array')
        return res
    else:
        return 'enabled'





@hops.component(
    '/get_np_array',
    name='get_np_array',
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

        return np.ndarray.tolist(o), pts


@hops.component(
    '/func_shape',
    name='func_shape',
    nickname='fs',
    description='read some n-gon for master plane site',
    inputs=[
        hs.HopsInteger("steps", "steps", "steps", hs.HopsParamAccess.ITEM, default=12),
        hs.HopsInteger("p", "p", "p", hs.HopsParamAccess.ITEM, default=3)

    ],
    outputs=[
        hs.HopsString("out", "out", "out", hs.HopsParamAccess.LIST, default='some problem'),
        hs.HopsPoint("pt", "pt", "pt", hs.HopsParamAccess.LIST)


    ]
)
def func_shape(steps, p):
    result = dec_tor_shp(steps, p)
    print(result, np.array(result).shape)
    pts = get_point_list(result)

    return np.ndarray.tolist(result), pts



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hops.start(debug=True)

