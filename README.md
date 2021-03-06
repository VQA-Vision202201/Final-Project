# What am I seeing? Visual Question Answering

This is our implementation for the Visual Question Answering task. We focused first on feature fusion by implementing multimodal blocks, but we observed that CNN and LSTM has many limitations. According to mentioned above, we suggest a Multimodal Transformer, keeping a remarkable attention strategy, for VQA.

![](./VQA_Examples.png)

Our main contribution is based on understanding and explaining the VQA problem as well as the limitations of the methods and possible future improvements. Additionally, we implement a state-of-the-art model that shows significant improvement over classical approaches in VQA2.0 dataset. Finally, we also suggest possible ethical considerations associated to VQA approach and task.

![](./baseline.png)
![](./fusion.png)
![](./uniter.png)

## Table of Contents
0. [Installation](#Installation)
1. [Data](#Data)
2. [Model](#Model)
3. [Test](#Test)
4. [Demo](#Demo)
5. [Acknowledgements](#Acknowledgements)

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
### Data
- Make the softlink to obtain the dataset images
```bash
ln -s /media/SSD0/naparicio/Vision/pytorch-vqa/mscoco .
```

- Make the softlink to obtain the features
```bash
ln -s /media/SSD0/daruiz/Transformers-VQA/data .
```

### Model
- Copy our best model
```bash
cp -r /media/SSD0/daruiz/Transformers-VQA/models .
```

### Test
- Run the following line to test our model
```bash
python main.py --test minival 
```

### Demo
- Run the following line to prove our demo. Afterwards, you will be able to visualize the power of VQA in "demo_pic.png"
```bash
python main.py --test demo 
```

### Acknowledgements
Both Multimodal Block Fusion and Transformers implementation were based on the links showed beyod:
- [BLOCK: Bilinear Superdiagonal Fusion for VQA and VRD](https://github.com/Cadene/block.bootstrap.pytorch)
- [LXMERT: Learning Cross-Modality Encoder Representations from Transformers](https://github.com/airsplay/lxmert)

