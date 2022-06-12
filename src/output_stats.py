import subprocess
import os
import sys
from src.helpers import eprint


def gfatk_stats(gfatk_path, input_gfa_filename, log_directory):
    """Generate a stats log file from gfatk.

    Args:
        gfatk_path (string): path to the gfatk executable.
        input_gfa_filename (string): path to the input GFA.
        log_directory (string): path to the directory where log files are to be saved.

    Returns:
        string: path to the log file.

    Notes:
        This is mainly for manual debugging if the pipeline for some reason
        fails (e.g. can't extract/linearise the GFA made from MBG).

        `gfatk stats` (version 0.2.1) has an output format like this:
            Subgraph number: <int>
                Number of nodes/segments: <int>
                Number of edges/links: <int>
                Circular: <bool>

                Segment ID's:
                list[int]

                Total sequence length:  <int>
                Total sequence overlap length:  <int>
                Sequence length minus overlaps: <int>
                GC content of total sequence:   <float>
                Average coverage of total segments:     <float>
    """

    # echo some stuff back to user.
    eprint(f"[+] gfatk_stats::gfatk path: {gfatk_path}")
    eprint(f"[+] gfatk_stats::input GFA filename: {input_gfa_filename}")

    # output to the log dir
    output_gfa_filename_log = (
        log_directory + os.path.basename(input_gfa_filename) + ".log"
    )

    eprint(f"[+] gfatk_stats::saving gfatk stats logfile: {output_gfa_filename_log}")

    eprint("[+] gfatk_stats::spawning gfatk stats run.")
    with open(output_gfa_filename_log, "w") as outfile:
        subprocess.run([gfatk_path, "stats", input_gfa_filename], stdout=outfile)

    eprint("[+] gfatk_stats::finished gfatk stats run.")
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
        if no_subgraphs == 0:
            eprint(
                f"[+] gfatk_stats::looks like the GFA is empty. This is probably because the chloroplast could not be extracted."
            )
            return None
        # exit if the number of subgraphs > 1
        if no_subgraphs > 1:
            eprint(
                f"[+] gfatk_stats::number of subgraphs in this GFA was greater than 1 ({no_subgraphs}); skipping."
            )
            return None
        else:
            # given that there is a single subgraph, check number of segments
            # in the subgraph. It will be the second line
            no_segments = int(lines[1].split(" ")[-1])
            if no_segments not in [1, 3]:
                eprint(
                    f"[+] gfatk_stats::number of segments in this subgraph ({no_segments}) is not equal to 1 or 3; skipping."
                )
                return None

        # we reach here it's all okay!
        eprint(f"[+] gfatk_stats::plastid graph looks OK.")
