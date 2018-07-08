import os
import glob
import argparse
import pickle
import Bio
from bioservices import *

rule all:
    input:
        "chembl.done",
        "uniprot.done",
        "ensemble.done"

rule chembl:
    output: touch("chembl.done")
    script:
        "./chembl.py"

rule uniprot:
    output: touch("uniprot.done")
    shell:
        "./uniprot.py"

rule ensemble:
    output: touch("ensemble.done")
    script:
        "./ensemble.py"