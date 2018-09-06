import click


@click.group()
def ecs():
    pass


@ecs.command()
def deploy():
    """Deploy something to ECS."""
    print("Deploying!")
