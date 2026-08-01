from .error_helper_funcs import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("error_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["error_helper_funcs"]
