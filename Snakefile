import os
import glob
import argparse
import pickle
import Bio
from bioservices import *
from kegg import function1 as function1
from kegg import function2 as function2
from kegg import function3 as function3

rule all:
    input:
        "done_files/chembl.done",
        "done_files/uniprot.done",
        "done_files/ensemble.done",
        "done_files/kegg.done"

rule chembl:
    output: touch("done_files/chembl.done")
    script:
        "./chembl.py"

rule uniprot:
    output: touch("done_files/uniprot.done")
    shell:
        "./uniprot.py"

rule ensemble:
    output: touch("done_files/ensemble.done")
    script:
        "./ensemble.py"

rule kegg:
    output: touch("done_files/kegg.done")
    run:
        "./kegg.py"