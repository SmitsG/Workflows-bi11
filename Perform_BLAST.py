from Bio.Blast import NCBIWWW, NCBIXML


def main():
    blast_handle_list = blast_controller(
        ids_protein=["MPRHYHYQPSRELHVVVLGAAQFVHNEWIESYDPTIEDSYRTQLQVDGRQVILEILDTAGTEQFVAMRDLYMKTGQGFL",
                     "MANDEYDFLFKVVLIGDSGVGKSNLLSRFTRNEFNLDSKSTIGVEFATRSIQVDSKTIKAQIWDTAGQERYRAITSAYY"])
    #write_blast_output_to_xml(blast_handle_list)


# It is not possible to BLAST multiple sequences at once, so a for loop is needed
def blast_controller(ids_protein):
    blast_handle_list = []
    for item in ids_protein:
        handle_blast = perform_blast(program="blastp", database="nr", sequence=item)
        blast_handle_list.append(handle_blast)
    return blast_handle_list


# Called from blast_controller
def perform_blast(program, database, sequence):
    handle = NCBIWWW.qblast(program=program, database=database, sequence=sequence)
    with open("blast_output.xml", "a") as out_handle:
        out_handle.write(handle.read())
        out_handle.close()
    handle.close()
    return handle

main()
