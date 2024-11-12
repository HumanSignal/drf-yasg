# coding=utf-8

__author__ = """Cristi V."""
__email__ = 'cristi@cvjd.me'

HS_PREFIX = 'humansignal_'

try:
    from importlib.metadata import version
    __version__ = version(HS_PREFIX + __name__)
except ImportError:  # Python < 3.8
    try:
        from pkg_resources import DistributionNotFound, get_distribution
        __version__ = get_distribution(HS_PREFIX + __name__).version
    except DistributionNotFound:  # pragma: no cover
        # package is not installed
        pass
