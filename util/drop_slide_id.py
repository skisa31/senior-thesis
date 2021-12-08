import os
from glob import glob

files = glob("./slidebar_log_data/*.txt")

date_list = []
id_list = []

for file_path in files:
    date_list = list()
    id_list = list()
    file = open(file_path, encoding="utf-8")
    text = file.readlines()
    output_file = os.path.splitext(os.path.basename(file_path))
    slide_id_path = "./slide_id/{}.txt".format(output_file[0])
    fw = open(slide_id_path, "w", encoding="utf-8")

    for line in text:
        log_list = line.split(" ")
        date = log_list[3]
        date = date.lstrip("[")
        print(date)
        ids = log_list[6]
        ids = ids.removeprefix("/photoslideshow/php/triggerreard.php?")
        print(ids)
        fw.write("date: {} , slide: {}\n".format(date, ids))

    fw.close
