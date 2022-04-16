# Blackjack

Playable Blackjack on python terminal

## Table of contents

-   [Overview](#overview)
    -   [How to Play](#how-to-play)
    -   [The challenge](#the-challenge)
    -   [Screenshot](#screenshot)
    -   [Executing Program](#executing-program)
-   [My process](#my-process)
    -   [Built with](#built-with)
    -   [What I learned](#what-i-learned)
-   [Author](#author)

## Overview

### How to Play

Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
If you want to learn properly visit [Bicycle](https://bicyclecards.com/how-to-play/blackjack/).

### The challenge

Users should be able to:

-   Play a normal casino game of Blackjack against the computer(Dealer).
-   See other "players" play the game alongside them.
-   Play a tutorial that guides them trough a scripted game.

### Screenshot

![](./ss/blackjack-intro.gif)

### Executing program

-   Run the main.py script in terminal

```
python main.py
```

## My process

### Built with

-   Python 3.10.4
-   PEP 8

### What I learned

Writing effect for strings.

```python
def writing_effect(txt, time = 0.05):
    for char in txt:
        sleep(time)
        print(char, end="")
        sys.stdout.flush()
```

Elevating block effect for strings.

```python
def rise_effect(txt, time):
    lines_txt = txt.split("\n")
    for line in lines_txt:
        print(line)
        sleep(time)
```

## Author

-   Marco Cámez - [Codeline0](https://github.com/Codeline0)
