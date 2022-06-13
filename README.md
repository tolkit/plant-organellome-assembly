# pmpap

A plant mitochondrial/organelle genome assembly pipeline.

<p align="center">
     <img width="300" height="132"
    src="https://www.darwintreeoflife.org/wp-content/themes/dtol/dist/assets/gfx/dtol-logo-round.png">
</p>

## Pipeline

### Overview

- Assemble the reads using <a href="https://github.com/maickrau/MBG">MBG</a>.
- Check the statistics of the output GFA (<a href="https://github.com/tolkit/gfatk/">gfatk</a>).
- Extract the putative mitochondrial genome subgraph (<a href="https://github.com/tolkit/gfatk/">gfatk</a>).
  - Note there may be more than one subgraph, and this is expected in some cases.
- Extract the putative chloroplast genome subgraph (<a href="https://github.com/tolkit/gfatk/">gfatk</a>).
  - We expect three segments from one subgraph, however this is not always the case.
- Linearise the graphs (<a href="https://github.com/tolkit/gfatk/">gfatk</a>).
  - We currently linearise within each subgraph, and attempt to include node coverage.
- Annotate the linearised organelle genome to see if it's complete.
  - Using <a href="https://github.com/tolkit/fpma/">fpma</a> and <a href="https://github.com/tolkit/fppa/">fppa</a>

### CLI usage

```txt
usage: pmpap.py [-h] [--mbg MBG] [--mbg-threads MBG_THREADS] [--mbg-k MBG_K] [--mbg-a MBG_A] [--mbg-w MBG_W]
                [--mbg-u MBG_U] [--gfatk GFATK] [--organelle {mitochondria,chloroplast,both}] [--prefix [PREFIX]]
                [--dir [DIR]] [--gfa [GFA]] [--annotation [{mitochondria,chloroplast,both}]] [--nhmmer NHMMER]
                [--fpma FPMA] [--fpma-hmms FPMA_HMMS] [--fppa FPPA] [--fppa-hmms FPPA_HMMS]
                [reads]

PMPAP: Plant Mitochondrial/Plastid Assembly Pipeline: https://github.com/tolkit/plant-organellome-assembly

positional arguments:
  reads                 the raw reads to be processed. gzipped or otherwise. (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --mbg MBG             path to MBG executable. (default: MBG)
  --mbg-threads MBG_THREADS
                        number of threads MBG assembles with. (default: 10)
  --mbg-k MBG_K         the k option value which MBG will assemble with. This is the kmer size. (default: 5001)
  --mbg-a MBG_A         the a option value which MBG will assemble with. This is the minimum kmer abundance. (default:
                        5)
  --mbg-w MBG_W         the w option value which MBG will assemble with. This is the window size, cannot be larger than
                        k - 30. (default: 250)
  --mbg-u MBG_U         the u option value which MBG will assemble with. This is the minimum unitig abundance.
                        (default: 150)
  --gfatk GFATK         path to gfatk executable. (default: gfatk)
  --organelle {mitochondria,chloroplast,both}
                        assemble a mitochondrial or chloroplast genome, or both. (default: mitochondria)
  --prefix [PREFIX]     prefix for all of the output files. otherwise a random UUID is generated. (default: None)
  --dir [DIR]           directory where all output directories are to store their output. (default: None)
  --gfa [GFA]           if you already have an MBG output GFA, use this entry point to specify the GFA file path.
                        (default: None)
  --annotation [{mitochondria,chloroplast,both}]
                        annotate a mitochondrial or chloroplast genome, or both. Omitting this option will not annotate
                        anything. (default: None)
  --nhmmer NHMMER       path to nhmmer executable. (default: nhmmer)
  --fpma FPMA           path to fpma executable. (default: fpma)
  --fpma-hmms FPMA_HMMS
                        path to fpma-hmms directory. (default: None)
  --fppa FPPA           path to fppa executable. (default: fppa)
  --fppa-hmms FPPA_HMMS
                        path to fppa-hmms directory. (default: None)
```

Main MBG parameters which seem to affect the assembly are included in the command line.

## Dependencies and installation advice

