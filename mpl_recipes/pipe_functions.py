"""Imports all the functions in the pipe package with _p suffixes."""
from warnings import warn
try:
    # try to import pipe
    import pipe
except ImportError:
    warn('pipe package is not available')
else:
    # get a reference to the namespace of this module
    g = globals()
    # for each function in pipe
    for name in dir(pipe):
        if name.startswith('_') or name == 'Pipe':
            continue
        # make a local version with the _p suffix
        g[name + '_p'] = getattr(pipe, name)
    # also add some aliases
    aliases = {'where_p': 'filter_p',
               'take_p': 'head_p'}
    for k, v in aliases.items():
        try:
            g[v] = g[k]
        except KeyError:
            warn('Bad alias: %s->%s' % (k, v))
