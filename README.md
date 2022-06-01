# pmpap

A plant mitochondrial/organelle genome assembly pipeline.

<p align="center">
     <img width="300" height="132"
    src="https://www.darwintreeoflife.org/wp-content/themes/dtol/dist/assets/gfx/dtol-logo-round.png">
</p>

## Pipeline

### Overview

- Assemble the reads using MBG.
- Check the statistics of the output GFA.
- Extract the putative mitochondrial genome subgraph.
- Extract the putative chloroplast genome subgraph.
  - For the chloroplast, if the number of segments is not equal to 3, we exit.
- Linearise the subgraph.
- Annotate the linearised organelle genome to see if it's complete.

### CLI usage

```bash
usage: pmpap.py [-h] [--threads THREADS] [--mbg MBG] [--gfatk GFATK] [--organelle {mitochondria,chloroplast,both}]
               [--prefix [PREFIX]] [--dir [DIR]] [--gfa [GFA]]
               [reads]

PMPAP: Plant Mitochondrial/Plastid Assembly Pipeline:
Assemble a plant organellome.
See installation instructions for dependencies.
<https://github.com/tolkit/plant-organellome-assembly>

positional arguments:
  reads                 the raw reads to be processed. gzipped or otherwise.

optional arguments:
  -h, --help            show this help message and exit
  --threads THREADS     number of threads MBG assembles with.
  --mbg MBG             path to MBG executable.
  --gfatk GFATK         path to gfatk executable.
  --organelle {mitochondria,chloroplast,both}
                        assemble a mitochondrial or chloroplast genome, or both.
  --prefix [PREFIX]     prefix for all of the output files. otherwise a random UUID is generated.
  --dir [DIR]           directory where all output directories are to store their output.
  --gfa [GFA]           if you already have an MBG output GFA, use this entry point to specify the GFA file path.
```

It's not very configurable at the moment, but work is in progress to make the interface more configurable.

## Dependencies

Must be in PATH. Or install and provide location on the command line.

- MBG (https://github.com/maickrau/MBG; conda installation easiest.)
- gfatk (https://github.com/tolkit/gfatk/; build from source, working on making this easier to install.)
- fpma (https://github.com/tolkit/fpma/; build from source. Database in this repo also required.)
- fppa (work in progress at https://github.com/tolkit/fppa/. Nothing to do yet.)
