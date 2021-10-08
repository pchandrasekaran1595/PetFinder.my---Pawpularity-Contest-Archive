import os
import sys
import pickle

#####################################################################################################

def analyze():
    PATH = "C:/Users/Ourself/Desktop/Repos/PetFinder/Misc"
    MODEL_NAMES  = ["resnet18", "resnet34", "resnet50", "resnet101", "resnet152",
                    "resnext50", "resnext101",
                    "wresnet50", "wresnet101",
                    "vgg11", "vgg13", "vgg16", "vgg19",
                    "densenet121", "densenet161", "densenet169", "densenet201",
                    "mobilenet"]

    name = None

    args_1 = "--name"

    if args_1 in sys.argv: name = sys.argv[sys.argv.index(args_1) + 1]

    assert(name is not None)

    with open(os.path.join(PATH, name + ".pkl"), "rb") as fp:
        metrics = pickle.load(fp)

    for i in range(len(metrics)):
        RMSE = []
        for j in range(len(metrics[i])):
            RMSE.append(metrics[i][j]["RMSE"])
    
        best_index = RMSE.index(min(RMSE))
        print("Model: {}, BestCV: {:.5f} (F{}), AvgCV: {:.5f}".format(MODEL_NAMES[i].capitalize(), 
                                                                metrics[i][best_index]["RMSE"], 
                                                                metrics[i][best_index]["Fold"],
                                                                sum(RMSE) / len(RMSE)))



#####################################################################################################
