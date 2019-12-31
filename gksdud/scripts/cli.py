# -*- coding: utf-8 -*-

"""
This file Implements Command Line Interface

"""

from __future__ import absolute_import
import click

import gksdud


@click.group()
def main():
    pass


@click.command()
@click.option("--string", default='Hello World')
def cli_kor2eng(string):
    """
    Example Usage

        >>> gksdud cli_kor2eng --string="한영"

    :return:
    """
    res = gksdud.kor2eng(string)
    click.echo(res)


@click.command()
@click.option("--string", default='Hello World')
def cli_eng2kor(string):
    """
    Example Usage

        >>> gksdud cli_eng2kor --string="dudgks"

    :param string:
    :return:
    """
    res = gksdud.eng2kor(string)
    click.echo(res)


main.add_command(cli_kor2eng)
main.add_command(cli_eng2kor)
