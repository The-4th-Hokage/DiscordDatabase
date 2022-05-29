__title__ = 'DiscordDatabase'
__author__ = 'Dhruva Shaw'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present Dhruvacube'
__version__ = '0.1.4'
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from typing import NamedTuple, Literal
import logging

from .DiscordDatabase import DiscordDatabase

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=1, micro=4, releaselevel='final', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

del logging, NamedTuple, Literal, VersionInfo