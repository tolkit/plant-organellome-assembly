import sys


def eprint(*args, **kwargs):
    """Print to stderr.

    Args:
        *args: arguments to print.
        **kwargs: keyword arguments to print.

    Notes:
        A thin wrapper of print() that prints to stderr.
        See https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python.
    """
    print(*args, file=sys.stderr, **kwargs)


# add together the parameters
# k, a, w, and u (MBG options)
# into a string so we can add to file names.
def params_to_string(k, a, w, u):
    """Convert parameters to a string.

    Args:
        k (Any): kmer size.
        a (Any): kmer abundance threshold.
        w (Any): window size.
        u (Any): minimum unitig abundance.

    Returns:
        string: parameters as a string.
    """
    return "k=" + str(k) + "a=" + str(a) + "w=" + str(w) + "u=" + str(u)


def is_tool(name):
    """Check whether `name` is on PATH and marked as executable

    Args:
        name (string): name of the tool to check.

    Returns:
        bool: True if the tool is present.

    Notes:
        See https://stackoverflow.com/questions/11210104/check-if-a-program-exists-from-a-python-script
    """

    # from whichcraft import which
    from shutil import which

    return which(name) is not None


def check_args_and_tools(args):
    """Check whether all the tools we need are present.

    Args:
        args (Namespace): parsed arguments.

    Notes:
        We hard exit if we don't have all the tools/args we need.
    """
    # gfatk and MBG are required no matter what.
    gfatk = args.gfatk
    mbg = args.mbg

    if not is_tool(gfatk):
        eprint(
            "[-] check_args_and_tools::gfatk not found. Please specify a valid path to gfatk."
        )
        sys.exit(1)
    if not is_tool(mbg):
        eprint(
            "[-] check_args_and_tools::MBG not found. Please specify a valid path to MBG."
        )
        sys.exit(1)

    organelle = args.organelle
    annotation = args.annotation

    # if we are on the annotation pipeline
    # we need to check the presence of three more
    # tools: nhmmer, fpma, and fppa
    if annotation is not None:
        # we firstly need to check that annotation == organelle
        if annotation != organelle:
            eprint(
                "[-] check_args_and_tools::the annotation flag option must be the same as the organelle flag option."
            )
            sys.exit(1)

        # and now check the executables are present
        # we need hmmer for both tools!
        nhmmer = args.nhmmer
        if not is_tool(nhmmer):
            eprint(
                "[-] check_args_and_tools::the nhmmer tool is not present. Required for annotation. Please install here: http://hmmer.org/download.html"
            )
            sys.exit(1)

        # check only fppa is present if we are on the chloroplast/both
        if annotation == "chloroplast" or annotation == "both":
            fppa = args.fppa
            if not is_tool(fppa):
                eprint(
                    "[-] check_args_and_tools::the fppa tool is not present. Required for annotation. Please install here: https://github.com/tolkit/fppa"
                )
                sys.exit(1)
            # check that the hmms are present also.
            # I guess this functionality is built into argparse...
            fppa_hmms = args.fppa_hmms
            if fppa_hmms is None:
                eprint(
                    "[-] check_args_and_tools::the fppa_hmms option is not present. Required for annotation. Please specify a valid path to the fppa hmms."
                )
                sys.exit(1)
        # conversely, check only fpma is present if we are on the mitochondria/both
        elif annotation == "mitochondria" or annotation == "both":
            fpma = args.fpma
            if not is_tool(fpma):
                eprint(
                    "[-] check_args_and_tools::the fpma tool is not present. Required for annotation. Please install here: https://github.com/tolkit/fpma"
                )
                sys.exit(1)
            # now check that the fpma hmms are present
            fpma_hmms = args.fpma_hmms
            if fpma_hmms is None:
                eprint(
                    "[-] check_args_and_tools::the fpma_hmms option is not present. Required for annotation. Please specify a valid path to the fpma hmms."
                )
                sys.exit(1)
