from Bio import Entrez


rule all:
    input:
        "done_files/get_sequences.done"

rule get_sequences:
    output:
        touch("done_files/get_sequences.done")
    script:
        "./get_sequences.py"


