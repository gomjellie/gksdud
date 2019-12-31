# -*- coding: utf-8 -*-

from __future__ import absolute_import
import click

import boilerplate


@click.group()
def main():
    pass


@click.command()
@click.option("--string", default='Hello World')
def single_print(string):
    """
    Example Usage

        >>> boiler single_print --string="hi there~"

    :return:
    """
    boilerplate.print_string(string)


@click.command()
@click.option("--string", "-s", default='Hello World', type=str, multiple=True)
def multiple_print(string):
    """
    Example Usage

        >>> boiler multiple_print --string="hello" --string="world"

        >>> boiler multi_print --string="hello" -sworld

    :param string:
    :return:
    """
    boilerplate.print_string(" ".join(string))


@click.command()
@click.option("--id", type=str, multiple=False)
@click.option("--password", type=str, multiple=False)
def login(id, password):
    """
    Example Usage

        >>> boiler login --id='adam' --password='smith'

    :param id:
    :param password:
    :return:
    """
    res = boilerplate.login(id, password)
    click.echo("{}".format(res))


main.add_command(single_print)
main.add_command(multiple_print)
main.add_command(login)
