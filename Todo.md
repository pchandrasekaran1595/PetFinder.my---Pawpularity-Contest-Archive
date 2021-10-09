1. [**Completed in Colab**] ~~Write a kaggle notebook to get the features from all the pytorch models available. Perform 10 Fold CV on all the features.~~

2. Work on reducing the CV score of densenet (D169), since it has the least difference between CV and LB.

3. [**Dropped**] ~~Train a network on grayscale images. (Full + Few Layers)~~

4. For color images:
    1. Train entire network
    2. Train only last few layers.
    3. Train only the final ANN layer and then finetune entire model.

5. Analyze metadata; check CV for different ANN and ML architectures.
 
6. [**Completed**] ~~Use the best models obtained from `1.`; submit and check LB.~~

7. [**Completed**] ~~Create Augmented Features for different seeds.~~

8. [**Completed**] ~~Perform 10 Fold CV on augmented features.~~

9. Create Augmented Features for different seeds for all the models.

10. Seed Analysis on data splits, dataloader creation and model initialization.  
    a. [**Completed**] ~~Analyze it on Pretrained Features (UA)~~  
    b. Analyze it on Pretrained Features (A)

11. Train Feature Models using Augmented and Unaugmented Data.
    1. [**Completed**] ~~(A, UA) fed as seperate inputs, add up MSELoss().~~
    2. [**Completed**] ~~(A, UA) concatenated along axis=0, train normally.~~
    3. Perform analysis as in `2.`, but stack multiple augmented features.
