"""
    D169 (LR, WD) Analysis
"""

import os
import sys
import pickle
import pandas as pd

import utils as u

#####################################################################################################

def run_module_3():
    PATH = "./Metrics - 2"

    name = None
    args = "--name"
    if args in sys.argv: name = sys.argv[sys.argv.index(args) + 1]

    with open(os.path.join(PATH, name + ".pkl"), "rb") as fp:
        params = pickle.load(fp)
        
    df = pd.DataFrame()
    for a in range(len(params)):
        temp_df = pd.DataFrame.from_dict(params[a])
        df = pd.concat((df, temp_df), axis=0)
    
    del temp_df

    lrs = sorted(list(set(df["LR"])))
    wds = sorted(list(set(df["WD"])))
    
    u.breaker()
    for lr in lrs:
        avgCVs, bestCVs = [], []
        for wd in wds:
            temp_df = df.loc[df["LR"] == lr]
            avgCV  = temp_df["RMSE"].loc[temp_df["WD"] == wd].mean()
            bestCV = temp_df["RMSE"].loc[temp_df["WD"] == wd].min()
            avgCVs.append(avgCV)
            bestCVs.append(bestCV)
            print("LR: {}, WD: {} [AvgCV: {:.5f}, BestCV: {:.5f}]".format(lr, wd, avgCV, bestCV))
        u.breaker()

#####################################################################################################
