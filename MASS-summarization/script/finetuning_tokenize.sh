#!/usr/bin/env bash

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
echo '>>>> Start Tokenizing Raw Corpus...'

#DATA_DIR=/media/pipaek/wdusb/data/mass-raw-nosplit-charex
#raw_pair_gen

DATA_DIR=/home/yun/data/kisdi/movie/temp
OUTPUT_DIR=/home/yun/data/kisdi/movie/tokenized_gen/

for SPLIT in train valid test; do
  for file in ${DATA_DIR}/${SPLIT}/*; do
    python encode.py \
        --inputs ${DATA_DIR}/${SPLIT}/${file} \
        --outputs ${OUTPUT_DIR}/${SPLIT}/${file} \
        --workers 10; \
  done
done
