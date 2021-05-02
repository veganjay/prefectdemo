"""This module creates and registers several Prefect flows.
The flows use tasks defined in the math.tasks modules that
define basic mathematical operations.

The flows are:

- Add: add two numbers
- Formula1: Calculate (a + b) * c
- Formula2: Calcuate (a * c) + (b * c), same result as Formula1
- Quadratic Formula: Solve the roots of a quadratic equation

To run:

   $ prefect run flow --name "Add" --project demo -ps '{"num1": 12, "num2": 52}'

   $ prefect run flow --name "Formula1" --project demo \
     -ps '{"a": 3, "b": 4, "c": 5}'

   $ prefect run flow --name "Formula2" --project demo \
     -ps '{"a": 3, "b": 4, "c": 5}'

   $ prefect run flow --name "QuadraticFormula" --project demo \
     -ps '{"a": 1, "b": 0, "c": -9}'
"""
from prefect import Flow, Parameter

from maths.tasks import add, subtract, multiply, divide, sqrt, output


def addition_flow():
    """Create a simple flow to add two numbers together."""
    with Flow("Add") as flow_add:
        num1 = Parameter('num1')
        num2 = Parameter('num2')
        _ = add(num1, num2)

    return flow_add


def formula1_flow():
    """Create a flow to run the equation:
    (a + b) * c
    """
    with Flow("Formula1") as flow:
        num1 = Parameter('a')
        num2 = Parameter('b')
        num3 = Parameter('c')
        result1 = add(num1, num2)
        _ = multiply(result1, num3)

    return flow


def formula2_flow():
    """Create a flow to run the equation:
    (a * c) + (b * c)
    """
    with Flow("Formula2") as flow:
        num1 = Parameter('a')
        num2 = Parameter('b')
        num3 = Parameter('c')
        result1 = multiply(num1, num3)
        result2 = multiply(num2, num3)
        _ = add(result1, result2)

    return flow


def quadratic_formula_flow():
    """Create a flow to use the quadratic formula
    The quadartic formula is: (-b +/ sqrt(b**2 - 4ac)) / 2a
    """
    with Flow("QuadraticFormula") as flow:
        # Obtain parameters from the flow
        num_a = Parameter('a')
        num_b = Parameter('b')
        num_c = Parameter('c')

        # Use the math tasks to build the quadratic formula
        negative_b = subtract(0, num_b)

        b_squared = multiply(num_b, num_b)
        a_times_c = multiply(num_a, num_c)
        four_a_c = multiply(4, a_times_c)
        b_squared_minus_four_a_c = subtract(b_squared, four_a_c)
        sqrt_b_squared_minus_four_a_c = sqrt(b_squared_minus_four_a_c)

        two_a = multiply(2, num_a)

        result1_numerator = add(negative_b, sqrt_b_squared_minus_four_a_c)
        result2_numerator = subtract(negative_b, sqrt_b_squared_minus_four_a_c)

        result1 = divide(result1_numerator, two_a)
        result2 = divide(result2_numerator, two_a)

        # Output results to log file
        output(num_a, num_b, num_c, result1, result2)

    return flow


def main():
    """Register the flows."""
    for flow in [
        addition_flow(),
        formula1_flow(),
        formula2_flow(),
        quadratic_formula_flow(),
    ]:
        flow.register(project_name='demo')


if __name__ == '__main__':
    main()
