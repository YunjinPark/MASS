#!/usr/bin/env bash

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
echo '>>>> Start MASS Preprocessing...'

VOCAB_FILE=mass_kor_32k.vocab

mkdir -p processed

# pipaek :여기서 체크로직 넣어서 전처리 끝났는데 또 돌리는 삽질을 하지 말아야 한다...

fairseq-preprocess \
    --user-dir mass --only-source --task masked_s2s \
    --trainpref mono/train.txt --validpref mono/valid.txt --testpref mono/test.txt \
    --destdir processed --srcdict $VOCAB_FILE --workers 30
