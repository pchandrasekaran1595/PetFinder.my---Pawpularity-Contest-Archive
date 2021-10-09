## **Notebook Information**

### **Analysis**
<pre>

1. 
    a. Dataset Creation (Latest: V1)
    b. Grayscale Dataset Creation (Latest: V2)
    c. Color Dataset Creation (Latest: V3)
    d. Color Dataset Creation (384) (Latest: V1)

   
2. 
   a. Pretrained Features (Latest: V1)
   b. Pretrained Features (Augmented) (Latest: V2)
   c. Pretrained Features (All) (Latest: V2)
   d. D169 (A, UA) Features (Latest: V1)

3. Pytorch Dataloader Analysis (Latest: V3)

4. Meta Analysis (XGB) (Latest: V2)

5. Meta Analysis (DL) (1 HL) (Latest: V7 [Fail])

6. Densenet Analysis (Latest: V5)

7. Densenet BS Analysis (Latest: V4)

8. Image Features (Fold and HL Analysis) (Latest: V4)

9. 
   a. Pretrained Model Weights (Latest: V1)
   b. Pretrained Model Weights (All) (Latest: V1)

10. All Features CV Analysis (Colab) 

   Model: Resnet18   , BestCV: 17.56810 (F3), AvgCV: 18.88930
   Model: Resnet34   , BestCV: 17.24156 (F3), AvgCV: 18.74975  
   Model: Resnet50   , BestCV: 17.19296 (F3), AvgCV: 18.56848  
   Model: Resnet101  , BestCV: 17.12310 (F3), AvgCV: 18.53340 
   Model: Resnet152  , BestCV: 17.15243 (F3), AvgCV: 18.54092 
   Model: Resnext50  , BestCV: 17.33056 (F3), AvgCV: 18.69707 
   Model: Resnext101 , BestCV: 17.27402 (F3), AvgCV: 18.51755
   Model: Wresnet50  , BestCV: 17.19350 (F3), AvgCV: 18.57485 
   Model: Wresnet101 , BestCV: 17.10483 (F3), AvgCV: 18.52638
   Model: Vgg11      , BestCV: 17.63321 (F3), AvgCV: 18.95783     
   Model: Vgg13      , BestCV: 17.58427 (F3), AvgCV: 18.84889
   Model: Vgg16      , BestCV: 17.58886 (F3), AvgCV: 18.80410
   Model: Vgg19      , BestCV: 17.47513 (F3), AvgCV: 18.76739
   Model: Densenet121, BestCV: 17.02147 (F3), AvgCV: 18.49810
   Model: Densenet161, BestCV: 17.13855 (F3), AvgCV: 18.42714
   Model: Densenet169, BestCV: 17.20356 (F3), AvgCV: 18.48411
   Model: Densenet201, BestCV: 17.07005 (F3), AvgCV: 18.45969
   Model: Mobilenet  , BestCV: 17.68768 (F3), AvgCV: 18.80634

   Best Model (BestCV) -> Densenet121
   Best Model (AvgCV)  -> Densenet161


