import click

from aws import ecr
from aws import ecs


@click.group()
def aws():
    pass


aws.add_command(ecr.ecr)
aws.add_command(ecs.ecs)
