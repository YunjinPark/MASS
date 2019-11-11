#!/usr/bin/env bash

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
#echo '>>>> Start MASS Preprocessing...'

VOCAB_FILE=mass_kor_32k.vocab
PREPROCESS_TARGET_DIR=processed

mkdir -p $PREPROCESS_TARGET_DIR

# pipaek :여기서 체크로직 넣어서 전처리 끝났는데 또 돌리는 삽질을 하지 말아야 한다...
FILECNT=$(ls $PREPROCESS_TARGET_DIR | wc -l)

if [ $FILECNT = 0 ] ; then
    echo '>>>> Start MASS fairseq-preprocess.'

    fairseq-preprocess \
        --user-dir mass --only-source --task masked_s2s \
        --trainpref mono/train.txt --validpref mono/valid.txt --testpref mono/test.txt \
        --destdir $PREPROCESS_TARGET_DIR --srcdict $VOCAB_FILE --workers 30
    echo '>>>> End MASS fairseq-preprocess.'
else
    echo '>>>> Preprocessed files are already exist in target dir. Check and try fairseq-preprocess again.'
fi