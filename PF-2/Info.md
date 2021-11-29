### **Analysis**

1. **Final Layer Analysis**
    1. Adam
        1. BN, WN 
            1. Best : (5e-4, 1e-1) [17.05965]
            2. Avg  : (5e-4, 1e-1) [18.44728]
        2. BN, _ 
            1. Best : (1e-3, 1e-1) [17.08852]
            2. Avg  : (5e-4, 1e-1) [18.45567]
        3. _, BN
            1. Best : (1e-3, 0) [17.13872]
            2. Avg  : (1e-3, 1e-1) [18.60270]
        4. _, _
            1. Best : (1e-4, 1e-1) [17.18451]
            2. Avg  : (1e-4, 1e-1) [18.61622]
    2. SGD (Momentum = 0.9)
        1. BN, WN 
            1. Best : (1e-3, 1e-1) [17.07662]
            2. Avg  : (1e-3, 1e-1) [18.44286]
        2. BN, _ 
            1. Best : (1e-3, 1e-1) [17.10056]
            2. Avg  : (1e-3, 1e-1) [18.45834]
        3. _, BN
            1. Best : (1e-3, 1e-1) [17.10823]
            2. Avg  : (1e-3, 1e-1) [18.57969]
        4. _, _
            1. Best : (1e-4, 1e-1) [17.15477]
            2. Avg  : (1e-4, 1e-1) [18.61651]

<br/>

### **Inference**

1. **D169 Baseline (NC)**
    1. Using Model Trained with an Adam Optimizer
        1. LB   = 18.38887
        2. Best = 17.05965
        3. Avg  = 18.44728
        4. (LB - Best) = 1.32905
        5. (LB - Avg)  = 0.05858
    2. Using Model Trained with a SGD Optimizer
        1. LB   = 18.38422
        2. Best = 17.07662
        3. Avg  = 18.44286
        4. (LB - Best) = 1.3076
        5. (LB - Avg)  = 0.05864

2. **D169 (384, SGD, NC)**
    1. LB   = 18.52001
    2. Best = 16.87821
    3. Avg  = 18.36047
    4. (LB - Best) = 1.6418
    5. (LB - Avg)  = 0.15954

3. **D169 (512, SGD, NC)**
    1. LB   = 18.62262
    2. Best = 17.07177
    3. Avg  = 18.44957
    4. (LB - Best) = 1.55085
    5. (LB - Avg)  = 0.17305

4. **D169 Last Block (Rand Init) (SGD0.9) (5CV)**
    1. LB   = 18.77563
    2. Best = 18.54372
    3. Avg  = 18.97115
    4. (LB - Best) = 0.23191
    5. (LB - Avg)  = 0.19552

5. **D169 Last Block (Rand Init) (SGD0.9) (10CV)**
    1. LB   = 18.74027
    2. Best = 17.52850
    3. Avg  = 18.90940
    4. (LB - Best) = 1.21177
    5. (LB - Avg)  = 0.16913

6. **D169 Last Block (Pre Init) (SGD0.9)**
    1. LB   = 18.46918
    2. Best = 17.13578
    3. Avg  = 18.49836
    4. (LB - Best) = 1.3334
    5. (LB - Avg)  = 0.02918