import os
# import kss
# from transformers import BasicTokenizer

# dir_path = '/media/pipaek/wdusb/data/mass-raw-nosplit-charex'
# target_file_train = 'data/raw_korean_corpus.train.txt'
# target_file_valid = 'data/raw_korean_corpus.valid.txt'
# target_file_test  = 'data/raw_korean_corpus.test.txt'

def one_text_proc(file_path, target_path):

    with open(file_path) as data_file:
        with open(target_path, mode='a') as target:
            for i, line in enumerate(data_file):
                target.write(line)

def merge_dir_files(src_dir, target_path):
    file_list = os.listdir(src_dir)
    file_list.sort()

    print(file_list)
    for file in file_list:
        file_path = os.path.join(src_dir, file)
        print(file_path)
        one_text_proc(file_path, target_path)

merge_dir_files('/media/pipaek/wdusb/data/mass-raw-nosplit-charex/train',
                '/media/pipaek/wdusb/data/mass-raw-nosplit-charex/train/raw_korean_corpus.train.txt')
merge_dir_files('/media/pipaek/wdusb/data/mass-raw-nosplit-charex/valid',
                '/media/pipaek/wdusb/data/mass-raw-nosplit-charex/valid/raw_korean_corpus.valid.txt')
merge_dir_files('/media/pipaek/wdusb/data/mass-raw-nosplit-charex/test',
                '/media/pipaek/wdusb/data/mass-raw-nosplit-charex/test/raw_korean_corpus.test.txt')
# merge_dir_files(src_dir, target_path)
# merge_dir_files(src_dir, target_path)

