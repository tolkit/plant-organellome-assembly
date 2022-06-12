# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
import os
from src.helpers import eprint


def extract_chloro(gfatk_path, input_gfa_filename, gfa_directory):
    """Extract the chloroplast from a GFA.

    Args:
        gfatk_path (string): path to the gfatk executable.
        input_gfa_filename (string): path to the input GFA.
        gfa_directory (string): path to the directory where output
            GFA's are to be saved.

    Returns:
        string: path to the output putative chloroplast GFA.

    Notes:
        ...
    """

    # echo some stuff back to user.
    eprint(f"[+] extract_chloro::gfatk path: {gfatk_path}")
    eprint(f"[+] extract_chloro::input GFA filename: {input_gfa_filename}")

    # make output file name
    output_gfa_filename_extract_chloro = (
        gfa_directory
        + os.path.splitext(os.path.basename(input_gfa_filename))[0]
        + "_extract_chloro.gfa"
    )

    eprint(
        f"[+] extract_chloro::saving gfatk extract-chloro output at: {output_gfa_filename_extract_chloro}"
    )

    eprint("[+] extract_chloro::spawning gfatk extract-chloro run.")
    with open(output_gfa_filename_extract_chloro, "w") as outfile:
        # there are other `gfatk extract-chloro` params that
        # may be worth including/exploring
        subprocess.run(
            [
                gfatk_path,
                "extract-chloro",
                input_gfa_filename,
                "--gc-upper",
                "0.40",
                "--gc-lower",
                "0.34",
            ],
            stdout=outfile,
        )

    eprint("[+] extract_chloro::finished gfatk extract-chloro run.")
    return output_gfa_filename_extract_chloro
