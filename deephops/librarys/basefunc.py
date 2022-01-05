import inspect
import itertools
import deephops.librarys.dh as dh
import ghhops_server as hs


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


@cls_count
class Function:

    _description = 'foo instance'
    _category = 'deephops'
    _subcategory = 'example'
    _INPUTS = [

        hs.HopsBoolean(
            'run',
            'run',
            'default test input,'
            ' default=True,'
            ' if want enable this hops, set False',
            hs.HopsParamAccess.ITEM,
            False,
            True)]
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
        print(f'new class instance:{_comp_func} | {_comp_func.__qualname__} | {description}')
        return instance

    def __init__(self, _comp_func, name=None, description=_description, category=_category, subcategory=_subcategory, inputs=[], outputs=[]):
        self._comp_func = _comp_func
        self.name = self._comp_func.__qualname__ if name is None else name
        self.nickname = self.name
        self.description = description
        self.category = category
        self.subcategory = subcategory
        self.rule = f'/{self.name}'
        self.inputs = list(itertools.chain(self._INPUTS, inputs))
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



Function(_comp_func=foo,name='foo')

Function(_comp_func=help,description='help')

Function(_comp_func=dh.add,description='add',inputs = [_param_p, _param_a],outputs=[_result_r])

for i in instances:
    print(i.name)



isfunction = inspect.isfunction
mem = inspect.getmembers(dh, isfunction)

