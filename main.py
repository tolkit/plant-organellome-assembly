# Max Brown, Wellcome Sanger Institute 2022
# Along with the plant organelle team:
# - Marcela Uliano
# - Lucia Campos
# - Alex Twyford

# log_directory = "poa_logs"
# fasta_directory = "poa_fastas"
# gfa_directory = "poa_gfas"

import argparse
import subprocess
import os
import sys

from src.helpers import eprint
from src.run_mbg import run_mbg
from src.output_stats import gfatk_stats, parse_gfatk_stats_output
from src.extract_mito import extract_mito
from src.extract_chloro import extract_chloro
from src.linear import linearise_gfa
from src.make_dirs import make_dirs

parser = argparse.ArgumentParser(
    description="""
Assemble a plant organellome.
See installation instructions for dependencies.
"""
)
parser.add_argument(
    "reads",
    metavar="reads",
    type=str,
    nargs="?",
    help="the raw reads to be processed. gzipped or otherwise.",
)
parser.add_argument(
    "--threads", default=10, help="number of threads MBG assembles with."
)
parser.add_argument("--mbg", type=str, default="MBG", help="path to MBG executable.")
parser.add_argument(
    "--gfatk", type=str, default="gfatk", help="path to gfatk executable."
)
parser.add_argument(
    "--organelle",
    type=str,
    default="mitochondria",
    choices=["mitochondria", "chloroplast", "both"],
    help="assemble a mitochondrial or chloroplast genome, or both.",
)
parser.add_argument(
    "--prefix",
    type=str,
    nargs="?",
    help="prefix for all of the output files. otherwise a random UUID is generated.",
)
parser.add_argument(
    "--dir",
    type=str,
    nargs="?",
    help="directory where all output directories are to store their output.",
)
parser.add_argument(
    "--gfa",
    type=str,
    nargs="?",
    help="if you already have an MBG output GFA, use this entry point to specify the GFA file path.",
)

# so we don't create directories unnecessarily.
args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

if __name__ == "__main__":

    # create the output directories
    log_directory, fasta_directory, gfa_directory = make_dirs(args.dir)

    if args.gfa:
        # copy the GFA to our file structure location, so we don't break stuff below
        # if we have a prefix, give it that prefix too
        if args.prefix:
            copy_location = gfa_directory + args.prefix + ".gfa"
            output_gfa = copy_location
        else:
            copy_location = gfa_directory
            output_gfa = gfa_directory + os.path.basename(args.gfa)

        subprocess.call(["cp", args.gfa, copy_location])

    else:
        if args.reads is None:
            parser.error("--reads was not specified. required is --gfa is absent.")
        # we make the output gfa from MBG
        # ~ 5-10 mins.
        output_gfa = run_mbg(
            args.mbg, args.reads, args.threads, args.prefix, gfa_directory
        )

    # now begin the pipeline

    # output a log file of the assembly GFA
    gfatk_stats(args.gfatk, output_gfa, log_directory)

    # extract organelle from GFA
    if args.organelle == "mitochondria":
        output_gfa_extracted_mito = extract_mito(args.gfatk, output_gfa, gfa_directory)
        # linearise
        linearise_gfa(args.gfatk, output_gfa_extracted_mito, fasta_directory)

    elif args.organelle == "chloroplast":
        output_gfa_extracted_chloro = extract_chloro(
            args.gfatk, output_gfa, gfa_directory
        )

        # check here whether we have the expected three segments
        output_gfa_extracted_chloro_log = gfatk_stats(
            args.gfatk, output_gfa_extracted_chloro, log_directory
        )

        parse_gfatk_stats_output(output_gfa_extracted_chloro_log)

        # linearise
        linearise_gfa(args.gfatk, output_gfa_extracted_chloro, fasta_directory)

    elif args.organelle == "both":
        output_gfa_extracted_mito = extract_mito(args.gfatk, output_gfa, gfa_directory)
        output_gfa_extracted_chloro = extract_chloro(
            args.gfatk, output_gfa, gfa_directory
        )

        # check here whether we have the expected three segments
        output_gfa_extracted_chloro_log = gfatk_stats(
            args.gfatk, output_gfa_extracted_chloro, log_directory
        )
        parse_gfatk_stats_output(output_gfa_extracted_chloro_log)

        # linearise both
        linearise_gfa(args.gfatk, output_gfa_extracted_mito, fasta_directory)
        linearise_gfa(args.gfatk, output_gfa_extracted_chloro, fasta_directory)

    # if the organelle is mitochondrial, also run fpma
