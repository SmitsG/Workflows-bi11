rule read_file:
    input:
        "RNA-Seq-counts.txt"
    run:
        import re
        with open("RNA-Seq-counts.txt", 'r') as file:
            gene_ids = open("gene_ids.txt", 'w')
            line = file.readlines()
            gene_id_list = (re.split(r'\t+', str(line[1]).strip()))
            gene_id_list.remove("ID")
            gene_ids = open("gene_ids.txt", 'w')
            gene_ids.write(str(gene_id_list))

