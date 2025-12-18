#!/bin/bash

conda env create -n eScreen -f escreen.yaml
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
conda install -c nvidia cuda-nvcc cuda-cudart-dev
MAX_JOBS=4 pip install flash-attn==2.7.3 --no-build-isolation
git clone https://github.com/HazyResearch/flash-fft-conv.git
cd flash-fft-conv
cd csrc/flashfftconv
python setup.py install
cd ../..
python setup.py install