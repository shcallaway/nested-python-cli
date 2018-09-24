# Nested Python CLI

An example of how to build a nested command-line interface with Python. The inspiration for this project was the [AWS CLI](https://aws.amazon.com/cli).

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

What is it?

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
