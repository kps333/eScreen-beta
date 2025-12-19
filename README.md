# eScreen-beta
A sequence-sensitive model built upon the Striped Hyena2 architecture.<br>This repository contains the official implementation of the model described in our paper:<br>Decoding the functional regulatory syntax at single-nucleotide resolution through deep learning and genome-scale perturbation
## Table of Contents
- [eScreen](#eScreen-beta)
  - [Table of Contents](#table-of-contents)
  - [Tutorials](#tutorials)
  - [Data](#data)
  - [Installation](#installation)
  - [Model Architecture](#model-architecture)
  - [Command line interface](#command-line-interface)
  - [License](#license)
  - [Citation](#citation)
  - [Contact](#contact)
## Tutorials

## Data

## Installation
```bash
git clone https://github.com/kps333/eScreen-beta.git
cd eScreen-beta

bash setup.sh
conda activate eScreen
pip install .
```

## Model Architecture

eScreen is a sequence-sensitive model built upon the Striped Hyena2 architecture, integrating:  

  ▶ Short- and long-range convolution layers for multi-scale regulatory feature extraction  

  ▶ An optional graph neural network (GNN) module that incorporates epigenetic context  
  
## Command line interface

## License

This project is licensed under the MIT License.

## Citation

If you use eScreen in your research, please cite our paper:

Decoding the functional regulatory syntax at single-nucleotide resolution through deep learning and genome-scale perturbation

## Contact

For questions or support, please open an issue or contact us. Please don't hesitate to contact us if you have any questions or suggestions about eScreen:
<br>[21620241153548@stu.xmu.edu.cn](mailto:21620241153548@stu.xmu.edu.cn).
<br>[sluo112211@163.com](mailto:sluo112211@163.com).
