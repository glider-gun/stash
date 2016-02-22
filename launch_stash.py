# coding: utf-8
"""
Launch StaSh in a more flexible and reliable way.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
import sys

module_names = (
    'stash',
    'system.shcommon',
    'system.shstreams',
    'system.shscreens',
    'system.shterminal',
    'system.shui',
    'system.shio',
    'system.shiowrapper',
    'system.shparsers',
    'system.shruntime',
    'system.shthreads',
    'system.shuseractionproxy',
)

# Attempt to reload modules when startup, does not seem to work
if 'stash.stash' in sys.modules:
    for name in module_names:
        sys.modules.pop('stash.' + name)
from stash import stash

# noinspection PyProtectedMember
debug = (
    # stash._DEBUG_STREAM,
    # stash._DEBUG_RENDERER,
    # stash._DEBUG_MAIN_SCREEN,
    # stash._DEBUG_MINI_BUFFER,
    # stash._DEBUG_IO,
    # stash._DEBUG_UI,
    # stash._DEBUG_TERMINAL,
    # stash._DEBUG_TV_DELEGATE,
    # stash._DEBUG_RUNTIME,
    # stash._DEBUG_PARSER,
    # stash._DEBUG_EXPANDER,
    # stash._DEBUG_COMPLETER,
)

log_setting = {
    'level': 'INFO',
    'stdout': True,
}

_stash = stash.StaSh(debug=debug, log_setting=log_setting)

_stash.launch()