11. Augmented Features CV Analysis (Colab)

   ------------------------------------------------------------
   Model: Densenet, BestCV: 18.00383 (F3, S33), AvgCV: 19.56775
   Model: Densenet, BestCV: 18.58269 (F3, S38), AvgCV: 19.93007
   Model: Densenet, BestCV: 17.56233 (F3, S49), AvgCV: 19.07615
   Model: Densenet, BestCV: 17.91412 (F3, S5) , AvgCV: 19.41350 
   Model: Densenet, BestCV: 18.31756 (F3, S51), AvgCV: 19.83152
   Model: Densenet, BestCV: 17.96301 (F3, S53), AvgCV: 19.37750
   Model: Densenet, BestCV: 18.39538 (F3, S61), AvgCV: 19.95182
   Model: Densenet, BestCV: 18.05967 (F3, S62), AvgCV: 19.71465
   Model: Densenet, BestCV: 18.05538 (F3, S65), AvgCV: 19.62465
   Model: Densenet, BestCV: 17.72818 (F3, S97), AvgCV: 19.24826

   Best Model (BestCV) -> Seed 49 Augment (17.56223)
   Best Model (AvgCV)  -> Seed 49 Augment (19.07615)
   ------------------------------------------------------------
   Model: Resnet  , BestCV: 18.15734 (F3, S33), AvgCV: 19.64033
   Model: Resnet  , BestCV: 18.72690 (F3, S38), AvgCV: 19.97403
   Model: Resnet  , BestCV: 17.84416 (F3, S49), AvgCV: 19.21140
   Model: Resnet  , BestCV: 17.97836 (F3, S5) , AvgCV: 19.47597
   Model: Resnet  , BestCV: 18.55108 (F3, S51), AvgCV: 19.89083
   Model: Resnet  , BestCV: 17.98777 (F3, S53), AvgCV: 19.38085
   Model: Resnet  , BestCV: 18.67789 (F3, S61), AvgCV: 20.03207
   Model: Resnet  , BestCV: 18.34269 (F3, S62), AvgCV: 19.82179
   Model: Resnet  , BestCV: 18.38207 (F3, S65), AvgCV: 19.78543
   Model: Resnet  , BestCV: 17.81187 (F3, S97), AvgCV: 19.33407

   Best Model (BestCV) -> Seed 97 Augment (17.81187)
   Best Model (AvgCV)  -> Seed 49 Augment (19.21140)
   ------------------------------------------------------------
   Model: Vgg     , BestCV: 18.47876 (F3, S33), AvgCV: 19.81500
   Model: Vgg     , BestCV: 18.83131 (F3, S38), AvgCV: 20.09474
   Model: Vgg     , BestCV: 18.03871 (F3, S49), AvgCV: 19.38239
   Model: Vgg     , BestCV: 18.26708 (F3, S5) , AvgCV: 19.70080
   Model: Vgg     , BestCV: 18.61832 (F3, S51), AvgCV: 20.04709
   Model: Vgg     , BestCV: 18.31016 (F3, S53), AvgCV: 19.59170
   Model: Vgg     , BestCV: 18.79034 (F3, S61), AvgCV: 20.14066
   Model: Vgg     , BestCV: 18.75636 (F3, S62), AvgCV: 19.95986
   Model: Vgg     , BestCV: 18.34278 (F3, S65), AvgCV: 19.76804
   Model: Vgg     , BestCV: 18.10266 (F3, S97), AvgCV: 19.53606

   Best Model (BestCV) -> Seed 49 Augment (18.03871)
   Best Model (AvgCV)  -> Seed 49 Augment (19.38239)
   ------------------------------------------------------------


12. D169 Seed Analysis (UA)

   BestCV: 17.16049 (F8, S49), AvgCV: 18.50818
   BestCV: 17.40329 (F3, S97), AvgCV: 18.51660
   BestCV: 17.82360 (F1, S53), AvgCV: 18.54451
   BestCV: 17.44112 (F5, S5) , AvgCV: 18.50566 
   BestCV: 17.57921 (F1, S33), AvgCV: 18.49070
   BestCV: 17.26649 (F7, S65), AvgCV: 18.48982
   BestCV: 18.07556 (F5, S62), AvgCV: 18.50482
   BestCV: 17.49405 (F1, S51), AvgCV: 18.51208
   BestCV: 17.59509 (F7, S38), AvgCV: 18.47640
   BestCV: 17.41412 (F5, S61), AvgCV: 18.52315

   Best Model (BestCV) -> Seed 49 (17.16049)
   Best Model (AvgCV)  -> Seed 38 (18.47640)


13. D169 (UA, A, 1) Analysis
    BestCV = 17.01836(F8)
    AvgCV  = 18.49328

   
14. D169 (UA, A, 2) Analysis
    BestCV = 18.00252(F9)
    AvgCV  = 18.62022

</pre>

&nbsp;

### **Train**
<pre>

1. Images (Baseline)(Train) (Latest: V2)


2. Images (Baseline)(Densenet Inference)  
   Latest: V4  
   Submitted: V1


3. Images (Baseline)(Stacked Inference)  
   Latest - V1  
   Submitted - V1


4. Densenet (Train) (5FCV) (Latest: V1)
   Validation RMSE calculated before transformation


