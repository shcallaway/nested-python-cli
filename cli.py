#!/usr/local/bin/python3

import click

from aws import aws


@click.group()
def cli():
    pass


@cli.command()
def version():
    """Display the current version."""
    click.echo(_read_version())


cli.add_command(aws.aws)


if __name__ == '__main__':
    cli()
