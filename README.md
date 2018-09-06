# Nested CLI

An example of how to build a nested command-line interface with Python. This project uses a nifty package called [Click](http://click.pocoo.org/5/).

## Installation

```
pip3 install -e .
```

See [this article](http://click.pocoo.org/5/setuptools/#testing-the-script) for more information.

## Usage

```
foo
```

## Bash Completion

Bash completion is extremely covenient:

```
$ foo
aws      k8s      version
$ foo aws ec
ecr  ecs
$ foo aws ecr pu
pull  push
```

You can enable it with the following command:

```
eval "$(_FOO_COMPLETE=source foo)"
```

See [this article](http://click.pocoo.org/5/bashcomplete/#activation) for more information.
