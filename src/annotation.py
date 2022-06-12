import subprocess
import os
from src.helpers import eprint

def annotate(
    path_to_fasta,
    organelle,
    annotation_exec_path,
    hmms_dir,
    nhmmer_path,
    gff_dir,
    annotation_dir,
):
    """Annotate a fasta file with fpma or fppa.

    Args:
        path_to_fasta (string): auto-generated fasta from the
            pipeline.
        organelle (string): either "mitochondrion" or "chloroplast".
        annotation_exec_path (string): path to the fpma or fppa executable.
        hmms_dir (string): path to the directory containing the
            hmms.
        nhmmer_path (string): path to the nhmmer executable.
        gff_dir (string): path to the directory containing the gff files.
        annotation_dir (string): path to the directory containing the annotation files.

    Returns: TODO:
        string: path to the annotated fasta file.

    Notes:
        ...
    """
    # echo some stuff back to user.
    eprint(f"[+] annotate::path to fasta to annotate: {path_to_fasta}")
    eprint(f"[+] annotate::organelle of interest: {organelle}")

    eprint(f"[+] annotate::annotation executable path: {annotation_exec_path}")
    eprint(f"[+] annotate::HMMs directory: {hmms_dir}")

    eprint(f"[+] annotate::GFF output directory: {gff_dir}")
    eprint(
        f"[+] annotate::annotation output directory (logs & HTMLs): {annotation_dir}"
    )

    # make output file names
    # there will be:
    # - a log file (sort of TSV to be parsed later)
    # - a GFF file
    # - an HTML file

    # these can be made here, as they will already have chloro/mito
    # in the file names
    output_html_file = (
        annotation_dir
        + os.path.splitext(os.path.basename(path_to_fasta))[0]
        + "_fpma.html"
    )
    output_log_file = (
        annotation_dir
        + os.path.splitext(os.path.basename(path_to_fasta))[0]
        + "_fpma.log"
    )
    output_gff_file = (
        gff_dir + os.path.splitext(os.path.basename(path_to_fasta))[0] + "_fpma.gff"
    )

    if organelle == "mitochondria":
        # run fpma
        with open(output_log_file, "w") as outfile:
            subprocess.run(
                [
                    annotation_exec_path,
                    "--plant-mito",
                    path_to_fasta,
                    "--nhmmer-path",
                    nhmmer_path,
                    "--hmms-path",
                    hmms_dir,
                    "--plot",
                    output_html_file,
                    "--gff",
                    output_gff_file,
                    "--e-value",
                    "0.00000001"
                ],
                stdout=outfile,
            )
    elif organelle == "chloroplast":
        # run fppa
        with open(output_log_file, "w") as outfile:
            subprocess.run(
                [
                    annotation_exec_path,
                    "--plant-chloro",
                    path_to_fasta,
                    "--nhmmer-path",
                    nhmmer_path,
                    "--hmms-path",
                    hmms_dir,
                    "--plot",
                    output_html_file,
                    "--gff",
                    output_gff_file,
                    "--e-value",
                    "0.00000001"
                ],
                stdout=outfile,
            )
    # return the path to the annotated fasta file log file
    return output_log_file

# a function to parse fpma/fppa output
# and print whether it was a success or not
def parse_annotation_output():
    None
