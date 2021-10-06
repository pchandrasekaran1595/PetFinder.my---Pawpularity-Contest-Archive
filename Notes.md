## **Notebook Information**

### **Analysis**
<pre>
1. 
    a. Dataset Creation (Latest: V1)
    b. Grayscale Dataset Creation (Latest: V2)
    c. Color Dataset Creation (Latest: V3)
   
2. Pretrained Features (Latest: V1)

3. Pytorch Dataloader Analysis (Latest: V3)

4. Meta Analysis (XGB) (Latest: V2)

5. Meta Analysis (DL) (1 HL)  (Latest: V7 [Fail])

6. Densenet Analysis (Latest: V5)

7. Densenet BS Analysis (Latest: V4)

8. Image Features (Fold and HL Analysis) (Latest: V4)
</pre>

---

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

6. Resnet (Train) (10FCV) (Latest: V4)

7. Mobilenet (Train) (10FCV) (Latest: V4)

8. VGG (Train) (10FCV) (Latest: V2)
</pre>

---

&nbsp;

---

1. Images and Meta Ensemble (Latest: V1)

2. Densenet (Inference) (Latest: V2) [Uses V1 Densenet (Train) (10FCV)]
   BestCV, AvgCV, LB = 17.20356 (F3), 18.48411, 18.38553  

3. Resnet (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.19295 (F3), 18.56848, _

4. Mobilenet (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.68768 (F3), 18.80634, _

5. VGG (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.58885 (F3), 18.80410, _

</pre>

---

&nbsp;

## Most Optimal Model so far (Unaugmented Data):
<pre>
    Backbone : Densenet
    LR       : 1e-2(10), 1e-3(5)
    WD       : 0.0(10), 1e-3(5)
    HL       : []
    BS       : 32
    SEED     : ??
</pre>

&nbsp;

---