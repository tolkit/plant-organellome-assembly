# 
# Plant Organelle Genome
# - Assembler
# - Annotator
# - Reorientator
#

import argparse
from src.run_mbg import run_mbg
from src.output_stats import gfatk_stats

parser = argparse.ArgumentParser(description=
'''
Assemble a plant organellome.
See installation instructions for dependencies.
''')
parser.add_argument('reads', metavar='reads', type=str, nargs='+',
                    help='the raw reads to be processed. gzipped or otherwise.')
parser.add_argument('--threads', default=10,
                    help='Number of threads MBG assembles with.')
parser.add_argument('--mbg', type=str, default="MBG",
                    help='Path to MBG executable.')
parser.add_argument('--gfatk', type=str, default="gfatk",
                    help='Path to gfatk executable.')

args = parser.parse_args()

if __name__ == '__main__':
    # make the assembly gfa (5-10mins)
    # output_gfa = run_mbg(args.mbg, args.reads, args.threads)

    # for testing
    output_gfa = "output_graph.gfa"
    gfatk_stats(args.gfatk, output_gfa)
