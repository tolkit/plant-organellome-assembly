# 
# Plant Organelle Genome
# - Assembler
# - Annotator
# - Reorientator
#

import argparse
from src.run_mbg import run_mbg

parser = argparse.ArgumentParser(description=
'''
Assemble a plant organellome.
See installation instructions for dependencies.
''')
parser.add_argument('reads', metavar='reads', type=str, nargs='+',
                    help='the raw reads to be processed. gzipped or otherwise.')
parser.add_argument('--threads', default=10,
                    help='Number of threads MBG assembles with.')

args = parser.parse_args()

if __name__ == '__main__':
    run_mbg(args.reads)
