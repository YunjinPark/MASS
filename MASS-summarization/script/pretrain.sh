#!/usr/bin/env bash

cd ..
BASEDIR=$(pwd)
echo $BASEDIR
echo '>>>> Start MASS Pretraining...'

VOCAB_FILE=mass_kor_32k.vocab


TOKENS_PER_SAMPLE=512
WARMUP_UPDATES=10000
PEAK_LR=0.0005
TOTAL_UPDATES=125000
MAX_SENTENCES=8
UPDATE_FREQ=16

fairseq-train processed \
    --user-dir mass --task masked_s2s --arch transformer_mass_base \
    --sample-break-mode none \
    --tokens-per-sample $TOKENS_PER_SAMPLE \
    --criterion masked_lm \
    --optimizer adam --adam-betas '(0.9, 0.98)' --adam-eps 1e-6 --clip-norm 0.0 \
    --lr-scheduler polynomial_decay --lr $PEAK_LR --warmup-updates $WARMUP_UPDATES --total-num-update $TOTAL_UPDATES \
    --dropout 0.1 --attention-dropout 0.1 --weight-decay 0.01 \
    --max-sentences $MAX_SENTENCES --update-freq $UPDATE_FREQ \
    --ddp-backend=no_c10d