# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from collections import Counter
from multiprocessing import Pool
import os

import torch

from fairseq.tokenizer import tokenize_line
from fairseq.binarizer import safe_readline
from fairseq.data import data_utils, Dictionary


class BertDictionary(Dictionary):
    """A mapping from symbols to consecutive integers"""

    def __init__(
        self,
        pad='<pad>',
        eos='</s>',
        unk='<unk>',
        bos='<s>',
        extra_special_symbols=None,
    ):
        super().__init__(pad, eos, unk, bos, extra_special_symbols)

    @classmethod
    def load_from_file(cls, filename):
        d = cls()
        d.symbols = []
        d.count = []
        d.indices = {}

        with open(filename, 'r', encoding='utf-8', errors='ignore') as input_file:
            for line in input_file:
                k, v = line.split()
                # 여기서 k에 포함된 _를 ##로 바꿔주자..
                # k = k.replace("▁", "##") # 이건 삽질이었다. 여기서 바꿔주면 안된다.
                d.add_symbol(k)
                # print(k)

        d.unk_word = '[UNK]'
        d.pad_word = '[PAD]'
        d.eos_word = '[SEP]'
        d.bos_word = '[CLS]'

        d.bos_index = d.add_symbol('[CLS]')
        d.pad_index = d.add_symbol('[PAD]')
        d.eos_index = d.add_symbol('[SEP]')
        d.unk_index = d.add_symbol('[UNK]')

        d.nspecial = 999

        # for k, v in d.indices.items():
        #     print(k)

        return d

    def save(self, f):
        """Stores dictionary into a text file"""
        ex_keys, ex_vals = self._get_meta()
        self._save(f, zip(ex_keys + self.symbols, ex_vals + self.count))

# # filename = '/media/pipaek/wdusb/data/transformer-lm/korean-bulk/sp-model.vocab'
# filename = './../mass_kor_32k.vocab'
# d = BertDictionary.load_from_file(filename)
# # sss = d.encode_line('인간은 반드시 배신한다. 그 상황에서 할 수 있는 것이 배신밖에 없으므로 배신한다. ')
# line = '인간은 반드시 배신한다. 그 상황에서 할 수 있는 것이 배신밖에 없으므로 배신한다. '
# tokens = d.encode_line(
#                     line, add_if_not_exist=False,
#                     append_eos=True, reverse_order=False,
#                 ).long()
# print(tokens)
# for token in tokens:
#     print(d[token])
#
