import subprocess
import os
from src.helpers import eprint

# some housekeeping.
# create separate directories for log files,
# fasta files, and GFA files.


def make_dirs(dir):
    """Create directories for log files, fasta files,
        GFA files, and annotations (GFF's + HTML's).

    Args:
        dir (string): path to the directory to create the directories in.

    Returns:
        (
        string,
        string,
        string,
        string,
        string
        ): tuple of paths to the directories that were created.
    """

    # if user specifies a dir
    if dir is not None:
        # check if user put a trailing slash or not
        if dir.endswith("/"):
            log_directory = dir + "poa_logs/"
            fasta_directory = dir + "poa_fastas/"
            gfa_directory = dir + "poa_gfas/"
            gff_directory = dir + "poa_gffs/"
            annotation_directory = dir + "poa_annotations/"
        else:
            log_directory = dir + "/poa_logs/"
            fasta_directory = dir + "/poa_fastas/"
            gfa_directory = dir + "/poa_gfas/"
            gff_directory = dir + "/poa_gffs/"
            annotation_directory = dir + "/poa_annotations/"
    # else we are in the current directory
    else:
        log_directory = "./poa_logs/"
        fasta_directory = "./poa_fastas/"
        gfa_directory = "./poa_gfas/"
        gff_directory = "./poa_gffs/"
        annotation_directory = "./poa_annotations/"

    # only make the dirs if they are not already there.
    # otherwise we get annoying stderr warnings.
    if not os.path.isdir(log_directory):
        subprocess.call(["mkdir", log_directory])
    if not os.path.isdir(fasta_directory):
        subprocess.call(["mkdir", fasta_directory])
    if not os.path.isdir(gfa_directory):
        subprocess.call(["mkdir", gfa_directory])
    if not os.path.isdir(gff_directory):
        subprocess.call(["mkdir", gff_directory])
    if not os.path.isdir(annotation_directory):
        subprocess.call(["mkdir", annotation_directory])

    return (
        log_directory,
        fasta_directory,
        gfa_directory,
        gff_directory,
        annotation_directory,
    )
