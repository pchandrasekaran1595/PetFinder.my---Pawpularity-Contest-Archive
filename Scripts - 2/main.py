import sys
from Module_1 import run_module_1
from Module_2 import run_module_2

#####################################################################################################

def main():
    args = "--module"

    if args in sys.argv: num = int(sys.argv[sys.argv.index(args) + 1])

    if num == 1: run_module_1()
    if num == 2: run_module_2()

#####################################################################################################

if __name__ == "__main__":
    sys.exit(main() or 0)

#####################################################################################################
