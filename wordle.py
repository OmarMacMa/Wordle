from random import randint
from typing import Counter, Dict, List


def won(tried: str) -> bool:
    return set(tried) == {"🟩", " "}


def change_input_visual(lst_guess: List, tried: str, letters_dict) -> str:
    lst_tried = list(tried)
    lst_vis = list(tried)
    lst_letters = lst_guess[::]
    for i in range(len(lst_guess)):
        if lst_tried[i] == lst_guess[i]:
            if lst_tried[i] not in letters_dict:
                letters_dict[lst_tried[i]] = "🟩"
            lst_vis[i] = "🟩"
            lst_letters.remove(lst_tried[i])
    for i in range(len(lst_guess)):
        if lst_tried[i] in lst_guess and lst_tried[i] in lst_letters \
        and lst_vis[i] != "🟩":
            if lst_tried[i] not in letters_dict:
                letters_dict[lst_tried[i]] = "🟩"
            lst_vis[i] = "🟨"
            lst_letters.remove(lst_tried[i])
    return "".join(lst_vis)


def select_random_word() -> str:
    fl = open("words_bank.txt", "r")
    rand = randint(0, 51)
    words = fl.readlines()
    fl.close()
    return words[rand].rstrip()


"""def store_letters(tried: str, letters_set: Set) -> Set:
    for character in tried:
        if character not in letters_set:
            letters_set.add(character)
    return letters_set"""


def compara_palabra(palabra_correcta, intento_palabra):
    lista_visual = [""] * len(palabra_correcta)
    dict_letras_palabra_correcta = Counter(palabra_correcta)
    set_letras_palabra_correcta = set(palabra_correcta) # Diccionario con contador de aparicion
    for i in range(len(palabra_correcta)):
        if intento_palabra[i] == palabra_correcta[i]:
            lista_visual[i] = "🟩"
            dict_letras_palabra_correcta[intento_palabra[i]] -= 1 # Restar 1 en diccionario
            # Diccionario constante already_tried[intento_palabra[i]] = "🟩"
        elif dict_letras_palabra_correcta[intento_palabra[i]] > 0:  # Si esta en diccionario y es mayor que 0
            lista_visual[i] = "🟨"
            dict_letras_palabra_correcta[intento_palabra[i]] -= 1 # Restar 1 en diccionario
            # Diccionario constante already_tried[intento_palabra[i]] = "🟨"
        else:
            lista_visual[i] = intento_palabra[i]
    return " ".join(lista_visual)


def main():
    win: bool = False
    correct_word: str = select_random_word()
    # Constante letters: Dict[str][str] = {}
    visual: str = ""
    while win == False:
        # From the constante print(f"You have used {letters}")
        tried_word: str = input(f"Try your guess of {len(correct_word)} letters:\n").upper()
        while len(tried_word) != len(correct_word):
            print("The guess must be of the same length")
            tried_word = input(f"Try your guess of {len(correct_word)} letters:\n").upper()
        visual = compara_palabra(correct_word, tried_word)
        tried_wordle = []
        for i in range(len(correct_word)):
            tried_wordle.append(tried_word[i])
        tried_word = " ".join(tried_wordle)
        print(tried_word)
        print(visual)
        win = won(visual)
    print("You won")
        


"""def main():
    win: bool = False
    word_to_guess: str = select_random_word()
    lst_word: List = list(word_to_guess)
    while win == False:
        print(f"You have used {letters}")
        inp: str = input(f"Try your guess of {len(lst_word)} letters").upper()
        while len(inp) != len(word_to_guess):
            print("The guess must be of the same length")
            inp = input(f"Try your guess of {len(lst_word)} letters").upper()
        letters = store_letters(inp, letters)
        inp = change_input_visual(lst_word, inp)
        print(inp)
        win = won(inp)
    print("You won")"""


if __name__ == "__main__":
    main()