# CryClass
This is a baby cry classifier, it classify a cry into 3 categories:

- Pain
- Hunger
- discomfort

The Model
---------------
The data come from donateacry-corpus, Chillanto Database, youtube videos and personaly collected but after some tests we found out that the size of the dataset was too small so we used reverb to do data augmentation wich gave us pretty good results

all the audios are highpassed and trimmed to 5 seconds or padded if needed then we pass its MFCC to the model after normalizing its value by dividing it by 303.
we are using a 90% 10% split to train and test the neural network that uses convolution and dense layers

The Webapp
---------------
The webapp isn't too advanced, it just give a ui to use the model in a more user frienly way, it lets you record your audio then send it to the model to predict its categorie then display the result with a picture and the confidence of the prediction on top of it

   ![Result Page](https://i.ibb.co/pRsSWsS/Uncom.png)
