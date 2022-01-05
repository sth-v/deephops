import operator


def add(run, a, b):
    if run:
        return f'{a} + {b}', operator.add(a, b)


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
