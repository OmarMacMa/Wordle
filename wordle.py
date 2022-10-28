import os
from random import randint
from typing import Dict, List, Set


class Wordle:
    # Constructor
    def __init__(self, word):
        """Constructor of the class Wordle generates a dictionary with all
        letters of the alphabet, the length of the word, a list with the
        visual given to the user, sets of letters that are in the word,
        letters in the right position, letters not in the word and letters
        in the word but not in the right position"""
        self._word: str = word
        self.letters: Dict[int, str] = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E",
                                        5: "F", 6: "G", 7: "H", 8: "I", 9: "J",
                                        10: "K", 11: "L", 12: "M", 13: "N",
                                        14: "O", 15: "P", 16: "Q", 17: "R",
                                        18: "S", 19: "T", 20: "U", 21: "V",
                                        22: "W", 23: "X", 24: "Y", 25: "Z"}
        self._length: int = len(word)
        self.win: bool = False
        self.visual: List[str] = ["__"] * self._length
        self.word_letters: Dict[str, int] = {}
        for letter in self._word:
            if letter in self.word_letters:
                self.word_letters[letter] += 1
            else:
                self.word_letters[letter] = 1
        self.words_tried: Set[str] = set()
        self.letters_green: Dict[str, int] = {}
        self.letters_yellow: Dict[str, int] = {}
        self.letters_red: Set[str] = set()

    # Property to get the length of the word

    @property
    def length(self):
        return self._length

    # Function that compares the word given by the user with the word to guess

    def compare_word(self, word_tried) -> None:
        """The function compares the word given by the user with the word to
        guess, if the word is correct the user wins, if the word is not correct
        the function updates local variables by calling an internal function"""
        if word_tried in self.words_tried:
            print("You already tried this word")
        elif len(word_tried) != self._length:
            print("The word must be of the same length")
        elif word_tried == self._word:
            self.win = True
            self.change_visual(word_tried)
            self.print_visual()
        else:
            self.change_visual(word_tried)
            self.words_tried.add(word_tried)

    # Function that updates local variables

    def change_visual(self, word_tried) -> None:
        """Function that updates the visual, the letters in the right
        position, the letters in the word but not in the right position
        and the letters not in the word"""
        for i in range(len(word_tried)):
            if self._word[i] == word_tried[i]:
                self.visual[i] = word_tried[i]
                if word_tried[i] in self.letters_green:
                    self.letters_green[word_tried[i]] += 1
                else:
                    self.letters_green[word_tried[i]] = 1
            elif word_tried[i] in self.word_letters:
                if word_tried[i] in self.letters_yellow:
                    self.letters_yellow[word_tried[i]] += 1
                else:
                    self.letters_yellow[word_tried[i]] = 1
            else:
                self.letters_red.add(word_tried[i])

    # Function that prints the visual

    def print_visual(self) -> None:
        """Prints the visual of the letters used, in white those that haven't
        been used, in green those that are in the correct position, in yellow
        those that are in the word but not in the correct position and in red
        those that are not in the word"""
        for i in range(len(self.letters)):
            print(f"{self.letters[i]}", end=" | ")
        print()
        for i in range(len(self.letters)):
            if self.letters[i] in self.letters_red:
                print("🟥", end=" |")
            elif self.letters[i] in self.letters_green:
                print("🟩", end=" |")
            elif self.letters[i] in self.letters_yellow:
                print("🟨", end=" |")
            else:
                print("⬜", end=" |")
        print()
        print()
        
        if self.win:
            for i in range(self._length):
                print(self._word[i], end=" | ")
            print()
            for i in range(len(self.visual)):
                print("🟩", end=" |")
            print()
        else:
            print(" | ".join(self.visual))   # Podria llegar a eliminarse
            for i in range(len(self.visual)):
                if self.visual[i] == self._word[i]:
                    print("🟩", end=" |") 
                elif self.visual[i] == "🟨":
                    print("🟨", end=" |")
                else:
                    print("⬜", end=" |")
            print()
        self.reset_visual()

    # Missing function to reset the visual in each call of print_visual

    def reset_visual(self) -> None:
        """Resets the visual of the letters used, it changes the visual
        to ["__"] * length of the word"""
        self.visual = ["__"] * self._length


# Function that selects a random word from a file
def select_random_word() -> str:
    """Function that selects a random word from the words_bank.txt file"""
    fl = open("words_bank.txt", "r")
    rand = randint(0, 51)
    words = fl.readlines()
    fl.close()
    return words[rand].rstrip()


def main():
    word_to_guess: str = select_random_word()
    wordle: Wordle = Wordle(word_to_guess)
    while wordle.win == False:
        print(f"You have tried {len(wordle.words_tried)} words")
        word_tried: str = input(
            f"Try your guess of {wordle.length} letters:\n").upper()
        while len(word_tried) != wordle.length:
            os.system("clear")
            print("The guess must be of the same length")
            wordle.print_visual()
            word_tried = input(f"Try your guess of {wordle.length} " \
                                "letters:\n").upper()
        wordle.compare_word(word_tried)
        os.system("clear")
        wordle.print_visual()
        for i in range(len(word_tried)):
            print(f"{word_tried[i]}", end=" | ")
        print()
    os.system("clear")
    wordle.print_visual()
    for i in range(len(word_tried)):
        print(f"{word_tried[i]}", end=" | ")
    print("\nYou won")


if __name__ == "__main__":
    main()
