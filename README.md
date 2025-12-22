<p align="flex">
  <img src="https://github.com/kps333/eScreen-beta/blob/main/img/lab_logo.png" height="100" title="lab_logo">
  <img src="https://github.com/kps333/eScreen-beta/blob/main/img/eScreen_logo.png" height="100" title="project_logo">
</p>
# eScreen-beta
A sequence-sensitive model built upon the Striped Hyena2 architecture.<br>This repository contains the official implementation of the model described in our paper:<br>Decoding the functional regulatory syntax at single-nucleotide resolution through deep learning and genome-scale perturbation
<br>For more details read our manuscript.
<p align="center">
  <img src="https://github.com/kps333/eScreen-beta/blob/main/img/Schema.png" width="800" title="logo">
</p>

## Table of Contents
- [eScreen](#eScreen-beta)
  - [Table of Contents](#table-of-contents)
  - [Tutorials](#tutorials)
  - [Data](#data)
  - [Installation](#installation)
  - [Model Architecture](#model-architecture)
  - [License](#license)
  - [Citation](#citation)
  - [Contact](#contact)


## Tutorials
[Train & Evaluation] (https://github.com/kps333/eScreen-beta/blob/main/Tutorial/Demo.ipynb)<br>
[Analysis]

## Data
Preprocessed tutorial dataset is available at Google Drive：https://drive.google.com/file/d/1ggN4Go3H5X0QWF2RzxznTVIda0bQ3fgC/view?usp=drive_link

## Setup
### Requirements
We recommend using our packaged setup script to create suitable environment:
```bash
git clone https://github.com/kps333/eScreen-beta.git
cd eScreen-beta
bash setup.sh
conda activate eScreen
```
### Installation
Then, you can install eScreen with pip:
```bash
pip install -e .
```

## Model Architecture

eScreen is a sequence-sensitive model built upon the Striped Hyena2 architecture, integrating:  

  ☛ Short- and long-range convolution layers for multi-scale regulatory feature extraction  

  ☛ An optional graph neural network (GNN) module that incorporates epigenetic context  

## License

This project is licensed under the MIT License.

## Citation

If you use eScreen in your research, please cite our paper:

Decoding the functional regulatory syntax at single-nucleotide resolution through deep learning and genome-scale perturbation

## Contact

For questions or support, please open an issue or contact us. Please don't hesitate to contact us if you have any questions or suggestions about eScreen:
<br>[21620241153548@stu.xmu.edu.cn](mailto:21620241153548@stu.xmu.edu.cn).
<br>[sluo112211@163.com](mailto:sluo112211@163.com).
