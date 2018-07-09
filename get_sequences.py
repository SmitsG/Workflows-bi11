from Bio import Entrez
import argparse


def main():
    # Controls the flow of the script
    args = parse_args()
    email = "silleke_frits@hotmail.com"
    ids_protein = search_entrez(email=email, db="protein", retmax=5, term="RAS", rettype="fasta")
    records_list_protein = fetch_results(email=email, db="protein", ids=ids_protein, rettype="fasta", retmode="xml")
    get_sequence_and_write_to_fasta(args.output, records_list_protein)


def search_entrez(email, db, retmax, term, rettype):
    """
    Searches database
    email=the emailadres of the user
    db=the database to be searched
    retmax=maximum number of hits
    term=query for the database
    rettype=type of retrieval
    returns the IDs of the records that are found
    """
    Entrez.email = email
    handle = Entrez.esearch(db=db, retmax=retmax, term=term, rettype=rettype)
    records = Entrez.read(handle)
    IDs = records['IdList']
    handle.close()
    return IDs


def fetch_results(email, db, ids, rettype, retmode):
    """
    Download the results
    email=the emailadres of the user
    db=the database to be searched
    ids=the record ids
    rettype=type of retrieval
    retmode=type of the outputfile
    returns a list with records
    """
    Entrez.email = email
    handle = Entrez.efetch(db=db, id=ids, rettype=rettype, retmode=retmode)
    records = Entrez.read(handle)
    records_list = list(records)
    handle.close()
    return records_list


def get_sequence_and_write_to_fasta(output, records_list):
    """
    Writes sequences to fasta ouputfile
    output=path for output
    records_list=list with records -> sequences
    """
    genes_fasta = open(output, "w")
    count = 0
    for record in records_list:
        count += 1
        sequence = record["TSeq_sequence"]
        genes_fasta.write(">" + str(count))
        genes_fasta.write("\n")
        genes_fasta.write(sequence)
        genes_fasta.write("\n")
    genes_fasta.close()


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """
    INFO = 'get sequence in fasta format'
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--output",
                        type=str,
                        required=False,
                        default="output.fasta",
                        help="(Absolute) output file path")

    # parse all arguments
    args = parser.parse_args()

    return args

main()
