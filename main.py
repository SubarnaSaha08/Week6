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
    pass
