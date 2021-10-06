import sys

import utils as u
from Find_Best_Model import find
from Calc_Avg_CV_Score import calculate

#####################################################################################################

def main():
    u.breaker()
    
    args_1 = "--find"
    args_2 = "--calc"

    if args_1 in sys.argv:
        find()
    if args_2 in sys.argv:
        calculate()
    
    u.breaker()

#####################################################################################################

if __name__ == "__main__":
    sys.exit(main() or 0)

#####################################################################################################