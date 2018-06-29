from Bio import Entrez, Medline



def main():
    email = "silleke_frits@hotmail.com"
    ids_protein = search_entrez(email=email, db="protein", retmax=5, term="RAS", rettype="fasta")
    ids_pubmed = search_entrez(email=email, db="pubmed", retmax=10, term="RAS MAPK pathway", rettype="fasta")
    records_list_protein = fetch_results(email=email, db="protein", ids=ids_protein, rettype="fasta", retmode="xml")
    records_list_pubmed = parseMedlineRecords(ids_pubmed)
    get_sequence_and_write_to_fasta(records_list_protein)
    blast_results = blast_controller(ids_protein)


def search_entrez(email, db, retmax, term, rettype):
    Entrez.email = email
    handle = Entrez.esearch(db=db, retmax=retmax, term=term, rettype=rettype)
    records = Entrez.read(handle)
    IDs = records['IdList']
    handle.close()
    return IDs


def fetch_results(email, db, ids, rettype, retmode):
    Entrez.email = email
    handle = Entrez.efetch(db=db, id=ids, rettype=rettype, retmode=retmode)
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





def parseMedlineRecords(idlist):
    handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    return (records)


main()
