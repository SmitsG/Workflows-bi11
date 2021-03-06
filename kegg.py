from Bio.KEGG import Enzyme
from Bio.KEGG import REST
from bioservices.kegg import KEGG


def main():
    get_kegg_annotation()
    amount_pathway_genes()
    show_pathway()


def get_kegg_annotation():
    """
    Get annotation ec:5.4.2.2 from kegg database and write to txt file.
    Print annotation
    :return:
    """
    request = REST.kegg_get("ec:5.4.2.2")
    open("ec_5.4.2.2.txt", "w").write(request.read())
    records = Enzyme.parse(open("ec_5.4.2.2.txt"))
    record = list(records)[0]
    print(record.classname)


def amount_pathway_genes():
    """
    Function to measure the amount repair genes in a human pathway.
    :return:
    """
    human_pathways = REST.kegg_list("pathway", "hsa").read()

    # Filter all human pathways for repair pathways
    repair_pathways = []
    for line in human_pathways.rstrip().split("\n"):
        entry, description = line.split("\t")
        if "repair" in description:
            repair_pathways.append(entry)

    # Get the genes for pathways and add them to a list
    repair_genes = []
    for pathway in repair_pathways:
        pathway_file = REST.kegg_get(pathway).read()  # query and read each pathway

        # iterate through each KEGG pathway file, keeping track of which section
        # of the file we're in, only read the gene in each pathway
        current_section = None
        for line in pathway_file.rstrip().split("\n"):
            section = line[:12].strip()  # section names are within 12 columns
            if not section == "":
                current_section = section

            if current_section == "GENE":
                gene_identifiers, gene_description = line[12:].split("; ")
                gene_id, gene_symbol = gene_identifiers.split()

                if not gene_symbol in repair_genes:
                    repair_genes.append(gene_symbol)

    print("There are %d repair pathways and %d repair genes. The genes are:" % \
          (len(repair_pathways), len(repair_genes)))
    print(", ".join(repair_genes))


def show_pathway():
    """
    function that shows p53 pathway in KEGG
    """
    k = KEGG(verbose=True)
    k.lookfor_pathway("p53 signaling pathway - Homo sapiens (human)")
    print(k.show_pathway("path:hsa04115"))

main()