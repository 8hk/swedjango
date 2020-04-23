# """
# This file manages settings file selection
#
# For make local based settings, please use local_settings.py file
# """
#
try:
    from .local_settings import *
except ImportError:
    from .base_settings import *
