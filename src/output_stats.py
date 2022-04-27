# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
from src.helpers import eprint

def gfatk_stats(gfatk_path, output_gfa_filename):
    
    # echo some stuff back to user.
    eprint(f"[+] gfatk_stats\tgfatk path: {gfatk_path}")
    eprint(f"[+] gfatk_stats\toutput GFA filename: {output_gfa_filename}")

    output_gfa_filename_log = output_gfa_filename + ".log"
    eprint(f"[+] gfatk_stats\tsaving gfatk stats logfile: {output_gfa_filename_log}")

    eprint("[+] Spawning gfatk stats run.")
    with open(output_gfa_filename_log, "w") as outfile:
        subprocess.run([gfatk_path, "stats", output_gfa_filename], stdout=outfile)
    
    eprint("[+] Finished gfatk stats run.")    
    