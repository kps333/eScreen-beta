#!/bin/bash

micromamba env create -n eScreen -f escreen.yaml -y
micromamba activate eScreen
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
micromamba install -c nvidia cuda-nvcc cuda-cudart-dev -y
InstallFlashAttentionDirectly(){
    MAX_JOBS=4 pip install flash-attn==2.7.3 --no-build-isolation
}
InstallFlashAttentionBinary(){
    wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.6cxx11abiTRUE-cp310-cp310-linux_x86_64.whl
    pip install flash_attn-2.7.3+cu11torch2.6cxx11abiTRUE-cp310-cp310-linux_x86_64.whl
}
InstallFlashAttentionDirectly || InstallFlashAttentionBinary
git clone https://github.com/HazyResearch/flash-fft-conv.git
cd flash-fft-conv
cd csrc/flashfftconv
python setup.py install
cd ../..
python setup.py install
python -m ipykernel install --user --name eScreen