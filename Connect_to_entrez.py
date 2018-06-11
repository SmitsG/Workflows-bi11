from Bio import Entrez


def get_ids(email):
    Entrez.email = email
    handle = Entrez.esearch(db="protein", retmax=100, term="RAS", rettype="fasta")
    records = Entrez.read(handle)
    IDs = records['IdList']
    handle.close()
    return IDs


def fetch_results(email, IDs):
    Entrez.email = email
    handle = Entrez.efetch(db="protein", id=IDs, rettype="fasta", retmode="xml")
    records = Entrez.read(handle)
    records_list = list(records)
    handle.close()
    return records_list


def get_sequence_and_write_to_fasta(records_list):
    genes_fasta = open("output.fasta", "w")
    count = 0
    for record in records_list:
        count += 1
        sequence = record["TSeq_sequence"]
        genes_fasta.write(">" + str(count))
        genes_fasta.write("\n")
        genes_fasta.write(sequence)
        genes_fasta.write("\n")
    genes_fasta.close()


email = "silleke_frits@hotmail.com"
IDs = get_ids(email)
fetch_results(email, IDs)
