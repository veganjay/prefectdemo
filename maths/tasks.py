"""This module defines Prefect tasks for basic mathematical operations.
"""
import math

from prefect import task


@task(log_stdout=True)
def add(num1: float, num2: float) -> float:
    """Add two numbers"""
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
    return result


@task(log_stdout=True)
def multiply(num1: float, num2: float) -> float:
    """Multiply two numbers"""
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
    return result


@task(log_stdout=True)
def subtract(num1: float, num2: float) -> float:
    """Subtract two numbers"""
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
    return result


@task(log_stdout=True)
def divide(num1: float, num2: float) -> float:
    """Divide two numbers"""
    if num2 != 0:
        result = num1 / num2
    else:
        result = None
    print(f"{num1} / {num2} = {result}")
    return result


@task(log_stdout=True)
def sqrt(num1: float) -> float:
    """Take the square root of a number"""
    result = math.sqrt(num1)
    print(f"sqrt({num1}) = {result}")
    return result


@task
def output(
    num_a: float, num_b: float, num_c: float, result1: float, result2: float
):
    """Write a message to a log file"""
    with open('/tmp/maths_output.txt', 'w') as output_file:
        msg = (
            'Running quadratic formula with '
            f'a={num_a}, b={num_b}, c={num_c}:\n'
            f' - result1={result1:0.3}\n'
            f' - result2={result2:0.3}\n'
        )
        output_file.write(msg)
