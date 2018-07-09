import os
import glob
import argparse
import pickle
import Bio
from bioservices import *
from kegg import get_kegg_annotation
from kegg import amount_pathway_genes
from kegg import show_pathway


# prove of concept.
# Sometimes it is necessary to enforce some rule execution order without real file dependencies.
# With the touch flag, Snakemake touches (i.e. creates or updates) the file mytask.done after mycommand has finished
# successfully.
rule all:
    input:
        "done_files/chembl.done",
        "done_files/uniprot.done",
        "done_files/ensembl.done",
        "done_files/kegg.done"

# get some information out of chembl
rule chembl:
    output: touch("done_files/chembl.done")
    priority: 1000
    script:
        "./chembl.py"

# get some information out of uniprot
rule uniprot:
    output: touch("done_files/uniprot.done")
    priority: 750
    shell:
        "./uniprot.py"

# gets some information out of ensembl
rule ensembl:
    output: touch("done_files/ensembl.done")
    priority: 500
    script:
        "./ensembl.py"

<<<<<<< Updated upstream
# gets some information out of kegg
rule kegg:
    output: touch("done_files/kegg.done")
    priority: 250
    run:
        "./kegg.py"
=======

>>>>>>> Stashed changes
