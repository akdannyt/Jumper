from game.terminal_service import TerminalService
from game.word import Word
from game.guess import Guess


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word (Word): The game's hidden word.
        is_playing (boolean): Whether or not to keep playing.
        guess (Guess): The player's guess.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = Word()
        self._is_playing = True
        self._guess = Guess()
        self._terminal_service = TerminalService()
        
    def start_game(self):
        """Starts the game by running the main game loop.
        Begins by outputing the players first clue.
        
        Args:
            self (Director): an instance of Director.
        """
        self._do_outputs()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Get's the player to guess a letter and updates the guess.

        Args:
            self (Director): An instance of Director.
        """
        guess = self._terminal_service.read_text("\nGuess a letter [a-z]: ")
        self._guess.change_guess(guess)
        
    def _do_updates(self):
        """Updates the guess list in word.

        Args:
            self (Director): An instance of Director.
        """
        self._word.update_guesses(self._guess)
        
    def _do_outputs(self):
        """Displays the clue and parachute.  Checks to see if the game should end.

        Args:
            self (Director): An instance of Director.
        """
        self._word.clue()
        self._word.display()
        if self._word.win():
            self._terminal_service.write_text("You Win")
            self._is_playing = False        
        if self._word.game_over():
            self._terminal_service.write_text("Game Over")
            self._is_playing = False
