# reads + threads, run MBG

import subprocess
from src.helpers import eprint
import uuid

# run an instance of MBG
# hardcode some parameters for the moment
# but allow them to be changed from the CLI

# outputs the assembly gfa in the working dir.
def run_mbg(mbg_path, fasta_read_paths, threads):
    
    # echo some stuff back to user.
    eprint(f"[+] run_mbg\tMBG path: {mbg_path}")
    eprint(f"[+] run_mbg\tfasta read path(s): {fasta_read_paths}")
    eprint(f"[+] run_mbg\tnumber of threads: {threads}")

    # for
    output_gfa_filename = str(uuid.uuid4()) + ".gfa"
    eprint(f"[+] run_mbg\toutput gfa filename: {output_gfa_filename}")

    # spawn the process
    # sensible(?) defaults for now...
    eprint("[+] Spawning MBG assembly run.")
    subprocess.run([mbg_path,
                    "-i", " ".join(fasta_read_paths),
                    "-o", output_gfa_filename,
                    "-k", "1001",
                    "-a", "5",
                    "-w", "250",
                    "-u", "150"])
    
    eprint("[+] Finished MBG assembly run.")
    return output_gfa_filename