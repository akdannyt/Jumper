import random

class Word:
    """The word that needs to be guessed
    
    The responsibility of Word is to generate a random word,
    keep track the guessed letters, display clues, and determine if the
    game is over
    
    Attributes:
        words (list[str]): The words that will be chosen from.
        word (str): The random word.
        word_len (int): The number of letters in the word.
        answer_letters (list[str]): The letters in word.
        guess_letters (list[str]): The letters that have been guessed.
        wrong (int): The number of wrong guesses


    """

    def __init__(self):
        """Constructs a new Word.

#         Args:
            self (Word): An instance of Word.
#         """
        words = ["fungi", "charm", "gully", "inter","whoop","taunt","leery","class","theme","lofty","tibia","booze","alpha",
        "thyme","doubt","parer","chute","stick","trice","alike","recap","saint","glory","grate","admit","brisk","soggy","usurp","scald","scorn"]
        self.word = random.choice(words)
        self.word_len = len(self.word)
        self.answer_letters = []
        for i in range(self.word_len):
            self.answer_letters.append(self.word[i])
        self.guess_letters = []
        self.wrong = 0
    
    def display(self):
        """Displays the parachuter.

        Args:
            self (Word): An instance of Word.
        """
        l1 = " ___  "
        l2 = "/___\ "
        l3 = "\   / "
        l4 = " \ /  "
        l5 = "  0   "
        l6 = " /|\  "
        l7 = " / \  "
        l8 = "      "
        l9 = "^^^^^^"
        lx = "  X   "

        parachute = [l1,l2,l3,l4]
        man = [l5,l6,l7,l8,l9]
        xman = [lx,l6,l7,l8,l9]
        for i in range(self.wrong,4):
            print(parachute[i])
        if self.wrong < 4:
            for i in range(0,5):
                print(man[i])
        else:
            for i in range(0,5):
                print(xman[i])

    def clue(self):
        """Displays the letters of the hidden word that have been correctly guessed.

        Args:
            self (Word): An instance of Word.
        """
        for i in range(self.word_len):
            if self.word[i] in self.guess_letters:
                print(self.word[i], end=' ')
            else:
                print('_', end=' ')
        print(" ")
        print(" ")


    def update_guesses(self, guess):
        """Updates the list of guessed letters and checks if the letter was in the word.

        Args:
            self (Word): An instance of Word.
            guess (Guess): The current guess from the class Guess
        """
        self.guess_letters.append(guess.get_guess())
        if guess.get_guess() in self.answer_letters:
            return
        else:
            self.wrong += 1

    def win(self):
        """Whether or not the player has won the game.

        Args:
            self (Word): An instance of Word.
            
        Returns:
            boolean: True if the player guessed all of the letters; false if otherwise.
        """
        count = 0
        for i in range(self.word_len):
            if self.word[i] in self.guess_letters:
                count += 1
        return (count == self.word_len)

    def game_over(self):
        """Whether or not the player has used all of their guesses.

        Args:
            self (Word): An instance of Word.
            
        Returns:
            boolean: True if the player used all of their guesses; false if otherwise.
        """
        return (self.wrong == 4)
