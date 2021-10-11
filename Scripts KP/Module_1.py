"""
    D169 (LR, WD) Analysis
"""

import os
import pickle

import utils as u

#####################################################################################################

def run_module_1():
    PATH = "./Metrics"
    
    names = ["DL169 (LR,WD) (32)", 
             "DL169 (LR,WD) (64)", 
             "DL169 (LR,WD) (128)", 
             "DL169 (LR,WD) (256)", 
             "DL169 (LR,WD) (512)"]
    
    batch_sizes = [name.split()[-1][1:-1] for name in names]

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
