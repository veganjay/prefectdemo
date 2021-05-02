%title: Introduction to Prefect
%author: Jason Youzwak
%date: 2021-05-27

## About me

My Prefect background

* Prefect newbie: Started using Prefect ~ November 2020
* Not affiliated with Prefect whatsover

Things I like:

* *Python*: programmer for ~10 years
^
* *Linux*: desktop, server, pi
^
* *Plant-based diet*
^
* *Boardgames* (hit me up: veganjay on boardgamearena.com)
^
* *Zachtronics* and similar programming games

-----------------------------------------------------------------------

## What is Prefect?

Prefect is a dataflow automation tool:

* Python functions become Prefect tasks
^
* Flows define recipes that run tasks
^
* Prefect determines dependencies between tasks
^
* Tasks run on agents, which can run be distributed
^


*Think "Containers for Computation"*

-----------------------------------------------------------------------

## Environment Set-up

Prefect is available via pip.  I recommend installing in a virtual environment:

    $ mkdir -p $HOME/.venv
    $ python3.9 -m venv $HOME/.venv/prefect
    $ source $HOME/.venv/prefect/bin/activate
    $ pip install prefect

-----------------------------------------------------------------------

## Hello, World!

An example task and flow is shown in ./hello/__main__.py

The Prefect flow can be run locally without a Prefect Server:

    $ python3 -m hello

The output shows the Prefect log and output from the task:

    INFO - prefect.FlowRunner | Beginning Flow run for 'My First Flow'
    INFO - prefect.TaskRunner | Task 'name': Starting task run...
    INFO - prefect.TaskRunner | Task 'name': Finished task run for task with final state: 'Success'
    INFO - prefect.TaskRunner | Task 'say_hello': Starting task run...
    INFO - prefect.TaskRunner | Hello, World!
    INFO - prefect.TaskRunner | Task 'say_hello': Finished task run for task with final state: 'Success'
    INFO - prefect.FlowRunner | Flow run SUCCESS: all reference tasks succeeded

-----------------------------------------------------------------------

## Why use Prefect?

Use it for simple to complex data flows that:

- Parse data
- Perform "number crunching"
- Store data

Good candidate is ETL (Extract, Transform, Load) jobs.

The Prefect core engine provides:

- Dependency resolution between tasks
- Scheduling
- Data caching
- Error handling
- Workflow state

-----------------------------------------------------------------------

## Prefect Server

Prefect really shines when running the Prefect server.

Start prefect server:

    $ prefect backend server
    $ prefect server start

Start prefect agent:

    $ prefect agent local start

The prefect server can be accessed at http://localhost:8080

-----------------------------------------------------------------------

## Registering Flows

Create the prefect project:

    $ prefect create project demo

Register the flow:

    $ python -m hello.register

## Running Flows

The flow can be run via the Prefect server:

- Navigate to http://localhost:8080
- Choose "Flows" -> "Hello Flow"
- Choose "Run" tab, enter name parameter, and click run
- Choose "Logs" to see results.

The flow can also be run via command line:

    $ prefect run flow --name "Hello Flow" --project demo -ps '{"name": "Command Line"}'

-----------------------------------------------------------------------


## Maths

Tasks are defined for mathematical functions in maths/tasks.py:

* add
* multiply
* subtract
* divide
* sqrt

Flows are defined using the tasks in maths/flows.py:

* add: x = a + b
* formula1: x = (a + b) * c
* formula2: x = (a * c) + (b * c)
^
* quadratic equation:

^
> x = (-b +/- (b^2 - 4ac)) / 2a

-----------------------------------------------------------------------

## Running Maths flows

Run the flows from command line:

    $ prefect run flow --name "Add" --project demo -ps '{"num1": 12, "num2": 52}'
    $ prefect run flow --name "Formula1" --project demo -ps '{"a": 3, "b": 4, "c": 5}'
    $ prefect run flow --name "Formula2" --project demo -ps '{"a": 3, "b": 4, "c": 5}'
    $ prefect run flow --name "QuadraticFormula" --project demo -ps '{"a": 1, "b": 0, "c": -9}'

-----------------------------------------------------------------------

## Example ETL: Retrieving Historical Weather

The module *nyc/weather.py* contains the following functions:

- *get_weather*: extract historical weather using meteostat library
- *parse_weather*: transform the data obtaining relevant fields and converting to fahrenheit
- *store_weather*: store the data in sqlite3 database

The resulting sqlite database:

    $ sqlite3 weather.db 
    sqlite> .headers on
    sqlite> .mode column
    sqlite> select * from weather limit 5;
    timestamp   average_temp  precipitation
    ----------  ------------  -------------
    2018-01-01  13.1          0            
    2018-01-02  18.86         0            
    2018-01-03  21.02         0            
    2018-01-04  25.34         18           
    2018-01-05  15.08         0  

-----------------------------------------------------------------------

## That's it, for now...

That just scratches the surface.  Advanced topics include:

- Deploying to DASK Cluster
- Scheduling
- Error handlers
- State handlers
- Built-in Prefect tasks
- Mappings

Thank you!  @veganjay
