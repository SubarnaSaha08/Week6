class Addition:
    """A class to perform addition operations."""

    def __init__(self, value):
        """Initialize the class with a numeric value.

        Args:
            value (int or float): The initial value to be used in addition.
        """
        self.value = value

    def add(self, *args):
        """Add two or three numbers to the current value.

        Args:
            *args (int or float): The numbers to add.

        Returns:
            int or float: The result of the addition.

        Raises:
            ValueError: If the number of arguments is not 2 or 3.
        """
        if len(args) == 2:
            return self.value + args[0] + args[1]
        elif len(args) == 3:
            return self.value + args[0] + args[1] + args[2]
        else:
            raise ValueError("add() requires either 2 or 3 arguments")

    def add_floats(self, other: float):
        """Add a float value to the current value.

        Args:
            other (float): The float value to add.

        Returns:
            float: The result of the addition.
        """
        return self.value + other


def main():
    """Main function to demonstrate the Addition class."""
    # Create an instance of the Addition class
    adder = Addition(10)

    # Perform various addition operations
    print("Adding 5 and 3:", adder.add(5, 3))  # Output: 18
    print("Adding 2, 3, and 4:", adder.add(2, 3, 4))  # Output: 19
    print("Adding float 2.5:", adder.add_floats(2.5))  # Output: 12.5


if __name__ == "__main__":
    main()
