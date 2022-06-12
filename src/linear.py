import subprocess
import os
from src.helpers import eprint


def linearise_gfa(gfatk_path, input_gfa_extracted_organelle_filename, fasta_directory):
    """Linearise a GFA.

    Args:
        gfatk_path (string): path to the gfatk executable.
        input_gfa_extracted_organelle_filename (string): path to the input GFA.
        fasta_directory (string): path to the directory where output
            fasta's are to be saved.

    Returns:
        string: paths to the linearised fastas.

    Notes:
        `gfatk linear` is run with the `-e` flag, so linearisations
        are made within subgraphs. This is because in the previous
        step, `gfatk extract-chloro/mito` potentially extracts multiple
        subgraphs. Including node coverage (`-i`) is always attempted.
    """

    # echo some stuff back to user.
    eprint(f"[+] linearise_gfa::gfatk path: {gfatk_path}")
    eprint(
        f"[+] linearise_gfa::input GFA (extracted) filename: {input_gfa_extracted_organelle_filename}"
    )

    # make output file names
    output_fasta_i = (
        fasta_directory
        + os.path.splitext(os.path.basename(input_gfa_extracted_organelle_filename))[0]
        + "_incl_node_cov.fa"
    )

    output_fasta = (
        fasta_directory
        + os.path.splitext(os.path.basename(input_gfa_extracted_organelle_filename))[0]
        + ".fa"
    )

    eprint(
        "[+] linearise_gfa::spawning gfatk linear run, including node coverage. May cause a stackoverflow."
    )

    with open(output_fasta_i, "w") as outfile:
        subprocess.run(
            [gfatk_path, "linear", "-e", "-i", input_gfa_extracted_organelle_filename],
            stdout=outfile,
        )

    eprint("[+] linearise_gfa::spawning gfatk linear run, excluding node coverage.")
    with open(output_fasta, "w") as outfile:
        subprocess.run(
            [gfatk_path, "linear", "-e", input_gfa_extracted_organelle_filename],
            stdout=outfile,
        )

    eprint("[+] linearise_gfa::finished gfatk linear run.")
    return output_fasta_i, output_fasta
