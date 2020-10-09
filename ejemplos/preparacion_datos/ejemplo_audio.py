import librosa
import wavio
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import pandas as pd
import os
from tqdm import tqdm

'''
Air Conditioner
Car Horn
Children Playing
Dog bark
Drilling
Engine Idling
Gun Shot
Jackhammer
Siren
Street Music

'''
# Class: Aire Acondicionado
filename = '../datasets/audio/UrbanSound Dataset sample/audio/100852-0-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Aire Acondicionado')
plt.plot(wav.data[:, 0])
#plt.show()


# Class: Bocina de carro

filename = '../datasets/audio/UrbanSound Dataset sample/audio/100648-1-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Bocina de Carro')
plt.plot(wav.data[:, 0])
#plt.show()



# Class: Ninos jugando

filename = '../datasets/audio/UrbanSound Dataset sample/audio/100263-2-0-117.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Ninos jugando')
plt.plot(wav.data[:, 0])
#plt.show()




# Class: Perros ladrando

filename = '../datasets/audio/UrbanSound Dataset sample/audio/100032-3-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Perros ladrando')
plt.plot(wav.data[:, 0])
#plt.show()


# Class: Perforacion

filename = '../datasets/audio/UrbanSound Dataset sample/audio/103199-4-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Perforacion')
plt.plot(wav.data[:, 0])
#plt.show()


# Class: Motor

filename = '../datasets/audio/UrbanSound Dataset sample/audio/102857-5-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Motor')
plt.plot(wav.data[:, 0])
#plt.show()



# Class: Disparos

filename = '../datasets/audio/UrbanSound Dataset sample/audio/102305-6-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Disparos')
plt.plot(wav.data[:, 0])
#plt.show()




# Class: Sirena

filename = '../datasets/audio/UrbanSound Dataset sample/audio/102853-8-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Sirena')
plt.plot(wav.data[:, 0])
#plt.show()


# Class: Musica de calle

filename = '../datasets/audio/UrbanSound Dataset sample/audio/101848-9-0-0.wav'
song = AudioSegment.from_wav(filename)
play(song)
wav = wavio.read(filename)
plt.figure(figsize=(12,4))
plt.title('Musica de calle')
plt.plot(wav.data[:, 0])
#plt.show()


import pandas as pd
metadata = pd.read_csv('../datasets/audio/UrbanSound Dataset sample/metadata/UrbanSound8K.csv')
print(metadata.head())

#cuenta los itens en cada folder
print(metadata["fold"].value_counts())


from librosa import display
import librosa
#conjunto de caracteristicas
#este es un archivo de ladrido de perro
y,sr=librosa.load('../datasets/audio/UrbanSound Dataset sample/audio/100032-3-0-0.wav')
mfccs = librosa.feature.mfcc(y, sr, n_mfcc=40)
melspectrogram =librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000)
chroma_stft=librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=40)
melspectrogram.shape,chroma_stft.shape,mfccs.shape



#MFCC of dog bark
import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
#plt.show()

#Melspectrogram of a dog bark
plt.figure(figsize=(10,4))
librosa.display.specshow(librosa.power_to_db(melspectrogram,ref=np.max),y_axis='mel', fmax=8000,x_axis='time')
plt.colorbar(format='%+2.0f dB')
plt.title('Mel spectrogram')
plt.tight_layout()
#plt.show()

#Chromagram of dog bark
plt.figure(figsize=(10,4))
librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time')
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
#plt.show()







#feature set
y,sr=librosa.load("../datasets/audio/UrbanSound Dataset sample/audio/100032-3-0-0.wav")
mfccs = np.mean(librosa.feature.mfcc(y, sr, n_mfcc=40).T,axis=0)
melspectrogram = np.mean(librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000).T,axis=0)
chroma_stft=np.mean(librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=40).T,axis=0)
melspectrogram.shape,chroma_stft.shape,mfccs.shape


#stacking and reshaping
features=np.reshape(np.vstack((mfccs,melspectrogram,chroma_stft)),(40,3))
features.shape

#preprocessing using entire feature set
x_train=[]
x_test=[]
y_train=[]
y_test=[]
path="UrbanSound8K/audio/fold"
for i in tqdm(range(len(metadata))):
    fold_no=str(metadata.iloc[i]["fold"])
    file=metadata.iloc[i]["slice_file_name"]
    label=metadata.iloc[i]["classID"]
    filename=path+fold_no+"/"+file
    y,sr=librosa.load(filename)
    mfccs = np.mean(librosa.feature.mfcc(y, sr, n_mfcc=40).T,axis=0)
    melspectrogram = np.mean(librosa.feature.melspectrogram(y=y, sr=sr, n_mels=40,fmax=8000).T,axis=0)
    chroma_stft=np.mean(librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=40).T,axis=0)
    features=np.reshape(np.vstack((mfccs,melspectrogram,chroma_stft)),(40,5))
    if(fold_no!='10'):
      x_train.append(features)
      y_train.append(label)
    else:
      x_test.append(features)
      y_test.append(label)
