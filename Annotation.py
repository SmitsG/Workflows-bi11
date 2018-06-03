import sys

from Bio import Entrez

# *Always* tell NCBI who you are
Entrez.email = "your email here"


def retrieve_annotation(id_list):
    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information.
    Returns a list of dictionaries with the annotations."""

    request = Entrez.epost("gene", id=",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError as e:
        # FIXME: How generate NAs instead of causing an error with invalid IDs?
        print("An error occurred while retrieving the annotations.")
        print("The error returned was %s" % e,
              sys.exit(-1))

    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esummary(db="gene", webenv=webEnv, query_key=
    queryKey)
    annotations = Entrez.read(data)
    print("Retrieved %d annotations for %d genes" % (len(annotations),
                                                     len(id_list)))
    return annotations





def print_data(annotation):
    gene_information = []

    # Dit is een poging om de datastructuur te bekijken
    for key, value in annotation.items():
        print(key, value)

    # Hier gaat het mis. Gene_data is een string.
    for gene_data in annotation:
        #gene_symbol = gene_data["NomenclatureSymbol"]
        gene_symbol = gene_data[0]
        print(gene_data)
        gene_information.append(gene_symbol)


# Dit is een willekeurige ID om het script te testen. De IDs van Tilman werken namelijk niet. Moet ik nog converteren
id_list = ["820216"]

# Hier wordt de annotatie daadwerkelijk opgehaald uit Entrez
annotations = retrieve_annotation(id_list)

# Dit is een functie om de annotatie te bekijken en op te slaan. Moet nog werkend gemaakt worden.
print_data(annotations)