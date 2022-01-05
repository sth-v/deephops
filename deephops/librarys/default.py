import ghhops_server as hs



_INPUTS_DEF = {'run': hs.HopsBoolean(
        'run',
        'run',
        'default test input,'
        ' default=True,'
        ' if want enable this hops, set False',
        hs.HopsParamAccess.ITEM,
        False,
        True)}

_OUTPUTS_DEF = {'strings': [
    ('out', hs.HopsString(
        'out',
        'out',
        'output field for text data, errors and other messages, and python console',
        hs.HopsParamAccess.LIST,
        False,
        'no output'))
]
}
