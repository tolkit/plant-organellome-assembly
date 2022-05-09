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
from src.extract_chloro import extract_chloro
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
parser.add_argument('--organelle', type=str, default="mitochondria", choices = ['mitochondria', 'chloroplast', 'both'],
                    help='Assemble a mitochondrial or chloroplast genome.')
parser.add_argument('--prefix', type=str, nargs='?',
                    help='Prefix for all of the output files. Otherwise a random UUID is generated.')

args = parser.parse_args()

# arg checking?

if __name__ == '__main__':
    # make the assembly gfa (5-10mins)
    # output_gfa = run_mbg(args.mbg, args.reads, args.threads, args.prefix)
    
    # for testing, uncomment below and add path to GFA
    output_gfa = "./data/gfas/Buxus_sempervirens_NC_058304.1.MZ934757.1.fasta.BOTH.HiFiMapped.bam.filtered.3k.gfa"

    # output a log file of the assembly GFA
    gfatk_stats(args.gfatk, output_gfa, args.prefix)
    
    # extract organelle from GFA
    if args.organelle == "mitochondria":
        output_gfa_extracted_mito = extract_mito(args.gfatk, output_gfa)
        # linearise
        linearise_gfa(args.gfatk, output_gfa_extracted_mito)

    elif args.organelle == "chloroplast":
        output_gfa_extracted_chloro = extract_chloro(args.gfatk, output_gfa)
        # linearise
        linearise_gfa(args.gfatk, output_gfa_extracted_chloro)
    
    elif args.organelle == "both":
        output_gfa_extracted_mito = extract_mito(args.gfatk, output_gfa)
        output_gfa_extracted_chloro = extract_chloro(args.gfatk, output_gfa)
        # linearise both
        linearise_gfa(args.gfatk, output_gfa_extracted_mito)
        linearise_gfa(args.gfatk, output_gfa_extracted_chloro)

    # if the organelle is mitochondrial, also run fpma