rule all:
    input:
        "done_files/get_sequence.done",
        "done_files/perform_blast.done",
        "done_files/search_pubmed.done"

rule get_sequences:
    output:
        "output.fasta",
        touch("done_files/get_sequence.done")
    shell:
        "python ./get_sequences.py --output {output[0]}"

rule perform_blast:
    input:
        "output.fasta"
    output:
        "blast_output.xml",
        touch("done_files/perform_blast.done")
    shell:
        "python ./perform_blast.py --input {input} --output {output[0]}"

rule search_pubmed:
    output:
        "PubMed_output.txt",
        touch("done_files/search_pubmed.done")
    shell:
        "python ./search_pubmed.py --output {output[0]}"


