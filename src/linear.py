# use gfatk to make a linear represenation of the GFA
# how to include `-i` flag?

import subprocess
import os
from src.helpers import eprint


def linearise_gfa(gfatk_path, input_gfa_extracted_organelle_filename, fasta_directory):

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
        "[+] Spawning gfatk linear run, including node coverage. May cause a stackoverflow."
    )

    with open(output_fasta_i, "w") as outfile:
        subprocess.run(
            [gfatk_path, "linear", "-i", input_gfa_extracted_organelle_filename],
            stdout=outfile,
        )

    eprint("[+] Spawning gfatk linear run, excluding node coverage.")
    with open(output_fasta, "w") as outfile:
        subprocess.run(
            [gfatk_path, "linear", input_gfa_extracted_organelle_filename],
            stdout=outfile,
        )

    eprint("[+] Finished gfatk linear run.")
