"""
Utility functions for the workshop
"""

def greet(name):
    """Greet a user"""
    return f"Hello, {name}!"


def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# Participants can add more utility functions here