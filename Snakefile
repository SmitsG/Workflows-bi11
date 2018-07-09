import os
import glob
import argparse
import pickle
import Bio
from bioservices import *
from kegg import get_kegg_annotation
from kegg import amount_pathway_genes
from kegg import show_pathway

# make sure the done directory is empty.

rule all:
    input:
        "done_files/get_sequence.done",
        "done_files/perform_blast.done",
        "done_files/search_pubmed.done",
        "done_files/calculate_sequence_length_plot.done",
        "done_files/chembl.done",
        "done_files/uniprot.done",
        "done_files/ensembl.done",
        "done_files/kegg.done"

# calculate the length of a sequence and plot
rule calculate_sequence_length_plot:
    output:
        touch("done_files/calculate_sequence_length_plot.done")
    script:
        "calculate_sequence_length_plot.R"

# get (protein) sequences and create a (output) fasta file.
rule get_sequences:
    output:
        "output.fasta",
        touch("done_files/get_sequence.done")
    shell:
        "python ./get_sequences.py --output {output[0]}"

# uses the output file create by get_sequence and performs a blast.
rule perform_blast:
    input:
        "output.fasta"
    output:
        "blast_output.xml",
        touch("done_files/perform_blast.done")
    shell:
        "python ./perform_blast.py --input {input} --output {output[0]}"

# get some pubmed info
rule search_pubmed:
    output:
        "PubMed_output.txt",
        touch("done_files/search_pubmed.done")
    shell:
        "python ./search_pubmed.py --output {output[0]}"


# prove of concept.
# Sometimes it is necessary to enforce some rule execution order without real file dependencies.
# With the touch flag, Snakemake touches (i.e. creates or updates) the file mytask.done after mycommand has finished
# successfully.

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

# gets some information out of kegg
rule kegg:
    output: touch("done_files/kegg.done")
    priority: 250
    run:
        "./kegg.py"

