import inspect
import itertools
import deephops.cpfuncs as _dh_geo
import deephops.npfuncs as _dh_np
import deephops.default as _dh_default
import ghhops_server as hs
import operator as op


__prms_in = dict(_dh_default.prms_hs)
__points_out_a = _dh_default.points_out[0]
__points_out_b = _dh_default.points_out[1]
_param_p = hs.HopsInteger("p", "p", "p to fl", hs.HopsParamAccess.ITEM, default=1)
_param_a = hs.HopsInteger("a", "a", "a to a", hs.HopsParamAccess.ITEM, default=2)
_result_r = hs.HopsInteger("integer_val", "r", "r to r", hs.HopsParamAccess.ITEM)
instances = []


def foo(run):
    if run:
        return 'Huge thanks to Andrew for this tool'


def help(run):
    if run:
        rulist = []
        for i in instances:
            rulist.append(i.rule)
        return rulist


def cls_count(cls):
    def wrap(*args: object, **kwargs: object) -> object:
        obj = cls(*args, **kwargs)
        instances.append(obj)
        return obj
    return wrap


def add(run, a, b):
    if run:
        return f'{a} + {b}', op.add(a, b)


@cls_count
class Function:

    _description = 'foo instance'
    _category = 'deephops'
    _subcategory = 'example'

    _OUTPUTS = [

        hs.HopsString(
            'out',
            'out',
            'output field for text data, errors and other messages, and python console',
            hs.HopsParamAccess.LIST,
            False,
            'no output')
    ]

    def __new__(cls, _comp_func, name=None, description=_description, category=_category, subcategory=_subcategory, inputs=[], outputs=[]):
        instance = super().__new__(cls)
        print(f'new class instance:{_comp_func} | {_comp_func.__qualname__ if name is None else name} | {description}')
        return instance

    def __init__(self, _comp_func, name=None, description=_description, category=_category, subcategory=_subcategory, inputs=[], outputs=[]):
        self._comp_func = _comp_func
        self.name = self._comp_func.__qualname__ if name is None else name
        self.nickname = self.name
        self.description = description
        self.category = category
        self.subcategory = subcategory
        self.rule = f'/{self.name}'
        self.inputs = inputs
        self.outputs = list(itertools.chain(self._OUTPUTS, outputs))

    def _no_func_dict(self):
        return itertools.islice(self.__dict__.items(), 1, None)

    def __setattr__(self, attr, value):
        if attr:
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')

    def __str__(self):
        return f' function {self.name}'


Function(_comp_func=foo,
         name='foo',
         inputs=[_dh_default._INPUTS_DEF['run']]
         )

Function(_comp_func=help,
         description='help',
         inputs=[_dh_default._INPUTS_DEF['run']]
         )

Function(
    _comp_func=add,
    description='add',
    inputs = [_dh_default._INPUTS_DEF['run'], _param_p, _param_a],
    outputs=[_result_r]
)

dh_func = dict(inspect.getmembers(_dh_np, inspect.isfunction))

for i in _dh_np.__privat__:
    dh_func.__delitem__(i)

dw = dict(_dh_np.kwd)
dhk = list(dh_func.keys())
dhf = list(dh_func.values())
print(dh_func)

for i in dhk:

    j = dw[i]
    print(dw[i])

    Function(_comp_func=dh_func[i], name=i, description='numpy creator', inputs=j, outputs=_dh_np.num_out)


#create func



Function(
    _comp_func=_dh_geo.base_min_bound_rect,
    name='base_min_bound_rect',
    description='base_min_bound_rect',
    inputs =[__prms_in['points'], __prms_in['run']],
    outputs=[__points_out_a]
)

Function(
    _comp_func=_dh_geo.base_convexhull,
    name='base_convexhull',
    description='base_convexhull',
    inputs =[__prms_in['points'], __prms_in['run']],
    outputs=[__points_out_a]
)

Function(
    _comp_func=_dh_geo.base_primitive_toroid,
    name ='base_primitive_toroid',
    description='primitive',
    inputs=[__prms_in['u'], __prms_in['v'], __prms_in['u_count'], __prms_in['v_count'],  __prms_in['run']],
    outputs=[__points_out_a, __points_out_b]
)