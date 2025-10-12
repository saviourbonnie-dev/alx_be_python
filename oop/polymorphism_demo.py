#!/usr/bin/python3
"""Defines classes demonstrating polymorphism and method overriding in Python."""

import math


class Shape:
    """Base class representing a generic shape."""

    def area(self):
        """Raise error to enforce overriding in subclasses."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length: float, width: float):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius: float):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

