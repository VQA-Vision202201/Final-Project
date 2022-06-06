import torch.backends.cudnn as cudnn
from torch.autograd import Variable
from data import get_loader
from model import Net
from tqdm import tqdm
from train import run
import argparse
import torch
import utils
import config
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='VQA')

parser.add_argument('--mode', type=str, default="demo", choices=["test", "demo"], 
                    help= "Evaluation mode")
parser.add_argument('-image', type=str, default="mscoco/val2014/000000262144.jpg", 
                    help= "Image file")
parser.add_argument('--seed', type=int, default=1, metavar='S',
                    help='random seed (default: 1)')
parser.add_argument('--no-cuda', action='store_true', default=False,
                    help='disables CUDA training')

args = parser.parse_args()

args.cuda = not args.no_cuda and torch.cuda.is_available()
torch.manual_seed(args.seed)
if args.cuda:
    torch.cuda.manual_seed(args.seed)
kwargs = {'num_workers': 0, 'pin_memory': True} if args.cuda else {}

train_loader = get_loader(train=True)
net = torch.nn.DataParallel(Net(train_loader.dataset.num_tokens)).cuda()
optimizer = torch.optim.Adam([p for p in net.parameters() if p.requires_grad])
tracker = utils.Tracker()

best_model = torch.load("logs/Block_Model.pth")
net = net.load_state_dict(best_model["weights"])
val_loader = get_loader(val=True)

if args.mode == "test":

    r = run(net, val_loader, optimizer, tracker, train=False, prefix='val', epoch=1)
    print('answers', r[0], 'accuracies', r[1], 'idx', r[2])

else:

    set = []
    img = plt.imread(args.image)
    for v, q, a, idx, q_len in val_loader:
        if v==img:
            set.append([v, q, a, idx, q_len])

    r = run(net, set, optimizer, tracker, train=False, prefix='val', epoch=1)
    print('answers:', r[0], 'accuracies:', r[1], 'idx:', r[2])

