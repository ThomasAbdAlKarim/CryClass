import tensorflow as tf
import numpy as np
import librosa

Model = tf.keras.models.load_model('Model72.h5')


def Trim(Signal,Sr,Len = 5):
    Signal = np.array(Signal[:(Len*Sr)])
    return Signal



def Pad(Signal,Len,Sr = 22050):
    if len(Signal) < (Len*Sr):
        Pad_Size = (Len*Sr)-len(Signal)
        Padded = np.pad(Signal, (0,Pad_Size ), 'constant')
        return Padded
    return Signal



def Save_MFCC(Signal,Sr,n_mfcc=13,n_fft=2048,hop_length=512):
    MFCC = librosa.feature.mfcc(Signal,sr=Sr,n_fft=n_fft,hop_length = hop_length,n_mfcc=n_mfcc)
    return MFCC/303.0

def Pred(Audio):
    Input = []
    Input.append(Audio)
    Input = np.array(Input)
    return Model.predict(Input)*100





