from glob import glob

files = glob('./tag_cleared_text/**/*.txt')
word_list = []
count = 0

post_text = './merged_text2.txt'
with open(post_text, 'w', encoding='utf-8') as f:
    for file_name in files:
        file = open(file_name, encoding='utf-8')
        text = file.readlines()

        """
        for word in text:
            if '<START>' in word:
                word_list.append(word)
                count = 1
                print(count)
            elif '<END>' in word:
                count -= 1
                word_list.append(word)
                print("test")
            elif count == 1:
                word_list.append(word)
        """
        f.writelines(text)
