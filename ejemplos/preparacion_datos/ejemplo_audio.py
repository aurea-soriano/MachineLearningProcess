#bibliotecas operar con sonido

import librosa
import wavio
from pydub import AudioSegment
from pydub.playback import play


import matplotlib.pyplot as plt

#perros ladrando
audio_file = "../../datasets/audio/UrbanSound Dataset sample/audio/100032-3-0-0.wav"
song = AudioSegment.from_wav(audio_file)
play(song)

wav = wavio.read(audio_file)
plt.figure(figsize=(12,4))
plt.title("Perros ladrando")
plt.plot(wav.data[:,0])
plt.show()


#librosa -> mfccs, melspectrogram, chroma_stf
