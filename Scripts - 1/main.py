import sys

import utils as u
from Find_Best_Model import find
from Calc_Avg_CV_Score import calculate
from CV_Analyzer import analyze
from CV_LB_Plotter import make_plot

#####################################################################################################

def main():
    u.breaker()
    
    args_1 = "--find"
    args_2 = "--calc"
    args_3 = "--colab"
    args_4 = "--plot"

    if args_1 in sys.argv: find()
    if args_2 in sys.argv: calculate()
    if args_3 in sys.argv: analyze()
    if args_4 in sys.argv: make_plot()
    
    u.breaker()

#####################################################################################################

if __name__ == "__main__":
    sys.exit(main() or 0)

#####################################################################################################