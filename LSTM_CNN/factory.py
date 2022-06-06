import copy
from bootstrap.lib.logger import Logger
from fusions import Block
from fusions import BlockTucker
from fusions import MLB
from fusions import MFB
from fusions import MFH
from fusions import MCB
from fusions import Mutan
from fusions import Tucker
from fusions import LinearSum
from fusions import ConcatMLP

def factory(ftype,input_dims, output_dims):

    if ftype == 'block':
        fusion = Block(input_dims, output_dims)
    elif ftype == 'block_tucker':
        fusion = BlockTucker(input_dims, output_dims)
    elif ftype == 'mlb':
        fusion = MLB(input_dims, output_dims)
    elif ftype == 'mfb':
        fusion = MFB(input_dims, output_dims)
    elif ftype == 'mfh':
        fusion = MFH(input_dims, output_dims)
    elif ftype == 'mcb':
        fusion = MCB(input_dims, output_dims)
    elif ftype == 'mutan':
        fusion = Mutan(input_dims, output_dims)
    elif ftype == 'tucker':
        fusion = Tucker(input_dims, output_dims)
    elif ftype == 'linear_sum':
        fusion = LinearSum(input_dims, output_dims)
    elif ftype == 'cat_mlp':
        fusion = ConcatMLP(input_dims, output_dims)
    else:
        raise ValueError()

    Logger().log_value('nb_params_fusion', fusion.n_params, should_print=True)
    return fusion