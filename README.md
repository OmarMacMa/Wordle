# Wordle
It is a word guessing game implemented to play on the command line. The game is played by typing a word of the length shown on the screen and then pressing enter. If a letter is in the word, but not in the correct position, it will be displayed as a yellow square. If a letter is in the word and in the correct position, it will be displayed as a green square. If a letter is not in the word, it will appear just the letter itself.

This game is based on the [Wordle](https://www.nytimes.com/games/wordle/index.html) game

Words are chosen from the *words_bank.txt* file, from a bank of 52 words with a length between 4 and 9 letters.

Here is an example of a play:\
\
![Battery](./Images/battery_guess.png)

Plans for the future:
- Make the game accept only words from a *dictionary.txt* file.
- Show the letters that have already been tried.
- Add a limit of tries.
- The user to choose the lenght of the playing word, as a difficulty level.

This game is written in Python 3.8. The files needed to run the game are:
- *words_bank.txt*
- *wordle.py*

And can be played by typing:
```bash
python3 wordle.py
```