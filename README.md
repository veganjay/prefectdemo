# README

This repository contains basic [Prefect](https://www.prefect.io/) examples and tutorial to learn.

The [presentation](presentation.md) can be viewed using *mdp*:

    $ mdp presentation.tpp

Also provided is a [Prefect cheatsheet](cheatsheat.md) show commonly used commands.

The examples require python3 and prefect installed using your manager of choice (conda, venv/pip).

## Prefect installation

To install prefect using venv/pip:

    $ python3 -m venv $HOME/.venv/prefect
    $ source $HOME/.venv/prefect/bin/activate
    $ pip install prefect

Conda install:

    $ conda create --name prefect python=3.9
    $ conda install prefect

## Running the examples

The examples can be run in standalone mode or by initiating through Prefect server.

### Hello World standalone

Run "Hello, World" standalone:

    $ python3 -m hello

### Running with Prefect server

Start Prefect server:

    prefect backend server
    prefect server start

Start a Prefect agent:

    prefect agent local start

Create a Prefect project:

    prefect create project demo

Register the "Hello, World" flow:

    python -m hello.register

Run the "Hello, World" flow:

    prefect run flow --name "Hello Flow" --project demo -ps '{ "name": "Prefect Server" }'

Navigate to your [Local Prefect Server](http://localhost:8080).

## Additional resources

- [Official Prefect Documentation](https://docs.prefect.io/): The Prefect project provides useful documentation and tutorials
- [Getting Started with Prefect - PyData Denver](https://www.youtube.com/watch?v=FETN0iivZps): An excellent video tutorial by Laura Lorenz
