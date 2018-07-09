from Bio import Entrez, Medline


def main():
    id_list = search_entrez(email="silleke_frits@hotmail.com", db="pubmed", retmax=10, term="RAS MAPK pathway", rettype="medline")
    records = parseMedlineRecords(id_list)


def search_entrez(email, db, retmax, term, rettype):
    Entrez.email = email
    handle = Entrez.esearch(db=db, retmax=retmax, term=term, rettype=rettype)
    records = Entrez.read(handle)
    IDs = records['IdList']
    handle.close()
    return IDs


def parseMedlineRecords(id_list):
    handle = Entrez.efetch(db="pubmed", id=id_list, rettype="medline", retmode="text")
    records = Medline.parse(handle)
    records = list(records)
    return records

main()