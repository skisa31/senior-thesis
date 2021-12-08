import os
import re
from glob import glob

files = glob('./formatted_text/**/*.txt')

for file_path in files:
    with open(file_path, encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r'[0-9]+', '', text)
        text = text.replace(':', '')
        text = text.replace('<START>\n', '')
        text = text.replace('<SW>\n', '')
        text = text.replace('<END>\n', '')
        text = text.replace('<END>\n', '')

        output_file = os.path.splitext(os.path.basename(file_path))
        output_dir = os.path.basename(os.path.dirname(file_path))
        clear_tag_file = './tag_cleared_text/{}/{}.txt'.format(output_dir, output_file[0])
        with open(clear_tag_file, 'w', encoding='utf-8') as fw:
            fw.write(text)
