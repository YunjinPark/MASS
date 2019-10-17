import os, shutil
from multiprocessing import Pool
# from transformers import BasicTokenizer

# dir_path = '/media/pipaek/wdusb/data/cleaned'
# source_dir = '/media/pipaek/wdusb/data/mass-raw'
# target_dir = '/media/pipaek/wdusb/data/bpe'
source_dir = '/media/pipaek/wdusb/data/mass-raw-nosplit-charex'
target_dir = '/media/pipaek/wdusb/data/bpe-nosplit-charex'
# target_file_format = '%s-%06d.txt'
# tokenizer = BasicTokenizer()

# def write_one_output(datafile_handle, target_file_path, max_doc_count=100):
#     bContinue = True
#     doc_count = 0
#     doc_start = False
#     line_feed_count = 0

def get_files(startpattern):
    file_names = [fn for fn in os.listdir(source_dir)
                  if fn.startswith(startpattern)]
    return file_names

def get_files_with_index(startpattern, index_quotient, index_modulo):
    file_names = get_files(startpattern)


    file_names = [fn  for fn in file_names
                  if int(fn.split('.')[0].split('-')[1]) % index_quotient == index_modulo]
    # file_names = [int(fn.split('.')[0].split('-')[1]) % index_quotient for fn in file_names]
    return file_names

def copy_files_to_dir(files, source_dir, target_dir):
    for file in files:
        source_path = os.path.join(source_dir, file)
        target_path = os.path.join(target_dir, file)
        shutil.copy(source_path, target_path)
        print(target_path)


copy_files_to_dir(get_files_with_index('namuwiki_20190312', 5, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('naver_corpus_flat', 1, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_IT과학', 2, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_경제', 7, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_사회', 10, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_생활문화', 2, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_세계', 5, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('navernews_정치', 7, 0), source_dir, target_dir)
copy_files_to_dir(get_files_with_index('watcha_corpus_flat', 1, 0), source_dir, target_dir)

# str = "this is string example....wow!!!"
# print (str.startswith( 'this' ))

# files = get_files_with_index(startpattern, index_quotient, index_modulo)


# files = get_files('namu')
# print(files)
# print(len(files))
# files = get_files_with_index('namu', 7, 1)
# print(files)
# print(len(files))