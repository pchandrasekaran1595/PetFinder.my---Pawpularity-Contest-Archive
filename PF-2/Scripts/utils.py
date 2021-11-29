import os
from termcolor import colored
os.system("color")

#####################################################################################################

def myprint(text: str, color: str) -> None:
    print(colored(text=text, color=color))


def breaker(num=50, char="*"):
    myprint("\n" + num*char + "\n", "magenta")

#####################################################################################################