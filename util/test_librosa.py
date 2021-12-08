import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ファイル読み込み
filename = "./voice/believe3/condition1.wav"
y, sr = librosa.load(filename)
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))
times = librosa.times_like(f0)

D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
fig, ax = plt.subplots()
img = librosa.display.specshow(D, x_axis='time', y_axis='log', ax=ax)
ax.set(title='pYIN fundamental frequency estimation')
fig.colorbar(img, ax=ax, format="%+2.f dB")
ax.plot(times, f0, label='f0', color='cyan', linewidth=3)
ax.legend(loc='upper right')

df_f0 = pd.Series(f0)
df_f0 = df_f0.dropna(how='all')
print(df_f0.describe())
