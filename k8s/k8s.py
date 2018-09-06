import click


@click.group()
def k8s():
    pass


@k8s.command()
def deploy():
    """Deploy something to Kubernetes."""
    print("Deploying!")
