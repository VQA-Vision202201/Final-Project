# Multimodal Fusion Model for VQA
This is our implementation for the Visual Question Answering task. We focused on feature fusion by implementing multimodal blocks and keeping an attention strategy. 

## Table of Contents
0. [Installation](#Installation)

### Installation
- First, clone this repo
```bash
git clone https://github.com/VQA-Vision202201/Final-Project.git
cd Final-Project
```

- Create a conda virtual environment and activate it
```bash
conda create -n vqa python=3.7 -y
conda activate vqa
```

- Install `Pytorch==1.7.1` and `torchvision==0.8.2` with `CUDA==10.1`:
```bash
conda install pytorch==1.7.1 torchvision==0.8.2 cudatoolkit=10.1 -c pytorch
```

- Install all python dependencies:
```bash
pip install -r requirements.txt
```

- Make the softlink to obtain the dataset images
```bash
ln -s /media/SSD0/naparicio/Vision/pytorch-vqa/mscoco .
```

- Make the softlink to obtain the features
```bash
ln -s /media/SSD0/daruiz/Transformers-VQA/data .
```

- Copy our best model
```bash
ln -s /media/SSD0/daruiz/Transformers-VQA/models/trained models
```

- Run the following line to test our model
```bash
python main.py --test minival 
```

- Run the following line to prove our demo
```bash
python main.py --test demo 
```
