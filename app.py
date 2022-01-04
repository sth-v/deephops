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

@hops.component(
    foo_deephops.rule,
    name=foo_deephops.name,
    nickname=foo_deephops.nickname,
    description=foo_deephops.description,
    inputs=foo_deephops.input,
    outputs=foo_deephops.output
)
def foo_dh(run=True):
    if run:
        print('foo run')
        return foo_deephops.f()
    else:
        return 'enabled'






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hops.start(debug=True)

