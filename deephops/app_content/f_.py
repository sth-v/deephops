import ghhops_server as hs



instances = []


def cls_count(cls):
    def wrap(*args: object, **kwargs: object) -> object:
        obj = cls(*args, **kwargs)
        instances.append(obj)
        return obj
    return wrap


@cls_count
class Function:

    _description = 'foo instance'
    _category = 'foo'
    _subcategory = 'foo'

    _INPUTS = [

        hs.HopsBoolean(*[
            'run',
            'run',
            'default test input,'
            ' default=True,'
            ' if want enable this hops, set False',
            hs.HopsParamAccess.ITEM,
            False,
            True])]

    _OUTPUTS = [

        hs.HopsString(*[
            'out',
            'out',
            'output field for text data, errors and other messages, and python console',
            hs.HopsParamAccess.LIST,
            False,
            'no output'])
    ]


    def __new__(cls, func, name, description = _description, category = _category, subcategory=_subcategory, inputs=_INPUTS, outputs=_OUTPUTS):
        instance = super().__new__(cls)
        print(f'new class instance: {func} | {name} | {description}')
        return instance

    def __init__(self, func, name, description = _description, category = _category, subcategory=_subcategory, inputs=_INPUTS, outputs=_OUTPUTS):
        self.f = func
        self.name = name
        self.nickname = name
        self.description = description
        self.category = category
        self.subcategory = subcategory
        self.rule = '/' + self.name
        self.names = self.__dict__.keys()
        self.input = [*self._INPUTS] if inputs == self._INPUTS else [*self._INPUTS, *inputs]
        self.output = [*self._OUTPUTS] if outputs == self._OUTPUTS else [*self._OUTPUTS, *outputs]

    def __setattr__(self, attr, value):
        if attr:
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')

    def __str__(self):
        return f' function {self.name}'


def f_foo_deephops():
    return 'Huge thanks to Andrew for this tool'


def f_help():
    rulist = []
    for i in instances:
        rulist.append(i.rule)
    return rulist


foo_deephops = Function(func=f_foo_deephops,
                        name='f_foo_deephops')


help_deephops = Function(func=f_help,
                         name='help',
                         description='f_help',
                         category='base',
                         subcategory='support'
                         )

'''
geometry pointlist
'''

'''
@rh_generator
def f_random_rhino_point():
    return rhino3dm.Point3d(random(), random(), 0)


def f_min_bound_rectangle(run, *args):
    if run:
        return print(*args), min_bound_rect(*args)


def f_polygon_read(run, *args):
    if run:
        return print(*args), poly_read(*args)


def f_tor_uv(run, *args):
    if run:
        return func_shape_tor(*args)


def f_meb_uv(run, *args):
    if run:
        return func_shape_mebius(*args)'''

'''
_geo_pl_category = 'geometry'
_geo_pl_subcategory = 'pointlist'
_param_pointlist = hs.HopsPoint("pointlist", "ptlist", "pointlist", hs.HopsParamAccess.LIST, optional=False, default=f_random_rhino_point(6))
_param_pointlist_out = hs.HopsPoint("pointlist", "ptlist", "pointlist", hs.HopsParamAccess.LIST)
_param_curvelist = hs.HopsCurve("C", "C", "C", hs.HopsParamAccess.LIST),
_param_p = hs.HopsInteger("parameter", "p", "p to fl", hs.HopsParamAccess.ITEM, default=1)
_param_range = hs.HopsInteger("steps", "steps", "steps", hs.HopsParamAccess.ITEM, default=12)

_geo_surf_category = 'geometry'
_geo_surf_subcategory = 'func_surface'
'''
'''
min_bound_rectangle = Function(func=f_min_bound_rectangle,
                         name='f_polygon_read',
                         description='read some n-gon for master plane site',
                         category= _geo_pl_subcategory,
                         subcategory= _geo_pl_subcategory,
                         inputs=[_param_pointlist, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])


polygon_read = Function(func=f_polygon_read,
                         name='f_polygon_read',
                         description='read some n-gon for master plane site',
                         category= _geo_pl_subcategory,
                         subcategory= _geo_pl_subcategory,
                         inputs=[_param_pointlist, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])


tor_uv = Function(func=f_tor_uv,
                         name='f_tor_uv',
                         description='tor_uv',
                         category= _geo_surf_category,
                         subcategory= _geo_surf_subcategory,
                         inputs=[_param_range, _param_p ],
                         outputs= [_param_curvelist, _param_curvelist])




meb_uv = Function(func=f_meb_uv,
                     name='f_meb_uv',
                     description='meb_uv',
                     category=_geo_surf_category,
                     subcategory=_geo_surf_subcategory,
                     inputs=[_param_range, _param_p],
                     outputs=[_param_curvelist, _param_curvelist])'''
