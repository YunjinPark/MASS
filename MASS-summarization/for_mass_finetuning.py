'''
gen, art 를
src(시놉시스)-tgt(평가1개) pair 들로 만들어주는 코드
'''
import os
import json
import time
from collections import defaultdict

#raw_dir = r'/home/yun/mass/MASS/MASS-summarization/data/movie/raw/gen'
#pair_dir = r'/home/yun/mass/MASS/MASS-summarization/data/movie/raw_pair_gen'
#files = ['gen_high', 'gen_mid', 'gen_low']


raw_dir = r'/home/yun/mass/MASS/MASS-summarization/data/movie/raw/art'
pair_dir = r'/home/yun/mass/MASS/MASS-summarization/data/movie/raw_pair_art'
files = ['art_high', 'art_mid', 'art_low']

#print(os.path.dirname( os.path.abspath( __file__ ) ))

def save_syn_comm(tvt, filename, syn, comm):
    with open(os.path.join(pair_dir, tvt, filename + '.src'), 'w', encoding = "utf-8") as f1:
        f1.write(syn)
    with open(os.path.join(pair_dir, tvt, filename + '.tgt'), 'w', encoding = "utf-8") as f2:
        f2.write(comm)

def replace_(st):
    st = st.replace('\\', '')
    st = st.replace('?', '')
    st = st.replace('/', '')
    st = st.replace('*', '')
    st = st.replace('"', '')
    st = st.replace('<', '')
    st = st.replace('>', '')
    st = st.replace('|', '')
    st = st.replace(':', '')
    return st

dic_train, dic_valid, dic_test = defaultdict(int), defaultdict(int), defaultdict(int)

for file in files:
    if file == "art_high": flag = '우호 [SEP] '
    if file == "art_mid": flag = '중립 [SEP] '
    if file == "art_low": flag = '적대 [SEP] '
    #if file == "gen_high": flag = '우호 [SEP] '
    #if file == "gen_mid": flag = '중립 [SEP] '
    #if file == "gen_low": flag = '적대 [SEP] '
    with open(os.path.join(raw_dir, file+'.json')) as json_file:
        data = json.load(json_file)
    print(file, ":", len(data.keys()))

    for i, key in enumerate(data.keys()):
        time.sleep(0.5)
        title = replace_(key)
        syn = data[key]['synop']
        tmp = i % 50

        #tvt: train/ valid/ test set 나누기
        if tmp == 0:
            tvt = 'valid'
            num = dic_valid[key]
        elif tmp == 1:
            tvt = 'test'
            num = dic_test[key]
        else:
            tvt = 'train'
            num = dic_test[key]

        if 'naver' in data[key]:
            for nav in data[key]['naver']:
                save_syn_comm(tvt, title + "_" + '{0:04d}'.format(num), syn, flag + nav)
                num += 1
        if 'watcha' in data[key]:
            for wat in data[key]['watcha']:
                save_syn_comm(tvt, title + "_" + '{0:04d}'.format(num), syn, flag + wat)
                num += 1
        if tmp == 0:
            dic_valid[key] = num
        elif tmp == 1:
            dic_test[key] = num
        else:
            dic_test[key] = num

        if i % 100 == 0:
            time.sleep(2)
            print(file, str(i)+'번째')
    time.sleep(3)
