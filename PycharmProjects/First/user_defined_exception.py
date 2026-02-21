# user_defined_exception.py

class NegativeError(Exception):
    """Custom exception for negative dimensions"""

    def __init__(self):
        self.msg = "-ve dimension"

    def __str__(self):
        return self.msg


def area(length, breadth):
    """Calculate area of rectangle"""

    if length >= 0 and breadth >= 0:
        return length * breadth
    else:
        raise NegativeError()


# Main Program
try:
    print("Area =", area(-3, 5))

except NegativeError as e:
    print("Error:", e)