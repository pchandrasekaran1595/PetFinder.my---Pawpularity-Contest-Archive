import os
import sys
import pickle
import utils as u

#####################################################################################################

def find():
    PATH = "C:/Users/Ourself/Desktop/Repos/PetFinder/Misc"
    name = None

    args_1 = "--name"

    if args_1 in sys.argv: name = sys.argv[sys.argv.index(args_1) + 1]

    assert(name is not None)

    with open(os.path.join(PATH, name + ".pkl"), "rb") as fp:
        params = pickle.load(fp)
    
    RMSE = []
    for i in range(len(params)):
        RMSE.append(params[i]["RMSE"])
    
    index = RMSE.index(min(RMSE))

    u.breaker()
    print(params[index])
    u.breaker()

#####################################################################################################
