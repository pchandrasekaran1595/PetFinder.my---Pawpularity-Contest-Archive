import matplotlib.pyplot as plt

#####################################################################################################

def make_plot():
    
    names  = ["D169UA", "D121UA", "D161UA", "D169A49", "D169S49", "Stacked"]

    BestCV = [17.20356, 17.02147, 17.13855, 17.56233, 17.16049, 17.41826]

    AvgCV  = [18.48411, 18.49810, 18.42714, 19.07615, 18.50818, 18.665005]

    LB     = [18.38553, 18.78301, 18.83728, 18.70162, 18.37173, 18.45663]


    plt.figure()
    # plt.stem(names, BestCV, linefmt="-", markerfmt="o", label="BestCV", use_line_collection=True)
    # plt.stem(names, AvgCV, linefmt="-", markerfmt="x", label="AvgCV", use_line_collection=True)
    # plt.stem(names, LB, linefmt="-", markerfmt="^", label="LB", use_line_collection=True)
    plt.plot(names, BestCV, "r", label="BestCV")
    plt.plot(names, AvgCV, "b", label="AvgCV")
    plt.plot(names, LB, "g", label="LB")
    plt.grid()
    plt.legend()

    figmngr = plt.get_current_fig_manager()
    figmngr.window.state("zoomed")
    plt.show()

#####################################################################################################
