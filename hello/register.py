"""This module creates and registers a flow with the Prefect server.
"""
from prefect import Flow, Parameter

from hello.__main__ import say_hello


def main():
    """Create a simple flow that accepts a name as the parameter and
    runs the 'Hello World' task to say the name.
    """
    with Flow("Hello Flow") as flow:
        name = Parameter("name")
        say_hello(name)

    flow.register(project_name='demo')


if __name__ == '__main__':
    main()
