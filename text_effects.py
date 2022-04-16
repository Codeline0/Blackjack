from time import sleep
import sys

def writing_effect(txt, time = 0.05):
    for char in txt:
        sleep(time)
        print(char, end="")
        sys.stdout.flush()

def rise_effect(txt, time):
    lines_txt = txt.split("\n")
    for line in lines_txt:
        print(line)
        sleep(time)

def enter_continue():
    input("Press enter to continue...")
    print("\033[A                             \033[A")