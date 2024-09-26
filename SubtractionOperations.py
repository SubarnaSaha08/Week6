class SubtractionOperations:
    """
    Class for performing subtraction operations.
    """

    def __init__(self, number1=0, number2=0):
        """
        Constructor to initialize two numbers.
        :param number1: First number (default is 0)
        :param number2: Second number (default is 0)
        """
        self.number1 = number1
        self.number2 = number2

    def subtract(self, *args):
        """
        Subtracts two or more numbers.
        :param args: Numbers to subtract (at least two numbers required)
        :return: Result of subtraction
        """
        if len(args) < 2:
            raise ValueError(
                "At least two numbers are required for subtraction."
            )

        result = args[0]
        for num in args[1:]:
            result -= num
        return result


# Example usage of SubtractionOperations
if __name__ == "__main__":
    # Create an instance
    subtractor = SubtractionOperations()

    # Subtracting two numbers
    result_two_numbers = subtractor.subtract(10, 5)
    print(f"Result of subtracting two numbers (10 - 5): {result_two_numbers}")

    # Subtracting three numbers
    result_three_numbers = subtractor.subtract(20, 5, 3)
    print(f"Result of subtracting three numbers (20 - 5 - 3): "
          f"{result_three_numbers}")
