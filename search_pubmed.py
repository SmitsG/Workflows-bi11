from Bio import Entrez, Medline
import os
import argparse


def main():
    args = parse_args()
    id_list = search_entrez(email="silleke_frits@hotmail.com", db="pubmed", retmax=10, term="RAS MAPK pathway",
                            rettype="medline")
    records = parseMedlineRecords(id_list)
    abstracts_list = get_abstracts(args.output, records)
    print(abstracts_list)


def search_entrez(email, db, retmax, term, rettype):
    Entrez.email = email
    handle = Entrez.esearch(db=db, retmax=retmax, term=term, rettype=rettype)
    records = Entrez.read(handle)
    IDs = records['IdList']
    handle.close()
    return IDs


def parseMedlineRecords(id_list):
    """
    Function gets the (pubmed) database records.
    :param id_list: list with pubmed ids
    :return: (Pubmed) database Records
    """
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    return records


def get_abstracts(output, records):
    """
    Function gets the (pubmed) database records
    :param output: (Absolute) (pubmed) database output file path in txt
    :param records: (pubmed) database Records
    :return: list with (pubmed) abstracts
    """
    abstracts_list = []
    if os.path.exists(output):
        os.remove(output)
    count = 0
    for record in records:
        count += 1
        with open(output, "a") as pm_out:
            pm_out.write("Abstract number ")
            pm_out.write(str(count))
            pm_out.write("\n")
            abstract = record.get("AB", "?")
            pm_out.write(abstract)
            pm_out.write("\n")
            pm_out.write("\n")
    pm_out.close()
    abstracts_list.append(record.get("AB", "?"))
    return abstracts_list


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """
    INFO = 'Search (pubmed) database'
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--output",
                        type=str,
                        required=False,
                        default="PubMed_output.txt",
                        help="(Absolute) Pubmed output file path in txt")

    # parse all arguments
    args = parser.parse_args()

    return args

main()
