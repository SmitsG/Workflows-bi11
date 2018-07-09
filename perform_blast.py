from Bio.Blast import NCBIWWW, NCBIXML
import argparse


def main():
    args = parse_args()
    blast_controller(args.output,
        ids_protein=["MPRHYHYQPSRELHVVVLGAAQFVHNEWIESYDPTIEDSYRTQLQVDGRQVILEILDTAGTEQFVAMRDLYMKTGQGFL",
                     "MANDEYDFLFKVVLIGDSGVGKSNLLSRFTRNEFNLDSKSTIGVEFATRSIQVDSKTIKAQIWDTAGQERYRAITSAYY"], hitlist_size = 1)


# It is not possible to BLAST multiple sequences at once, so a for loop is needed
def blast_controller(output, ids_protein, hitlist_size):
    for item in ids_protein:
        perform_blast(output, program="blastp", database="nr", sequence=item, hitlist_size=hitlist_size)
    return ""


# Called from blast_controller
def perform_blast(output, program, database, sequence, hitlist_size):
    handle = NCBIWWW.qblast(program=program, database=database, sequence=sequence, hitlist_size=hitlist_size)
    with open(output, "a") as out_handle:
        out_handle.write(handle.read())
        out_handle.close()
    handle.close()



INFO = 'Arguments workflow project'


def parse_args():
    """
    Argument parser
    :return: args: All arguments are parsed to the args.
    """
    INFO = 'Creates a report with gene information'
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--input",
                        type=str,
                        required=False,
                        default="output.fasta",
                        help="Absolute input file path")

    parser.add_argument("--output",
                        type=str,
                        required=False,
                        default="blast_output.xml",
                        help="Absolute input file path")

    # parse all arguments
    args = parser.parse_args()

    return args

main()
