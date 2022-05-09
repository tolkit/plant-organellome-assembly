# run gfatk stats and save output in a log file.
# this is for manual inspection and debugging
# in case things get crazy.

import subprocess
from src.helpers import eprint

def extract_mito(gfatk_path, output_gfa_filename):
    
    # echo some stuff back to user.
    eprint(f"[+] extract_mito::gfatk path: {gfatk_path}")
    eprint(f"[+] extract_mito::output GFA filename: {output_gfa_filename}")

    # make the new file name
    output_gfa_filename_extract_mito = output_gfa_filename.split(".")[0] + "_extract_mito.gfa"
    eprint(f"[+] extract_mito::saving gfatk extract-mito output at: {output_gfa_filename_extract_mito}")

    eprint("[+] Spawning gfatk extract-mito run.")
    with open(output_gfa_filename_extract_mito, "w") as outfile:
        subprocess.run([gfatk_path, "extract-mito", output_gfa_filename], stdout=outfile)
    
    eprint("[+] Finished gfatk extract-mito run.")
    return output_gfa_filename_extract_mito
    