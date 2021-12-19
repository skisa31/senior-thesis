import opensmile
from opensmile.core.define import FeatureSet
from glob import glob
import os


def open_smile(audio_file, cnt):
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv01b,
        feature_level=opensmile.FeatureLevel.Functionals,
    )
    output_features = smile.process_file(audio_file)
    print(output_features)
    file_name = os.path.splitext(os.path.basename(audio_file))
    user_name = os.path.basename(os.path.dirname(os.path.dirname(audio_file)))
    condition = os.path.basename(os.path.dirname(audio_file))
    output_path = "./result/opensmile/{}/{}/{}.csv".format(
        user_name, condition, file_name[0]
    )
    output_features.to_csv(output_path)
    output_all = "./result/opensmile/result_all.csv"
    output_con1 = "./result/opensmile/{}/result_condition1.csv".format(user_name)
    output_con2 = "./result/opensmile/{}/result_condition2.csv".format(user_name)
    output_con3 = "./result/opensmile/{}/result_condition3.csv".format(user_name)
    output_con4 = "./result/opensmile/{}/result_condition4.csv".format(user_name)
    if cnt == 1:
         output_features.to_csv(output_all)
    else:
        output_features.to_csv(output_all, mode="a", header=False)
    if condition == "condition1":
        output_features.to_csv(output_con1, mode="a", header=False)
    elif condition == "condition2":
        output_features.to_csv(output_con2, mode="a", header=False)
    elif condition == "condition3":
        output_features.to_csv(output_con3, mode="a", header=False)
    elif condition == "condition4":
        output_features.to_csv(output_con4, mode="a", header=False)


audio = glob("../voice/**/**/*.wav")
cnt = 0
for audio_file in audio:
    print(audio_file)
    cnt += 1
    open_smile(audio_file, cnt)
    print(cnt)
