class Guess:

    """The player's letter guess.
    
    The responsibility of a Seeker is to keep track of the player's letter guess.
    Attributes:
        guess (str): The player's current guess [a-z].
    """

    def __init__(self):

        self.guess = " "
    """Constructs a Guess.

        Args:
            self (Seeker): An instance of Guess.
        """

    def get_guess(self):
        guess = self.guess
        return guess
    """Gets the current guess.
        Returns:
            str: The current guess,
        """

    def change_guess(self, guesss):
        self.guess = guesss
    """Changes the current guess.

        Args:
            self (Seeker): An instance of Guess.
            guess (int): The new guess.
        """