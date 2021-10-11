"""
    All Features CV Analysis
"""

import sys
import pickle
import pandas as pd
import matplotlib.pyplot as plt

import utils as u

#####################################################################################################

def run_module_2():
    PATH = "./Metrics/All Features CV Analysis.pkl"
    fontsize = 5.5

    args = "--shortlist"
    if args in sys.argv: 
        PATH = "./Metrics/Shortlisted Features CV Analysis.pkl"
        fontsize = 12

    with open(PATH, "rb") as fp:
        params = pickle.load(fp)
        
    df = pd.DataFrame()
    for a in range(len(params)):
        temp_df = pd.DataFrame.from_dict(params[a])
        df = pd.concat((df, temp_df), axis=0)
    
    del temp_df

    model_names = sorted(list(set(df["Model"])))
    avgCVs, bestCVs = [], []

    u.breaker()
    for model_name in model_names:
        avgCV  = df["RMSE"].loc[df["Model"] == model_name].mean()
        bestCV = df["RMSE"].loc[df["Model"] == model_name].min()
        avgCVs.append(avgCV)
        bestCVs.append(bestCV)
        print("{} [AvgCV: {:.5f}, BestCV: {:.5f}]".format(model_name, avgCV, bestCV))
    u.breaker()

    plt.figure()
    plt.plot(model_names, avgCVs, "r", label="AvgCV")
    plt.plot(model_names, bestCVs, "b", label="BestCV")
    plt.legend()
    plt.grid()
    plt.title("Avg and Best CV Scores")
    figmngr = plt.get_current_fig_manager()
    figmngr.window.state("zoomed")
    plt.xticks(fontsize=fontsize)
    plt.show()

#####################################################################################################
