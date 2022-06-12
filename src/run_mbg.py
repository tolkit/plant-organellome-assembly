# reads + threads, run MBG

import subprocess
from src.helpers import eprint, params_to_string
import uuid

# run an instance of MBG
# hardcode some parameters for the moment
# but allow them to be changed from the CLI

# outputs the assembly gfa in the working dir.
def run_mbg(mbg_path, fasta_read_paths, threads, k, a, w, u, prefix, gfa_directory):
    """Run MBG (https://github.com/maickrau/MBG).

    Args:
        mbg_path (string): path to the MBG executable.
        fasta_read_paths (string): path to the fasta file(s) to be assembled.
        threads (string): number of threads to use (MBG param).
        k (int): kmer size (MBG param).
        a (int): minimum kmer abundance size (MBG param).
        w (int): window size (MBG param).
        u (int): minimum unitig abundance (MBG param).
        prefix (string): prefix for the output files. If not provided, a
            random uuid will be used.
        gfa_directory (string): path to the directory to write the GFA to.

    Returns:
        string: path to the assembled GFA.
    """

    # echo some stuff back to user.
    eprint(f"[+] run_mbg::MBG path: {mbg_path}")
    eprint(f"[+] run_mbg::fasta read path(s): {fasta_read_paths}")
    eprint(f"[+] run_mbg::number of threads: {threads}")
    eprint(f"[+] run_mbg::prefixing files with: {prefix}")

    # file name depending on whether prefix is present
    if prefix is None:
        # randomly generate a uuid
        output_gfa_filename = (
            gfa_directory
            + str(uuid.uuid4())
            + "_"
            + params_to_string(k, a, w, u)
            + ".gfa"
        )
        eprint(f"[+] run_mbg::output gfa filename: {output_gfa_filename}")
    elif prefix is not None:
        output_gfa_filename = (
            gfa_directory + str(prefix) + "_" + params_to_string(k, a, w, u) + ".gfa"
        )
        eprint(f"[+] run_mbg::output gfa filename: {output_gfa_filename}")

    # annoying, but MBG needs `-i` specified multiple times
    # if there are multiple fasta files to be read in
    formatted_fasta_read_paths = []
    if isinstance(fasta_read_paths, list):
        for fasta_read_path in fasta_read_paths:
            formatted_fasta_read_paths.append("-i")
            formatted_fasta_read_paths.append(fasta_read_path)
    else:
        # NO spaces within each individual path
        temp_fasta_read_paths = fasta_read_paths.split(" ")
        for fasta_read_path in temp_fasta_read_paths:
            formatted_fasta_read_paths.append("-i")
            formatted_fasta_read_paths.append(fasta_read_path)

    # spawn the process
    # sensible(?) defaults for now...
    eprint("[+] Spawning MBG assembly run.")
    formatted_argument_string = f"{mbg_path} {' '.join(formatted_fasta_read_paths)} -o {output_gfa_filename} -k {str(k)} -a {str(a)} -w {str(w)} -u {str(u)} -t {str(threads)}"

    subprocess.run(formatted_argument_string, shell=True)

    eprint("[+] Finished MBG assembly run.")
    return output_gfa_filename
