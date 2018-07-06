from Bio.Blast import NCBIWWW, NCBIXML


def main():
    blast_results = blast_controller()
    # perform_blast(program, database, sequence)


def blast_controller(ids_protein):
    blast_results = []
    for item in ids_protein:
        handle_blast = perform_blast(program="blastp", database="nr", sequence=item)
        blast_result = parse_blast_record(handle_blast)
        blast_results.append(blast_result)
    return blast_results


def perform_blast(program, database, sequence):
    handle = NCBIWWW.qblast(program=program, database=database, sequence=sequence)
    handle.close()
    return handle


def parse_blast_record(handle):
    results = NCBIXML.parse(handle)
    results.close()
    return results
