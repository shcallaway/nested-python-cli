import click


@click.group()
def ecr():
    pass


@ecr.command()
def push():
    """Push an image to ECR."""
    print("Pushing!")


@ecr.command()
def pull():
    """Pull an image from ECR."""
    print("Pulling!")
