"""
    D169 (LR, WD) Analysis
"""

import os
import sys
import pickle

import utils as u

#####################################################################################################

def run_module_1():
    PATH = "./Metrics - 2"

    names = ["D169 (LR,WD) (32) (CC)", 
             "D169 (LR,WD) (64) (CC)", 
             "D169 (LR,WD) (128) (CC)", 
             "D169 (LR,WD) (256) (CC)", 
             "D169 (LR,WD) (512) (CC)"]

    args = "--nc"
    if args in sys.argv: 
        names = ["D169 (LR,WD) (32) (NC)", 
                 "D169 (LR,WD) (64) (NC)", 
                 "D169 (LR,WD) (128) (NC)", 
                 "D169 (LR,WD) (256) (NC)", 
                 "D169 (LR,WD) (512) (NC)"]
    
    batch_sizes = [name.split()[-2][1:-1] for name in names]

    u.breaker()
    for i in range(len(names)):
        with open(os.path.join(PATH, names[i] + ".pkl"), "rb") as fp:
            params = pickle.load(fp)
        
        rmse = []
        for a in range(len(params)):
            for b in range(len(params[a])):
                rmse.append(params[a][b]["RMSE"])
        
        best_index = rmse.index(min(rmse))
        best_index_1 = best_index // 10
        best_index_2 = best_index % 10

        print("Batch Size: {}, Params: {}".format(batch_sizes[i], params[best_index_1][best_index_2]))

    u.breaker()
    
#####################################################################################################
