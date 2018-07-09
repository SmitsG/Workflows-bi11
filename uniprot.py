#!/usr/bin/env python
import argparse
from bioservices import *


def main():
    args = parse_args()
    get_uniprot_annotation(args.id, args.query)


def get_uniprot_annotation(id, query):
    """
    function that gets some uniprot information
    :param id: uniprot id
    :param query: uniprot query
    :return:
    """
    u = UniProt()
    # get the fasta of the id.
    print(u.get_fasta(id))
    # get query results
    print(u.search(query, limit=5))
    df = u.get_df(id)
    # print Entry ids
    print(df)


INFO = 'Uniprot'


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """

    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--id",
                        type=str,
                        required=False,
                        default="P04637",
                        help="uniprot id")

    parser.add_argument("--query",
                        type=str,
                        required=False,
                        default="P53 and taxonomy:human",
                        help="uniprot query")

    # parse all arguments
    args = parser.parse_args()

    return args

main()