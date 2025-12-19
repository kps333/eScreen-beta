#!/bin/bash

# 创建环境
micromamba env create -n eScreen -f escreen.yaml -y

# 使用 source 激活环境（确保在当前shell中生效）
source $(micromamba shell hook -s bash)
micromamba activate eScreen

# 安装基础包
pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118
micromamba install -c nvidia cuda-nvcc cuda-cudart-dev -y

# 定义安装函数（在同一环境中执行）
install_flash_attention() {
    # 尝试直接编译安装
    MAX_JOBS=4 pip install flash-attn==2.7.3 --no-build-isolation && return 0
    
    # 如果失败，尝试二进制安装
    echo "编译安装失败，尝试二进制安装..."
    wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.6cxx11abiTRUE-cp310-cp310-linux_x86_64.whl
    pip install flash_attn-2.7.3+cu11torch2.6cxx11abiTRUE-cp310-cp310-linux_x86_64.whl
}

# 调用函数（在当前shell中执行）
install_flash_attention

# 安装flash-fft-conv
git clone https://github.com/HazyResearch/flash-fft-conv.git
cd flash-fft-conv
cd csrc/flashfftconv
python setup.py install
cd ../..
python setup.py install
cd ..

# 安装kernel
python -m ipykernel install --user --name eScreen