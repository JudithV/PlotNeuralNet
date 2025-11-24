import sys
sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_Conv("conv1", 512, 64, offset="(1,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("bn1", offset="(0,0,0)", to="(conv1-east)", height=64, depth=64, width=2 ),
    #to_Conv("relu1", offset="(0,0,0)", to="(bn1-east)"),
    to_Conv("conv2", 64, 64, offset="(1,0,0)", to="(bn1-east)", height=32, depth=32, width=2 ),
    to_connection( "bn1", "conv2"),
    to_Conv("conv2", 64, 64, offset="(1,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    to_Pool("bn2", offset="(0,0,0)", to="(conv2-east)", height=64, depth=64, width=2 ),
    #to_Conv("relu2", offset="(0,0,0)", to="(bn2-east)"),
    to_Conv("conv3", 64, 64, offset="(1,0,0)", to="(bn2-east)", height=32, depth=32, width=2 ),
    to_connection( "bn2", "conv3"),
    to_ConvConvRelu("pool1", offset="(0,0,0)", to="(conv3-east)"),
    #to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)"),
    #to_connection("conv3", "pool1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()