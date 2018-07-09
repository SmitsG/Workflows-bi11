
rule all:
    input:
        "done_get_sequences.done",

rule get_sequences:
    output:
        "protein_sequences.fasta"
    script:
        "Get_protein_sequence_fasta.py"