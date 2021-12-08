import os
from glob import glob

files = glob("./text/**/*.txt")
word_list = []
count = 0

for file_path in files:
    word_list = list()
    file = open(file_path, encoding="utf-8")
    text = file.readlines()

    for word in text:
        if "<START>" in word:
            word_list.append(word)
            count = 1
        elif "<END>" in word:
            count -= 1
            word_list.append(word)
        elif "##" in word:
            pass
        elif count == 1:
            word_list.append(word)

    output_file = os.path.splitext(os.path.basename(file_path))
    output_dir = os.path.basename(os.path.dirname(file_path))
    formatted_text = "./formatted_text/{}/{}.txt".format(output_dir, output_file[0])
    with open(formatted_text, "w", encoding="utf-8") as f:
        f.writelines(word_list)

    file.close
