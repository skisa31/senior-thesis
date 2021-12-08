import librosa
import matplotlib.pyplot as plt
import numpy as np

# [path_to_your_file]にはみなさんの使用するファイルを指定してください。
y, sr = librosa.load('./voice/believe3/condition1.wav')

# フレームのズラす幅の指定
hop_length = 512

# フレームで切り出す回数
nms = ((y.shape[0])//hop_length)+1

# 最初と最後をフレームで切り出せるようにゼロパディング
y_bf = np.zeros(hop_length*2)
y_af = np.zeros(hop_length*2)
y_concat = np.concatenate([y_bf, y, y_af])

zero_cross_list = []
for j in range(nms):
  zero_cross = 0
  # フレームによる切り出し
  y_this = y_concat[j*512:j*512+2048]
  for i in range(y_this.shape[0]-1):
    # もし正負が変わったらという条件
    if (np.sign(y_this[i]) - np.sign(y_this[i+1]))!=0:
      zero_cross += 1
  zero_cross_list.append(zero_cross)

# 最大値が1になるように正規化
zero_cross_list = np.array(zero_cross_list)/max(zero_cross_list)

# 閾値は0.4に設定（ヒューリスティックですが…）
zero_cross_list = (zero_cross_list<0.4)*1

spec = librosa.stft(y, hop_length=512, n_fft=2048)
logmel_db = librosa.feature.melspectrogram(sr=sr, S=librosa.power_to_db(np.abs(spec)**2), n_mels=80)
plt.imshow(logmel_db, vmin=np.min(logmel_db), vmax=np.max(logmel_db), cmap="gist_heat", aspect= "auto", origin="lower")
plt.plot(np.arange(logmel_db.shape[1]), (zero_cross_list)*10)
plt.xlabel("Time_frame")
plt.ylabel("Frequency [Hz]")
