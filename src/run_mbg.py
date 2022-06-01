# reads + threads, run MBG

import subprocess
from src.helpers import eprint
import uuid

# run an instance of MBG
# hardcode some parameters for the moment
# but allow them to be changed from the CLI

# outputs the assembly gfa in the working dir.
def run_mbg(mbg_path, fasta_read_paths, threads, k, a, w, u, prefix, gfa_directory):

    # echo some stuff back to user.
    eprint(f"[+] run_mbg::MBG path: {mbg_path}")
    eprint(f"[+] run_mbg::fasta read path(s): {fasta_read_paths}")
    eprint(f"[+] run_mbg::number of threads: {threads}")
    eprint(f"[+] run_mbg::prefixing files with: {prefix}")

    # file name depending on whether prefix is present
    if prefix is None:
        # randomly generate a uuid
        output_gfa_filename = gfa_directory + str(uuid.uuid4()) + ".gfa"
        eprint(f"[+] run_mbg::output gfa filename: {output_gfa_filename}")
    elif prefix is not None:
        output_gfa_filename = gfa_directory + str(prefix) + ".gfa"
        eprint(f"[+] run_mbg::output gfa filename: {output_gfa_filename}")

    # spawn the process
    # sensible(?) defaults for now...
    # TODO: Marcela help!
    eprint("[+] Spawning MBG assembly run.")
    subprocess.run(
        [
            mbg_path,
            "-i",
            " ".join(fasta_read_paths),
            "-o",
            output_gfa_filename,
            "-k",
            k,
            "-a",
            a,
            "-w",
            w,
            "-u",
            u,
        ]
    )

    eprint("[+] Finished MBG assembly run.")
    return output_gfa_filename
