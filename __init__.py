'''

'''
if True:
    from ._py import *
    to_exclude = ['Config', 'Global']
    for name in to_exclude:
        del globals()[name]
else:
    # import from _pyx
    pass

from .Parser.parser import parser, parse
