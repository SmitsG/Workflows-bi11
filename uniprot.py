#!/usr/bin/env python
import argparse
from bioservices import *


def main():
    args = parse_args()
    uniprot(args.id, args.query)


def uniprot(id, query):
    u = UniProt()
    print(u.get_fasta(id))
    print(u.search(query, limit=5))
    df = u.get_df(id)
    print(df)


INFO = 'Uniprot'


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args. The arguments will be presented in CamelCase.
    """

    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--id",
                        type=str,
                        required=False,
                        default="P43403",
                        help="uniprot id")

    parser.add_argument("--query",
                        type=str,
                        required=False,
                        default="ZAP70 and taxonomy:human",
                        help="uniprot query")

    # parse all arguments
    args = parser.parse_args()

    return args

main()
