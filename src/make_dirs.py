import subprocess
from src.helpers import eprint

# some housekeeping.
# create separate directories for log files,
# fasta files, and GFA files.


def make_dirs(dir):

    # if user specifies a dir
    if dir is not None:
        # check if user put a trailing slash or not
        if dir.endswith("/"):
            log_directory = dir + "poa_logs/"
            fasta_directory = dir + "poa_fastas/"
            gfa_directory = dir + "poa_gfas/"
        else:
            log_directory = dir + "/poa_logs/"
            fasta_directory = dir + "/poa_fastas/"
            gfa_directory = dir + "/poa_gfas/"
    # else we are in the current directory
    else:
        log_directory = "./poa_logs/"
        fasta_directory = "./poa_fastas/"
        gfa_directory = "./poa_gfas/"

    # now make the dirs
    subprocess.call(["mkdir", log_directory, fasta_directory, gfa_directory])

    return log_directory, fasta_directory, gfa_directory
