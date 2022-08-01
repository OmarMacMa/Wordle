from random import randint
from typing import List


def won(tried: str) -> bool:
    return set(tried) == {"🟩"}


def change_input_visual(lst_guess: List, tried: str) -> str:
    lst_tried = list(tried)
    lst_vis = list(tried)
    lst_letters = lst_guess[::]
    for i in range(len(lst_guess)):
        if lst_tried[i] == lst_guess[i]:
            lst_vis[i] = "🟩"
            lst_letters.remove(lst_tried[i])
    for i in range(len(lst_guess)):
        if lst_tried[i] in lst_guess and lst_tried[i] in lst_letters \
        and lst_vis[i] != "🟩":
            lst_vis[i] = "🟨"
            lst_letters.remove(lst_tried[i])
    return "".join(lst_vis)


def select_random_word() -> str:
    fl = open("words_bank.txt", "r")
    rand = randint(0, 19)
    words = fl.readlines()
    fl.close()
    return words[rand].rstrip()

def main():
    win: bool = False
    word_to_guess: str = select_random_word()
    lst_word: List = list(word_to_guess)
    while win == False:
        visual: str = "_ "*len(word_to_guess)
        inp: str = input(f"Try your guess of: \n{visual}\n").upper()
        while len(inp) != len(word_to_guess):
            print("The guess must be of the same length")
            inp = input(f"Try your guess of: \n{visual}\n").upper()
        inp = change_input_visual(lst_word, inp)
        print(inp)
        win = won(inp)
    print("You won")


if __name__ == "__main__":
    main()