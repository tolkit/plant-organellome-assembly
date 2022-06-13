#!/usr/bin/env bash

# run the full pipeline on raw reads.

# I have gfatk, MBG, fppa, fpma in my $PATH
# I need to point to nhmmer, and both sets of hmms

FPMA_ANGIOSPERM_HMMS="/software/team301/fpma/hmms/angiosperm_hmms"
FPPA_ANGIOSPERM_HMMS="/software/team301/fppa/hmms/Magnoliopsida/"
NHMMER="/software/team301/hmmer-3.3.2/bin/nhmmer"

# some test data
TEST_DATA="./data/fa_gz/Ailanthus_altissima.fa.gz"

# now we can run the pipeline
# where possible, I am using default params

python3 pmpap.py \
    --organelle "mitochondria" \
    --annotation "mitochondria" \
    --nhmmer $NHMMER \
    --fpma-hmms $FPMA_ANGIOSPERM_HMMS \
    --fppa-hmms $FPPA_ANGIOSPERM_HMMS \
    $TEST_DATA
