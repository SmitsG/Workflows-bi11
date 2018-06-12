#!/usr/bin/env python
import os
import argparse


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    args = parse_args(dir_path)
    print('{}'.format(args))
    get_gene_ids(args.inputfile, args.output)


def get_gene_ids(inputfile, output):
    with open(inputfile, 'r') as file:
        data = [i.strip('\n').split('\t') for i in open(inputfile)]
        gene_id_list = []
        for i in data:
            i = i[0]
            if i.startswith("lp"):
                gene_id_list.append(i)
        file = open(output, "w")
        file.write(str(gene_id_list))


def parse_args(dir_path):
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """
    INFO = 'Creates a report with gene information'
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--inputfile",
                        type=str,
                        required=True,
                        default=dir_path + "/rna_seq_data.txt",
                        help="Absolute input file path")

    parser.add_argument("--output",
                        type=str,
                        required=False,
                        default=dir_path + "/ids_locus.txt",
                        help="Absolute file location")

    # parse all arguments
    args = parser.parse_args()

    return args


main()

