# Prefect cheat sheet

Setting up a prefect environment using venv and pip:

    mkdir -p $HOME/.venv
    python3.9 -m venv $HOME/.venv/prefect
    source $HOME/.venv/prefect/bin/activate
    pip install prefect

Start prefect server:

    prefect backend server
    prefect server start

Once up and running, Prefect server can be accessed at [http://localhost:8080](http://localhost:8080)

Start prefect agent:

    prefect agent local start

Create a prefect project:

    prefect create project <name>

Run a flow:

    prefect run flow --name <flowname> --project demo -ps <parameters>

