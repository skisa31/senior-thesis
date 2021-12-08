import wave
import struct
from scipy import fromstring, int16
import numpy as np
import os
import math
from glob import glob


def cut_wav(audio_file):
    wav_file = wave.open(audio_file)
    cor_file = os.path.splitext(os.path.basename(audio_file))
    cor_dir = os.path.basename(os.path.dirname(audio_file))
    time = "./voice/{}/cut_time/{}.txt".format(cor_dir, cor_file[0])
    time_file = open(time)

    ch = wav_file.getnchannels()
    width = wav_file.getsampwidth()
    fr = wav_file.getframerate()
    times = time_file.readlines()
    for i, n in enumerate(times):
        times[i] = int(n.replace("\n", ""))
    print(times)
    frames = []
    for i in times:
        frames.append(int(ch * fr * i))
    print(frames)
    num_cut = len(times)
    print(num_cut)

    data = wav_file.readframes(wav_file.getnframes())
    wav_file.close()
    X = np.frombuffer(data, dtype="int16")

    for i in range(num_cut):
        if i < 10:
            output_file_path = os.path.splitext(os.path.basename(audio_file))
            output_dir_path = os.path.dirname(audio_file)
            output_file = (
                "{}/{}/".format(output_dir_path, output_file_path[0])
                + "c0"
                + str(i)
                + ".wav"
            )
        else:
            output_file_path = os.path.splitext(os.path.basename(audio_file))
            output_dir_path = os.path.dirname(audio_file)
            output_file = (
                "{}/{}/".format(output_dir_path, output_file_path[0])
                + "c"
                + str(i)
                + ".wav"
            )
        if i <= num_cut - 2:
            start_cut = int(frames[i])
            print(start_cut)
            end_cut = int(frames[i + 1])
            print(end_cut)
            Y = X[start_cut:end_cut]
            outd = struct.pack("h" * len(Y), *Y)
            ww = wave.open(output_file, "w")
            ww.setnchannels(ch)
            ww.setsampwidth(width)
            ww.setframerate(fr)
            ww.writeframes(outd)
            ww.close()
        else:
            pass


def equal_div(audio_file, time):

    # ファイルを読み出し
    wr = wave.open(audio_file, "r")

    # waveファイルが持つ性質を取得
    ch = wr.getnchannels()
    width = wr.getsampwidth()
    fr = wr.getframerate()
    fn = wr.getnframes()
    total_time = 1.0 * fn / fr
    integer = math.floor(total_time)  # 小数点以下切り捨て
    t = int(time)  # 秒数[sec]
    frames = int(ch * fr * t)
    num_cut = int(integer // t)

    print("Total time: ", total_time)
    print("Total time(integer)", integer)
    print("Time: ", t)
    print("Frames: ", frames)
    print("Number of cut: ", num_cut)

    # waveの実データを取得し、数値化
    data = wr.readframes(wr.getnframes())
    wr.close()
    X = fromstring(data, dtype=int16)
    print(X)

    for i in range(num_cut):
        print(i)
        # 出力データを生成
        if i < 10:
            output_file_path = os.path.splitext(os.path.basename(audio_file))
            output_dir_path = os.path.dirname(audio_file)
            output_file = (
                "{}/{}".format(output_dir_path, output_file_path[0])
                + "_0"
                + str(i)
                + ".wav"
            )
            print(output_file)
        else:
            output_file_path = os.path.splitext(os.path.basename(audio_file))
            output_dir_path = os.path.dirname(audio_file)
            output_file = (
                "{}/{}".format(output_dir_path, output_file_path[0])
                + "_"
                + str(i)
                + ".wav"
            )
            print(output_file)
        start_cut = i * frames
        end_cut = i * frames + frames
        print(start_cut)
        print(end_cut)
        Y = X[start_cut:end_cut]
        outd = struct.pack("h" * len(Y), *Y)

        # 書き出し
        ww = wave.open(output_file, "w")
        ww.setnchannels(ch)
        ww.setsampwidth(width)
        ww.setframerate(fr)
        ww.writeframes(outd)
        ww.close()


"""
audio = glob("./voice/**/*.wav")
cnt = 0

for audio_file in audio:
    cnt += 1
    cut_wav(audio_file)
    print(cnt)
"""

audio = input("input target path: ")
cut_time = input("input cut time: ")
equal_div(audio, cut_time)
