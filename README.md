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
  - For the chloroplast, if the number of segments is not equal to 1 (complete genome assembled) or 3 (LSC, SSC, IR's), we exit.
- Linearise the subgraph.
- Annotate the linearised organelle genome to see if it's complete.

### CLI usage

```txt
usage: pmpap.py [-h] [--mbg MBG] [--mbg-threads MBG_THREADS] [--mbg-k MBG_K] [--mbg-a MBG_A]
                [--mbg-w MBG_W] [--mbg-u MBG_U] [--gfatk GFATK]
                [--organelle {mitochondria,chloroplast,both}] [--prefix [PREFIX]] [--dir [DIR]]
                [--gfa [GFA]]
                [reads]

PMPAP: Plant Mitochondrial/Plastid Assembly Pipeline: https://github.com/tolkit/plant-organellome-
assembly

positional arguments:
  reads                 the raw reads to be processed. gzipped or otherwise. (default: None)

optional arguments:
  -h, --help            show this help message and exit
  --mbg MBG             path to MBG executable. (default: MBG)
  --mbg-threads MBG_THREADS
                        number of threads MBG assembles with. (default: 10)
  --mbg-k MBG_K         the k option value which MBG will assemble with. This is the kmer size.
                        (default: 5001)
  --mbg-a MBG_A         the a option value which MBG will assemble with. This is the minimum kmer
                        abundance. (default: 5)
  --mbg-w MBG_W         the w option value which MBG will assemble with. This is the window size,
                        cannot be larger than k - 30. (default: 250)
  --mbg-u MBG_U         the u option value which MBG will assemble with. This is the minimum unitig
                        abundance. (default: 150)
  --gfatk GFATK         path to gfatk executable. (default: gfatk)
  --organelle {mitochondria,chloroplast,both}
                        assemble a mitochondrial or chloroplast genome, or both. (default:
                        mitochondria)
  --prefix [PREFIX]     prefix for all of the output files. otherwise a random UUID is generated.
                        (default: None)
  --dir [DIR]           directory where all output directories are to store their output. (default:
                        None)
  --gfa [GFA]           if you already have an MBG output GFA, use this entry point to specify the
                        GFA file path. (default: None)
```

Main MBG parameters which seem to affect the assembly are included in the command line.

## Dependencies

Must be in PATH. Or install and provide location on the command line.

- MBG (https://github.com/maickrau/MBG; conda installation easiest.)
- gfatk (https://github.com/tolkit/gfatk/; build from source, working on making this easier to install.)
- fpma (https://github.com/tolkit/fpma/; build from source. Database in this repo also required.)
- fppa (work in progress at https://github.com/tolkit/fppa/. Nothing to do yet.)
