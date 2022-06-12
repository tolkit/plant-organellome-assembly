# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
import os
from src.helpers import eprint


def extract_mito(gfatk_path, input_gfa_filename, gfa_directory):
    """Extract the mitochondrion from a GFA.

    Args:
        gfatk_path (string): path to the gfatk executable.
        input_gfa_filename (string): path to the input GFA.
        gfa_directory (string): path to the directory where output
            GFA's are to be saved.

    Returns:
        string: path to the output putative mitochondrion GFA.

    Notes:
        ...
    """

    # echo some stuff back to user.
    eprint(f"[+] extract_mito::gfatk path: {gfatk_path}")
    eprint(f"[+] extract_mito::input GFA filename: {input_gfa_filename}")

    # make output file name
    output_gfa_filename_extract_mito = (
        gfa_directory
        + os.path.splitext(os.path.basename(input_gfa_filename))[0]
        + "_extract_mito.gfa"
    )

    eprint(
        f"[+] extract_mito::saving gfatk extract-mito output at: {output_gfa_filename_extract_mito}"
    )

    eprint("[+] extract_mito::spawning gfatk extract-mito run.")
    with open(output_gfa_filename_extract_mito, "w") as outfile:
        subprocess.run([gfatk_path, "extract-mito", input_gfa_filename], stdout=outfile)

    eprint("[+] extract_mito::finished gfatk extract-mito run.")
    return output_gfa_filename_extract_mito