5. Densenet (Train) (10FCV) (Latest: V2)
   BestCV = 17.20356 (F3)
   AvgCV  = 18.48411


6. Resnet (Train) (Latest: V4)
   BestCV = 17.19295 (F3)
   AvgCV  = 18.56848


7. Mobilenet (Train) (Latest: V4)
   BestCV = 17.68768 (F3)
   AvgCV  = 18.80634


8. VGG (Train) (Latest: V2)
   BestCV = 17.58885 (F3)
   AvgCV  = 18.80410


9. Dense + Meta (No Norm, Train) (Latest: V2)
   BestCV = 17.22557(F3) 
   AvgCV  = 18.48170


10. Dense + Meta (Norm, Train) (Latest: V2)
    BestCV = 17.30660(F3) 
    AvgCV  = 18.63520


11.[Dropped] 
   PetFinder - Gray384 - Dense Full (Colab)
   Batch Size = 20
   10 Minutes per Epoch
   Ran in Debug Mode (Epochs = 5, Folds = 3)
   Perform a Full Run


12. D121 (Train) (Latest: V1)
    BestCV = 17.02147(F3) 
    AvgCV  = 18.49810


13. D161 (Train) (Latest: V1)
    BestCV = 17.13855(F3) 
    AvgCV  = 18.42714


14. D169 (Train) (Augment Seed 49) (Latest: V1)
    BestCV = 17.56233(F3) 
    AvgCV  = 19.07615


15. D169 (Train) (Split Seed 49) (Latest: V2)
    BestCV = 17.16049(F8)
    AvgCV  = 18.50818


16. D169 (Train) (Split Seed 38) (Latest: V3)
    BestCV = 17.59508(F7)
    AvgCV  = 18.47640

</pre>

&nbsp;

### **Inference**
<pre>

1. Images and Meta Ensemble (Latest: V1)


2. Densenet (Inference) (Latest: V2) [Uses V1 Densenet (Train) (10FCV)]
   LB = 18.38553  
   Diff(BestCV - LB) = 1.18197
   Diff(AvgCV - LB)  = 0.09858


3. Resnet (Inference) (Latest: V1)
   LB = _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


4. Mobilenet (Inference) (Latest: V1)
   LB = _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


5. VGG (Inference) (Latest: V1)
   LB = _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


6. Stacked Inference (Latest: V2)
   BestCV = 17.41826 (F3) 
   AvgCV  = 18.665005
   LB     = 18.45663
   Diff(BestCV - LB) = 1.03837
   Diff(AvgCV - LB)  = 0.208375


7. Stacked Inference - Best (Latest: V2)
   Only Use the Best Models
   AvgCV = 17.41826
   LB    = 18.47799
   Diff(AvgCV - LB)  = 1.05973


8. D121 (Inference) (Latest: V1)
   LB = 18.78301
   Diff(BestCV - LB) = 1.76154
   Diff(AvgCV - LB)  = 0.28491


8. D161 (Inference) (Latest: V2)
   LB = 18.83728
   Diff(BestCV - LB) = 1.69873
   Diff(AvgCV - LB)  = 0.41014


9. D169 (Inference) (Augment Seed 49) (Latest: V1)
   LB = 18.70162
   Diff(BestCV - LB) = 1.13939
   Diff(AvgCV - LB)  = 0.37453


10. D169 (Inference) (Split Seed 49) (Latest: V2)
    LB = 18.37173
    Diff(BestCV - LB) = 1.21124
    Diff(AvgCV - LB)  = 0.13645
   

10. D169 (Inference) (Split Seed 38) (Latest: V1)
    LB = _
    Diff(BestCV - LB) = _
    Diff(AvgCV - LB)  = _

</pre>

---

&nbsp;

## **Most Optimal Model so far (Unaugmented Data)**
<pre>

    Backbone : Densenet
    KFold    : 10
    LR       : 1e-2(10), 1e-3(5)
    WD       : 0.0(10), 1e-3(5)
    HL       : []
    BS       : 32
    SEED     : ??

</pre>

&nbsp;

---

&nbsp;

Kaggle torch Version       - 1.7.1  
Kaggle torchvision Version - 0.8.1

---

&nbsp;

Appears to be a very slight difference when training on a CPU vs GPU.

---