#!/usr/bin/env bash

RAW_CORPUS_FILE_PATH=data/raw_korean_corpus.txt
MODEL_PREFIX=mass_kor_32k
VOCAB_SIZE=32000
MAX_SENTENCE=100000000

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
echo '>>>> Start Building SPM Model...'

python build_tokenizer.py \
  --input=$RAW_CORPUS_FILE_PATH \
  --model_prefix=$MODEL_PREFIX \
  --vocab_size=$VOCAB_SIZE \
  --mining_sentence_size=$MAX_SENTENCE

echo '>>>> Building SPM Model Finished..'
