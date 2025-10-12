#!/usr/bin/python3
"""Defines a Calculator class demonstrating class methods and static methods."""


class Calculator:
    """A class demonstrating the difference between class and static methods."""

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers (static method)."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers (class method)."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

