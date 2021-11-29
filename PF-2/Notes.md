1. **Full CNN**
    1. Finetune
    2. Train from scratch

<br/>

2. **Pretrained Densenet169 Features**
    1. Adam Optimizer
        1. (BS, LR, WD, WN, BN) (NC) - 128, 5e-4, 1e-1, Yes, Yes
        2. (BS, LR, WD, WN, BN) (CC) - 128, 
    2. SGD Optimizer
        1. (BS, LR, WD, WN, BN) (NC) - 128, 1e-3, 1e-1, Yes, Yes
        2. (BS, LR, WD, WN, BN) (CC) - 128, 

<br/>

- All analysis must be done on CC and NC
- `Size != 224` performs bad on test data
- Train last few layers of different pretrained models. Compare CV performance. Let final layer be initialized by:
    1. Randomness
    2. Using a state_dict from the folds in the best model.
    3. May have to train them for more than 25 epochs.
- Split problem into 2 parts: *(Test Further)*
    1. Classification: (1-10): 1, (11-20): 2, (21-30): 3 .....
    2. Regression: (0 - 9) for each class
- Perform one hot encoding on the targets and perform classification.
- Train using augmented features.
    1. Pass (F, AF) as a single input. Sum and then backward pass the losses.
    2. Concatenate (F, AF) to effectively *n* times the amount of data.
        1. Repeat for various seeds.
        2. Concatenate various seeds.
- Create heavily augmented features.
- Test features without AAP.

<br/>