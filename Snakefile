from snakemake.utils import min_version
min_version("3.2")

rule uniprot:
    input:
    output:
    shell:
        "python.py"