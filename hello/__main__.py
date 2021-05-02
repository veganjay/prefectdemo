"""Create a 'Hello, World' Prefect Task
This serves as a basic introduction to the world of Prefect tasks.
A function is declared a task by using the "task" decorator.
A task by itself cannot be run directly.
Rather a flow is created that includes one or more tasks, and
the flow is run.
"""
from prefect import task, Flow, Parameter


@task(log_stdout=True)
def say_hello(name: str):
    """Print the words Hello, {name}!
    This is designated as a Prefect task.
    The log_stdout flag is set to True to allow reading the output.
    Arguments:
        name (str): name to print
    """
    print(f'Hello, {name}!')


def main():
    """Create a flow that uses the 'say_hello' task and run it.
    This creates a Prefect flow and runs it a couple times with
    different inputs.
    """
    with Flow("My First Flow") as flow:
        name = Parameter('name')
        say_hello(name)

    flow.run(name='World')
    flow.run(name='NH Python Meetup Group')


if __name__ == '__main__':
    main()
