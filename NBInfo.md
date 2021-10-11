## **Notebooks**

---

**Analysis**

1. Features
    1. Pretrained      
    2. Pretrained (All)  

<br/>

2. D169 Analysis
    1. CC
        1. LR, WD, BS
            1. Batch Size: 32, Params: {'Fold': 3, 'LR': 0.0005, 'WD': 0.1, 'RMSE': 17.1252116566921}
            2. Batch Size: 64, Params: {'Fold': 3, 'LR': 0.001, 'WD': 0.1, 'RMSE': 17.126835773918355}  
            3. Batch Size: 128, Params: {'Fold': 3, 'LR': 0.0005, 'WD': 0.1, 'RMSE': 17.13431670895495} 
            4. Batch Size: 256, Params: {'Fold': 3, 'LR': 0.0005, 'WD': 0.1, 'RMSE': 17.137577082219202}
            5. Batch Size: 512, Params: {'Fold': 3, 'LR': 0.001, 'WD': 0.1, 'RMSE': 17.131417446056336} 
        
        2. Best v/s Avg
            1. Batch Size: 32, BestCV (5e-4, 1e-1), AvgCV (1e-4, 1e-1)
            2. Batch Size: 64, BestCV (1e-3, 1e-1), AvgCV (5e-4, 1e-1)
            3. Batch Size: 128, BestCV (5e-4, 1e-1), AvgCV (5e-4, 1e-1)
            4. Batch Size: 256, BestCV (5e-4, 1e-1), AvgCV (5e-4, 1e-1)
            5. Batch Size: 512, BestCV (1e-3, 1e-1), AvgCV (1e-3, 1e-2)
        
        3. Split Seed
            Params: {'Seed': 49, 'Fold': 8, 'RMSE': 16.883282329889802} using (32, 5e-4, 1e-1)
    
    2. NC
        1. LR, WD, BS (SS49)
            1. Batch Size: 32, Params: {'Fold': 8, 'LR': 0.001, 'WD': 0.01, 'RMSE': 17.074325692012973}
            2. Batch Size: 64, Params: {'Fold': 8, 'LR': 0.001, 'WD': 0.01, 'RMSE': 17.055975391521706}
            3. Batch Size: 128, Params: {'Fold': 8, 'LR': 0.0005, 'WD': 0.1, 'RMSE': 17.0596548449943} 
            4. Batch Size: 256, Params: {'Fold': 8, 'LR': 0.001, 'WD': 0.1, 'RMSE': 17.070384670717644}
            5. Batch Size: 512, Params: {'Fold': 8, 'LR': 0.001, 'WD': 0.001, 'RMSE': 17.27364925862079} 
        
        2. Best v/s Avg 
            1. Batch Size: 32, BestCV (1e-3, 1e-2), AvgCV (1e-3, 1e-2)
            2. Batch Size: 64, BestCV (1e-3, 1e-2), AvgCV (5e-4, 1e-1)
            3. Batch Size: 128, BestCV (5e-4, 1e-1), AvgCV (5e-4, 1e-1)
            4. Batch Size: 256, BestCV (1e-3, 1e-1), AvgCV (1e-3, 1e-1)
            5. Batch Size: 512, BestCV (1e-3, 1e-3), AvgCV (1e-3, 1e-3)

<br/>

3. Meta DL Analysis
    1. LR, WD, BS
        1. Batch Size: 32, Params: {'LR': 0.001, 'WD': 0.0, 'Fold': 3, 'RMSE': 19.259673055085084}
        2. Batch Size: 64, Params: {'LR': 0.01, 'WD': 0.0, 'Fold': 3, 'RMSE': 19.276742589450585} 
        3. Batch Size: 128, Params: {'LR': 0.01, 'WD': 0.001, 'Fold': 3, 'RMSE': 19.28499796177486} 
        4. Batch Size: 256, Params: {'LR': 0.01, 'WD': 0.0, 'Fold': 3, 'RMSE': 19.29645227045374} 
        5. Batch Size: 512, Params: {'LR': 0.01, 'WD': 0.001, 'Fold': 3, 'RMSE': 19.28667163925248} 

<br/>

4. All Features CV Analysis
    1. CC
        1. Best --> {'Model': 'densenet201', 'Fold': 8, 'RMSE': 16.733944546854936}
        2. AvgCV Best -> Densenet201

<br/>

5. Shortlisted Features CV Analysis
    1. CC
        1. BestCV -> Densenet201 (16.73394)
        2. AvgCV  -> Densenet201 (18.32681)
         
        
<br/>
<br/>

**Train**

1. D169 
    1. Batch Size: 512 </br>
        Best CV : 17.13142 at Fold 3 </br>
        Avg CV  : 18.41612

    2. Batch Size: 32 <br/>
        Best CV : 17.12521 at Fold 3 </br>
        Avg CV  : 18.39669 <br/>

2. D201 <br/>
    Best CV : 16.73394 at Fold 8 <br/>
    Avg CV  : 18.32681
    
<br/>
<br/>

**Inference**

1. D169  
    1. Train Batch Size: 512 <br/>
        LB = 18.43603 </br>
        LB - Best = 1.30461 </br>
        LB - Avg  = 0.01991 </br>
    
    2. Train Batch Size: 32 <br/>
        LB = 18.41624 </br>
        LB - Best = 1.29103 </br>
        LB - Avg  = 0.01955 </br>

2. D169 (No CC) [*Used batch_size=512*] <br/>
   LB = 18.51597 </br>
   LB - Best = 1.38455 </br>
   LB - Avg  = 0.09985 </br>


3. D201 <br/>
    LB = 18.44899 <br/>
    LB - Best = 1.71505 <br/>
    LB - Avg  = 0.12218 <br/>

<br/>

---

<br/>

1. CC -> (128, 5e-4, 1e-1)
2. NC -> (128, 5e-4, 1e-1)

<br/>