class Multiplication:
    """
    A class to perform multiplication operations.
    """

    def __init__(self, a: int, b: int):
        """
        Constructor to initialize two numbers for multiplication.

        :param a: First number
        :param b: Second number
        """
        self.a = a
        self.b = b

    def multiply(self, x: int, y: int) -> int:
        """
        Multiplies two integers.

        :param x: First integer
        :param y: Second integer
        :return: Product of x and y
        """
        return x * y

    def multiply_float(self, x: float, y: float) -> float:
        """
        Multiplies two floats.

        :param x: First float
        :param y: Second float
        :return: Product of x and y
        """
        return x * y


# Main function to test the multiplication class
if __name__ == "__main__":
    # Create an instance of the Multiplication class
    mult = Multiplication(5, 10)

    # Test integer multiplication
    int_result = mult.multiply(5, 6)
    print(f"Multiplication of 5 and 6 (integers): {int_result}")

    # Test float multiplication
    float_result = mult.multiply_float(5.5, 2.2)
    print(f"Multiplication of 5.5 and 2.2 (floats): {float_result}")
