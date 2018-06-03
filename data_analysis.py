import argparse
import ntpath
import os
import re
INFO = 'Creates a report with gene information'


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = "gene_ids.txt"
    gene_id_file_location = get_gene_ids("RNA-Seq-counts.txt", dir_path + "/" + filename)


def get_gene_ids(input_file, file_location):
    with open(input_file, 'r') as file:
        data = [i.strip('\n').split('\t') for i in open(input_file)]
        gene_id_list = []
        for i in data:
            i = i[0]
            if i.startswith("lp"):
                gene_id_list.append(i)
        file = open(file_location, "w")
        file.write(str(gene_id_list))
    return file_location






if __name__ == "__main__":
    main()

