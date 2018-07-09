rule all:
    input:
        "done_files/get_sequence.done",
        "done_files/perform_blast.done"

rule get_sequences:
    output:
        "output.fasta",
        touch("done_files/get_sequence.done")
    script:
        "./get_sequences.py"

rule perform_blast:
    input:
        "output.fasta"
    output:
        "blast_output.xml",
        touch("done_files/perform_blast.done")
    shell:
        "python ./perform_blast.py --input {input} --output {output[0]}"

