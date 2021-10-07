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
   {'Fold': 1,  'RMSE': 18.057433709941307}
   {'Fold': 2,  'RMSE': 19.208499716765605}
   {'Fold': 3,  'RMSE': 17.20356384231105}
   {'Fold': 4,  'RMSE': 18.287770611865195}
   {'Fold': 5,  'RMSE': 18.943310906647508}
   {'Fold': 6,  'RMSE': 18.664445267902714}
   {'Fold': 7,  'RMSE': 19.246420345783864}
   {'Fold': 8,  'RMSE': 18.983535616655168}
   {'Fold': 9,  'RMSE': 17.793830771697124}
   {'Fold': 10, 'RMSE': 18.452296426408655}


6. Resnet (Train) (Latest: V4)
   {'Fold': 1,  'RMSE': 18.396494132423992}
   {'Fold': 2,  'RMSE': 19.129146592899257}
   {'Fold': 3,  'RMSE': 17.19295742261089}
   {'Fold': 4,  'RMSE': 18.602527727854827}
   {'Fold': 5,  'RMSE': 18.887026230698226}
   {'Fold': 6,  'RMSE': 18.832853773358515}
   {'Fold': 7,  'RMSE': 19.132354871148124}
   {'Fold': 8,  'RMSE': 18.756417600707913}
   {'Fold': 9,  'RMSE': 18.00501797435925}
   {'Fold': 10, 'RMSE': 18.75005079403802}


7. Mobilenet (Train) (Latest: V4)
   {'Fold': 1,  'RMSE': 18.543632413171544}
   {'Fold': 2,  'RMSE': 19.651486087414945}
   {'Fold': 3,  'RMSE': 17.687681586713534}
   {'Fold': 4,  'RMSE': 18.591171244812283}
   {'Fold': 5,  'RMSE': 19.207519797314387}
   {'Fold': 6,  'RMSE': 19.144033517847284}
   {'Fold': 7,  'RMSE': 19.410189995808572}
   {'Fold': 8,  'RMSE': 19.17186552553398}
   {'Fold': 9,  'RMSE': 18.071784272751003}
   {'Fold': 10, 'RMSE': 18.584009988630445}


8. VGG (Train) (Latest: V2)
   {'Fold': 1,  'RMSE': 18.466018161395}
   {'Fold': 2,  'RMSE': 19.359981893081862}
   {'Fold': 3,  'RMSE': 17.58885891207003}
   {'Fold': 4,  'RMSE': 18.622362825853763}
   {'Fold': 5,  'RMSE': 19.0011963636624}
   {'Fold': 6,  'RMSE': 19.231005250112577}
   {'Fold': 7,  'RMSE': 19.53539234966364}
   {'Fold': 8,  'RMSE': 19.205218313610448}
   {'Fold': 9,  'RMSE': 18.216399230286488}
   {'Fold': 10, 'RMSE': 18.814584033794514}


9. Dense + Meta (No Norm, Train) (Latest: V2)
   {'Fold': 1,  'RMSE': 17.974186124819028}
   {'Fold': 2,  'RMSE': 19.18652026337317}
   {'Fold': 3,  'RMSE': 17.225570687794686}
   {'Fold': 4,  'RMSE': 18.245223493824614}
   {'Fold': 5,  'RMSE': 19.00355821277801}
   {'Fold': 6,  'RMSE': 18.640010493520407}
   {'Fold': 7,  'RMSE': 19.3356389608441}
   {'Fold': 8,  'RMSE': 18.85120496768312}
   {'Fold': 9,  'RMSE': 17.835846618964375}
   {'Fold': 10, 'RMSE': 18.51920404423652}


10. Dense + Meta (Norm, Train) (Latest: V2)
   {'Fold': 1, 'RMSE': 18.03942124469386}
   {'Fold': 2, 'RMSE': 19.498367490288718}
   {'Fold': 3, 'RMSE': 17.306601077811937}
   {'Fold': 4, 'RMSE': 18.423025342397192}
   {'Fold': 5, 'RMSE': 19.072061828421518}
   {'Fold': 6, 'RMSE': 18.73027646546086}
   {'Fold': 7, 'RMSE': 19.47167450216092}
   {'Fold': 8, 'RMSE': 18.995501600951666}
   {'Fold': 9, 'RMSE': 17.974863667610098}
   {'Fold': 10, 'RMSE': 18.840179066757013}

</pre>

&nbsp;

### **Inference**
<pre>

1. Images and Meta Ensemble (Latest: V1)


2. Densenet (Inference) (Latest: V2) [Uses V1 Densenet (Train) (10FCV)]
   BestCV, AvgCV, LB = 17.20356 (F3), 18.48411, 18.38553  
   Diff(BestCV - LB) = 1.18197
   Diff(AvgCV - LB)  = 0.09858


3. Resnet (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.19295 (F3), 18.56848, _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


4. Mobilenet (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.68768 (F3), 18.80634, _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


5. VGG (Inference) (Latest: V1)
   BestCV, AvgCV, LB = 17.58885 (F3), 18.80410, _
   Diff(BestCV - LB) = _
   Diff(AvgCV - LB)  = _


6. Stacked Inference (Latest: V2)
   BestCV, AvgCV, LB = 17.41826 (F3), 18.665005, 18.45663
   Diff(BestCV - LB) = 1.03837
   Diff(AvgCV - LB)  = 0.208375


7. Stacked Inference - Best (Latest: V2)
   Only Use the Best Models
   AvgCV, LB = 17.41826, 18.47799
   Diff(AvgCV - LB)  = 1.05973


8. Dense + Meta (No Norm) (Latest: N/A)
   BestCV, AvgCV, LB = 17.22557(F3), 18.48170, _


9. Dense + Meta (Norm) (Latest: N/A)
   BestCV, AvgCV, LB = 17.30660(F3), 18.63520, _

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