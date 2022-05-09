# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
from src.helpers import eprint

def extract_chloro(gfatk_path, output_gfa_filename):
    
    # echo some stuff back to user.
    eprint(f"[+] extract_chloro::gfatk path: {gfatk_path}")
    eprint(f"[+] extract_chloro::output GFA filename: {output_gfa_filename}")

    # make the new file name
    output_gfa_filename_extract_chloro = output_gfa_filename.split(".")[0] + "_extract_chloro.gfa"
    eprint(f"[+] extract_chloro::saving gfatk extract-chloro output at: {output_gfa_filename_extract_chloro}")

    eprint("[+] Spawning gfatk extract-chloro run.")
    with open(output_gfa_filename_extract_chloro, "w") as outfile:
        # there are other `gfatk extract-chloro` params that
        # may be worth including/exploring
        subprocess.run([gfatk_path, "extract-chloro", output_gfa_filename, "--gc-upper", "0.40"], stdout=outfile)
    
    eprint("[+] Finished gfatk extract-chloro run.")
    return output_gfa_filename_extract_chloro
