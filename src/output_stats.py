# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
import os
from src.helpers import eprint


def gfatk_stats(gfatk_path, input_gfa_filename, log_directory):

    # echo some stuff back to user.
    eprint(f"[+] gfatk_stats::gfatk path: {gfatk_path}")
    eprint(f"[+] gfatk_stats::input GFA filename: {input_gfa_filename}")

    # output to the log dir
    output_gfa_filename_log = (
        log_directory + os.path.basename(input_gfa_filename) + ".log"
    )

    eprint(f"[+] gfatk_stats::saving gfatk stats logfile: {output_gfa_filename_log}")

    eprint("[+] Spawning gfatk stats run.")
    with open(output_gfa_filename_log, "w") as outfile:
        subprocess.run([gfatk_path, "stats", input_gfa_filename], stdout=outfile)

    eprint("[+] Finished gfatk stats run.")
