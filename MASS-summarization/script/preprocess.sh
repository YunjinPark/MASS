#!/usr/bin/env bash

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
echo '>>>> Start MASS Preprocessing...'

VOCAB_FILE=mass_kor_32k.vocab

mkdir -p processed

fairseq-preprocess \
    --user-dir mass --only-source --task masked_s2s \
    --trainpref mono/train.txt --validpref mono/valid.txt --testpref mono/test.txt \
    --destdir processed --srcdict $VOCAB_FILE --workers 30
