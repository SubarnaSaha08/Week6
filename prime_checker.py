class PrimeChecker:
    """
    A class used to check if a number is prime.

    Attributes
    ----------
    number : int
        The number to check for primality.

    Methods
    -------
    is_prime() -> bool
        Returns True if the number is prime, False otherwise.
    """

    def __init__(self, number: int):
        """
        Initializes the PrimeChecker with the given number.

        Parameters
        ----------
        number : int
            The number to check for primality.

        Raises
        ------
        ValueError
            If the input number is less than or equal to 1.
        """
        if number <= 1:
            raise ValueError("Prime numbers must be greater than 1.")

        self.number = number

    def is_prime(self) -> bool:
        """
        Check if the number provided during initialization is a prime number.

        A prime number is a natural number greater than 1.
        This number has no positive divisors other than 1 and itself.

        Returns
        -------
        bool
            True if the number is prime, False otherwise.
        """
        if self.number == 2:
            return True

        if self.number % 2 == 0:
            return False

        for i in range(3, int(self.number ** 0.5) + 1, 2):
            if self.number % i == 0:
                return False

        return True


if __name__ == "__main__":
    """
    Main function for the PrimeChecker class.
    This class takes manual input from the user.

    The program prompts the user to enter an integer.
    This integer is checked to determine
    if it is a prime number using the `PrimeChecker` class.

    Workflow:
    ---------
    1. The user is prompted to enter a number.
    2. The number is converted to an integer.
    3. Then, the number is passed to the `PrimeChecker` class.
    3. The `is_prime()` method is called to determine
        whether the number is prime.
    4. The result is printed to the console.
    5. If the number entered is less than or equal to 1,
        a `ValueError` is raised with the message
        "Prime numbers must be greater than 1."

    Input:
    ------
    - An integer from the user.

    Exceptions:
    -----------
    ValueError:
        Raised if the user enters a number less than or
        equal to 1 or an invalid input.
    """
    try:
        number = int(input("Enter a number to check if it's prime: "))
        prime_checker = PrimeChecker(number)
        if prime_checker.is_prime():
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError as e:
        print(e)
