import os
import re
from glob import glob
import MeCab

word_list = {}
list_output = []
all_words = 0

# file_path = input("input file path: ")
files = glob("./formatted_text/**/*.txt")


def word_count(word):
    global all_words
    if word in word_list:
        word_list[word] += 1
        all_words += 1
    else:
        word_list.setdefault(word, 1)
        all_words += 1
    return word_list, all_words


for file_path in files:
    word_list.clear()
    list_output = list()
    all_words = 0
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        text = re.sub(r"[0-9]+", "", text)
        text = text.replace(":", " ")
        text = text.replace("<START>", " ")
        text = text.replace("<SW>", " ")
        text = text.replace("<END>", " ")
        text = text.replace("\n", " ")

        mecab = MeCab.Tagger("-Owakati")
        mecab.parse(" ")
        node = mecab.parseToNode(text)

        while node:
            if node.feature.split(",")[0] == "名詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "動詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "形容詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "形容動詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "副詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "連体詞":
                word = node.surface
                word_count(word)
            elif node.feature.split(",")[0] == "感動詞":
                word = node.surface
                word_count(word)
            else:
                pass
            node = node.next

        for i in word_list.items():
            list_output.append(i)
        list_output = sorted(list_output, key=lambda x: x[1], reverse=True)

        # print(list_output)
        # print(word_list)
        # print(all_words)
        output_file = os.path.splitext(os.path.basename(file_path))
        output_dir = os.path.basename(os.path.dirname(file_path))
        counted_file = "./count_word/{}/{}.txt".format(
            output_dir, output_file[0])
        with open(counted_file, "w", encoding="utf-8") as fw:
            fw.write("total number of words is {}\n".format(str(all_words)))
            fw.write("number of word types is {}\n".format(
                str(len(list_output))))
            for i in list_output:
                fw.write("{}\n".format(str(i)))
