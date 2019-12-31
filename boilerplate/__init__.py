# -*- coding: utf-8 -*-
from __future__ import absolute_import

from pkg_resources import get_distribution

from boilerplate.api import print_string, login
from boilerplate.scripts import cli

__version__ = get_distribution('boilerplate').version

__all__ = [
    'print_string',
    'login',
]
