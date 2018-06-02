import argparse
import ntpath
import os
import re
INFO = 'Creates a report with gene information'

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = "gene_ids.txt"
    gene_id_file = get_gene_ids("RNA-Seq-counts.txt", dir_path + "/" + filename)


def get_gene_ids(input_file, file_location):
    filename = ntpath.basename(file_location)
    with open(input_file, 'r') as file:
        line = file.readlines()
        gene_id_list = (re.split(r'\t+', str(line[1]).strip()))
        gene_id_list.remove("ID")
        gene_ids_txt = open(filename, 'w')
        gene_ids = []
        for gene_id in gene_id_list:
            gene_id = gene_id.split(".", 1)[0]
            if gene_id not in gene_ids:
                gene_ids.append(gene_id)
        gene_ids_txt.write(str(gene_ids))
    return file_location






if __name__ == "__main__":
    main()