There are five dependencies for this pipeline:

- MBG (https://github.com/maickrau/MBG; conda installation easiest.)
- nhmmer (http://hmmer.org/download.html and http://hmmer.org/documentation.html; I compiled from source)
- gfatk (https://github.com/tolkit/gfatk/; build from source, working on making this easier to install.)
- fpma (https://github.com/tolkit/fpma/; build from source. Database in this repo also required.)
- fppa (https://github.com/tolkit/fppa/; build from source. Database in this repo also required.)

I'll attempt to walk through the installation process, as there are a few bits and bobs.

1. MBG

This is probably the easiest. You will need conda:

```bash
conda install -c bioconda mbg
# `MBG` should be in your path, check it!
MBG --version
```

You can also compile from source. See https://github.com/maickrau/MBG.

2. nhmmer

The documentation on HMMER.org (http://hmmer.org/documentation.html) is pretty good. I compiled from source, and did all the checks:

```bash
wget http://eddylab.org/software/hmmer/hmmer.tar.gz 
tar zxf hmmer.tar.gz
cd hmmer-3.3.2
./configure --prefix /your/install/path
make
make check
make install
```

3. gfatk, fpma, fppa

You will need to install Rust on your system.

```bash
# using rustup (recommended)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# `rustup`, which is the toolchain installer for rust, will attempt
# to add all the relevant bits to your PATH.
```

I'll go through the installation in this BASH script.

```bash
# gfatk v0.2.1 (latest) is on crates.io, so get it directly.
cargo install gfatk
# check
gfatk --version

# the annotators require bits of data in folders, so get from 
# GitHub. cd to wherever you want the data to be stored.
git clone https://github.com/tolkit/fpma
cd fpma
# this installs the executable to PATH
cargo install --path=.
# check 
fpma --version
# in the fpma dir are the HMMs
# e.g. if you were running on a flowering plant:
ls ./hmms/angiosperm_hmms/

# last one is fppa.
git clone https://github.com/tolkit/fppa
cd fppa
cargo install --path=.
# check 
fppa --version
# and show the flowering plant HMMs for the chloroplast
# sorry the default names are different between these tools...
ls ./hmms/Magnoliopsida/
```

## Example run

Now all the dependencies are installed, you can run the pipeline. I will show the most complete example I can think of.

```bash
# pmpap.py is the entrypoint for the pipeline.
# I assume all of the necessary tools installed are in PATH.
# I am using default MBG params
python3 pmpap.py \
    --organelle both \
    --prefix my_plant \
    --dir /path/to/output \
    --annotation both \
    --fpma-hmms fpma-hmms \
    --fppa-hmms fppa-hmms \
    /path/to/raw/reads.fa.gz
```

This will produce five output directories in the directory `/path/to/output`. A lot of information will be printed to the STDERR, this can be very useful to see where in the pipeline the error/failure is, or to garner further information about the assemblies that have been produced.

The output directories contain the following information:

- `poa_annotations` is where the HTMLs & logs for the annotated assembly fastas are. Especially the log files are useful, as at the top there is a statement of how many genes were annotated. Above ~90% for the chloroplast, and ~80% for the mitochondria (core genes at least), indicate probable assembly completeness/success.
- `poa_fastas` is where the assemblies live. These are linearised GFA's and can include coverage information (if the `-i` flag was successful) which means there will be repitition of segments from the GFA. The fasta record headers usually contain interesting information, e.g. which subgraph the contig is from, which path through the graph was used, and whether the molecule is circular or not.
- `poa_gfas` contain all the GFA's produced in the course of the program. If there is a failure in the pipeline, it is usually because a chloroplast or mitochondrion could not be extracted from the initial GFA produced by MBG. As this GFA is saved here, you can troubleshoot as to why. The answer is usually re-running the pipeline with modified MBG parameters.
- `poa_gffs` are where the GFF files from the annotation pipeline are stored. Not sure how useful they are.
- `poa_logs` are essentially the raw output of `gfatk stats <GFA>`. Check these if something has gone wrong. These files should never be that big, or contain hundreds of subgraphs. If they do, the MBG parameters need to be edited.