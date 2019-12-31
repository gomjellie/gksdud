# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pkg_resources import get_distribution

from gksdud.api import kor2eng, eng2kor
from gksdud import utils
from gksdud.scripts import cli

__version__ = get_distribution('gksdud').version

__all__ = [
    'kor2eng',
    'eng2kor',
    'utils',
]
