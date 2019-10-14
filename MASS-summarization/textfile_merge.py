import os

dir_path = '/media/pipaek/wdusb/data/cleaned'
target_file = 'data/raw_korean_corpus.txt'

def one_text_proc(file_path):
    with open(file_path) as data_file:
        with open(target_file, mode='a') as target:
            for i, line in enumerate(data_file):
                if i % 10000 == 0:
                    print('line %d OK..' % i)
                target.write(line)


file_list = os.listdir(dir_path)
file_list.sort()

print(file_list)
for file in file_list:
    file_path = os.path.join(dir_path, file)
    print(file_path)
    one_text_proc(file_path)