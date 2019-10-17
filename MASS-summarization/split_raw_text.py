import os
from multiprocessing import Pool
# from transformers import BasicTokenizer
from util.lang_util import filter_str_by_chartype

dir_path = '/media/pipaek/wdusb/data/cleaned'
# target_dir = '/media/pipaek/wdusb/data/mass-raw'
target_dir = '/media/pipaek/wdusb/data/mass-raw-nosplit-charex'
target_file_format = '%s-%06d.txt'
# tokenizer = BasicTokenizer()  # 얘가 쓸데없는 캐릭터를 많이 없애준다는 사실을 몰랐네..

def write_one_output(datafile_handle, target_file_path, max_doc_count=100):
    bContinue = True
    doc_count = 0
    doc_start = False
    line_feed_count = 0

    with open(target_file_path, mode='w') as target:

        while True:
            # read a single line
            line = datafile_handle.readline()
            if not line:  # EOF
                bContinue = False
                break

            if line == '\n':
                line_feed_count += 1
                if doc_start:
                    target.write('\n')
                    if line_feed_count > 1:  # \n\n을 만났다..
                        doc_start = False
                        target.write('\n')   # \n\n을 만들어 주자..
                        if doc_count >= max_doc_count:
                            break   # max_doc_count 만큼의 파일을 썼다. 이 함수를 리턴하자..
                else:
                    continue
            else:
                line_feed_count = 0
                if not doc_start:
                    doc_start = True
                    doc_count += 1
                # line = " ".join(tokenizer.tokenize(line))
                line = filter_str_by_chartype(line)
                target.write(line)
                target.write('\n')  # tokenizer를 안쓰면 \n은 필요없다..

    return bContinue


def one_text_proc(params):
    dir_path, file, max_doc_count = params
    bContinue = True
    with open(os.path.join(dir_path, file), 'r') as data_file:
        data_file_name = file.split('.')[0]
        file_count = 0
        while bContinue:
            target_file = target_file_format % (data_file_name, file_count)
            target_file_path = os.path.join(target_dir, target_file)
            bContinue = write_one_output(data_file, target_file_path, max_doc_count)
            file_count += 1
            # print(file_count)
        print('END : ', target_file)



def run_multi_proc(file_list, data_dir):
  pool = Pool(len(file_list))
  try:
    pool.map_async(one_text_proc, [(data_dir, file, 1000)
                               for file in file_list]).get(999999999)
    pool.close()
    pool.join()
  except KeyboardInterrupt:
    pool.terminate()
    pool.join()
    raise



if __name__ == "__main__":
    file_list = os.listdir(dir_path)
    file_list.sort()
    print(file_list)
    run_multi_proc(file_list, dir_path)