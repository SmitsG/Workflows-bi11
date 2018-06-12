# from Bio import Entrez
from snakemake.utils import min_version
min_version("3.2")

rule connect_to_entrez:
    output:
        "output.fasta"
    script:
        "Connect_to_entrez.py"

rule R:
    input:
        "output.fasta"
    script:
        "Calculate_sequence_length_plot.R"

rule get_gene_ids:
    input:
        "rna_seq_data.txt"
    output:
        "/home/gerwin/miniconda3/envs/workflow_project/test_workflow/ids_locus.txt"
    shell:
        "./get_locus_gene_ids.py --inputfile {input} --output {output}"
