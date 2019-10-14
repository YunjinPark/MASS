import os
# import kss
from transformers import BasicTokenizer

dir_path = '/media/pipaek/wdusb/data/cleaned'
target_file_train = 'data/raw_korean_corpus.train.txt'
target_file_valid = 'data/raw_korean_corpus.valid.txt'
target_file_test  = 'data/raw_korean_corpus.test.txt'

tokenizer = BasicTokenizer()

def one_text_proc(file_path):

    with open(file_path) as data_file:
        with open(target_file_train, mode='a') as target_train:
            with open(target_file_valid, mode='a') as target_valid:
                with open(target_file_test, mode='a') as target_test:
                    doc_count = 0
                    doc_start = False
                    line_feed_count = 0
                    target = target_train

                    for i, line in enumerate(data_file):
                        if i % 10000 == 0:
                            print('line %d OK..' % i)

                        if line == '\n':
                            line_feed_count += 1
                            if doc_start:
                                if line_feed_count > 1: # \n\n을 만났다..
                                    doc_start = False
                                    target.write('\n\n')
                            else:
                                continue
                        else:
                            line_feed_count = 0
                            if not doc_start:
                                doc_start = True
                                doc_count += 1
                                if doc_count % 3000 == 1:
                                    target = target_valid
                                    # print('doc %d, target_valid' % doc_count)
                                elif doc_count % 3000 == 2:
                                    target = target_test
                                    # print('doc %d, target_test' % doc_count)
                                else:
                                    target = target_train
                                    # print('doc %d, target_train' % doc_count)


                            line =  " ".join(tokenizer.tokenize(line))
                            target.write(line)
                            target.write('\n')
                        # lines = kss.split_sentences(line)  # 문장 나누기
                        # for l in lines:
                        #     target.write(l)
                        #     target.write('\n')


file_list = os.listdir(dir_path)
file_list.sort()

print(file_list)
for file in file_list:
    file_path = os.path.join(dir_path, file)
    print(file_path)
    one_text_proc(file_path)