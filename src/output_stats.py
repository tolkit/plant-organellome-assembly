# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
import os
import sys
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
    return output_gfa_filename_log


# take the output of gfatk stats and determine how many
# subgraphs are in the GFA.
def parse_gfatk_stats_output(input_gfa_filename):

    # echo some stuff back to user.
    eprint(f"[+] gfatk_stats::input GFA filename: {input_gfa_filename}")

    with open(input_gfa_filename, "r") as infile:
        lines = infile.readlines()
        lines = [line.rstrip() for line in lines]

        last = lines[-1]
        # now extract the number from this line
        no_subgraphs = int(last.split(" ")[-1])
        eprint(f"[+] gfatk_stats::number of subgraphs in this GFA: {no_subgraphs}")
        # exit if the number of subgraphs > 1
        if no_subgraphs > 1:
            eprint(
                f"[+] gfatk_stats::number of subgraphs in this GFA was greater than 1 ({no_subgraphs}); exiting."
            )
            sys.exit(1)
        else:
            # given that there is a single subgraph, check number of segments
            # in the subgraph. It will be the second line
            no_segments = int(lines[1].split(" ")[-1])
            if no_segments != 3:
                eprint(
                    f"[+] gfatk_stats::number of segments in this subgraph ({no_segments}) is not equal to 3; exiting."
                )
                sys.exit(1)

        # we reach here it's all okay!
        eprint(f"[+] gfatk_stats::plastid graph looks OK.")
