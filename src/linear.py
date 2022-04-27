# use gfatk to make a linear represenation of the GFA
# how to include `-i` flag?

import subprocess
from src.helpers import eprint

def linearise_gfa(gfatk_path, output_gfa_extracted_mito_filename):
    
    # echo some stuff back to user.
    eprint(f"[+] linearise_gfa::gfatk path: {gfatk_path}")
    eprint(f"[+] linearise_gfa::output GFA (extracted) filename: {output_gfa_extracted_mito_filename}")

    output_fasta = output_gfa_extracted_mito_filename.split(".")[0] + ".fa"

    eprint("[+] Spawning gfatk linear run.")
    with open(output_fasta, "w") as outfile:
        subprocess.run([gfatk_path, "linear", output_gfa_extracted_mito_filename], stdout=outfile)
    
    eprint("[+] Finished gfatk linear run.")    
    