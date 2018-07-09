rule all:
    input:
        "done_files/get_sequences.done"

rule get_sequences:
    output:
        touch("done_files/get_sequences.done")
    script:
        "./get_sequences.py"

rule Perform_BLAST:
    input:
        "output.fasta"
    output:
        touch("output_blast.txt")
    script:
        "./Perform_BLAST.py"

