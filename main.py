# 
# Plant Organelle Genome
# - Assembler
# - Annotator
# - Reorientator
#

# (potential) problems
# - extracting the mito from the GFA assembly
#   might need to be a bit more sophisticated.
#   For example, an annotator/blast approach.

import argparse
from src.helpers import eprint
from src.run_mbg import run_mbg
from src.output_stats import gfatk_stats
from src.extract_mito import extract_mito
from src.linear import linearise_gfa

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

# arg checking?

if __name__ == '__main__':
    # make the assembly gfa (5-10mins)
    # output_gfa = run_mbg(args.mbg, args.reads, args.threads)
    # for testing
    output_gfa = "output_graph.gfa"

    # output a log file of the assembly GFA
    gfatk_stats(args.gfatk, output_gfa)
    # extract mito from the GFA
    output_gfa_extracted_mito = extract_mito(args.gfatk, output_gfa)
    # linearise
    linearise_gfa(args.gfatk, output_gfa_extracted_mito)
