import os
import sys
import pickle

#####################################################################################################

def analyzer_1():
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

def analyzer_2():
    PATH = "C:/Users/Ourself/Desktop/Repos/PetFinder/Misc"
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
        print("Model: {}, BestCV: {:.5f} (F{}, S{}), AvgCV: {:.5f}".format(metrics[i][best_index]["Model"].capitalize(), 
                                                                           metrics[i][best_index]["RMSE"], 
                                                                           metrics[i][best_index]["Fold"],
                                                                           metrics[i][best_index]["Seed"],
                                                                           sum(RMSE) / len(RMSE)))


#####################################################################################################

def analyzer_3():
    PATH = "C:/Users/Ourself/Desktop/Repos/PetFinder/Misc"
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
        print("BestCV: {:.5f} (F{}, S{}), AvgCV: {:.5f}".format(metrics[i][best_index]["RMSE"], 
                                                                metrics[i][best_index]["Fold"],
                                                                metrics[i][best_index]["Seed"],
                                                                sum(RMSE) / len(RMSE)))


####################################################################################################

def analyze():
    args_1 = "--analyze1"
    args_2 = "--analyze2"
    args_3 = "--analyze3"

    if args_1 in sys.argv: analyzer_1()
    if args_2 in sys.argv: analyzer_2()
    if args_3 in sys.argv: analyzer_3()


#####################################################################################################
