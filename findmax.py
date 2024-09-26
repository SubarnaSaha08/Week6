class MaxOfThree:
    """
    This class is used to get the max value of three numbers.

    Attributes:
    ----------
    number1: int
        First number.
    number2: int
        Second number.
    number3: int
        Third number.

    Methods:
    -------
    find_max():
        Finds the maximum among three numbers.

    Author:
    -------
    Sudipta Singha
    """

    def __init__(self, number1, number2, number3):
        """
        Initializes the MaxOfThree class with three numbers.

        Parameters:
        ----------
        number1: int
            The first number.
        number2: int
            The second number.
        number3: int
            The third number.
        """
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3

    def find_max(self):
        """
        Finds the maximum among three numbers.

        Returns:
        -------
        int
            The maximum number among the three.
        """
        return max(self.number1, self.number2, self.number3)


# Example usage
if __name__ == "__main__":
    max_of_three = MaxOfThree(5, 10, 3)
    print("The maximum number is: ", max_of_three.find_max())
