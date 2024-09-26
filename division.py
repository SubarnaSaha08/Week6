class Divider:
    """
    A class used to perform division operations.

    Attributes
    ----------
    dividend : float
        The number to be divided.

    Methods
    -------
    divide_by(divisor: float) -> float
        Divides the dividend by the divisor and returns the result.
    """

    def __init__(self, dividend: float):
        """
        Initializes the Divider with the given dividend.

        Parameters
        ----------
        dividend : float
            The number that will be divided.
        """
        self.dividend = dividend

    def divide_by(self, divisor: float) -> float:
        """
        Divides the dividend by the given divisor.

        Parameters
        ----------
        divisor : float
            The number to divide the dividend by.

        Returns
        -------
        float
            The result of the division.

        Raises
        ------
        ZeroDivisionError
            If the divisor is zero.
        """
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.dividend / divisor


if __name__ == "__main__":
    # Prompt the user to input the dividend
    try:
        dividend = float(input("Enter the number to be divided: "))

        # Create an instance of Divider with the user-provided dividend
        divider = Divider(dividend)

        # Prompt the user to input the divisor
        divisor = float(input("Enter the divisor: "))

        # Perform division and print the result
        result = divider.divide_by(divisor)
        print(f"{dividend} divided by {divisor} is {result}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except ZeroDivisionError as e:
        print(e)
