#!/usr/local/bin/python3

import click

from aws import aws
from k8s import k8s


@click.group()
def foo():
    pass


@foo.command()
def version():
    """Display the current version."""
    click.echo(_read_version())


foo.add_command(aws.aws)
foo.add_command(k8s.k8s)
