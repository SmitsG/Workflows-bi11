from Bio.Blast import NCBIWWW, NCBIXML
import argparse


def main():
    print("hello")
    args = parse_args()
    print(args.input)
    print(args.output)
    blast_handle_list = blast_controller(args.output,
        ids_protein=["MPRHYHYQPSRELHVVVLGAAQFVHNEWIESYDPTIEDSYRTQLQVDGRQVILEILDTAGTEQFVAMRDLYMKTGQGFL",
                     "MANDEYDFLFKVVLIGDSGVGKSNLLSRFTRNEFNLDSKSTIGVEFATRSIQVDSKTIKAQIWDTAGQERYRAITSAYY"])


# It is not possible to BLAST multiple sequences at once, so a for loop is needed
def blast_controller(output, ids_protein):
    blast_handle_list = []
    for item in ids_protein:
        handle_blast = perform_blast(output, program="blastp", database="nr", sequence=item)
        blast_handle_list.append(handle_blast)
    return blast_handle_list


# Called from blast_controller
def perform_blast(output, program, database, sequence):
    handle = NCBIWWW.qblast(program=program, database=database, sequence=sequence)
    with open(output, "a") as out_handle:
        out_handle.write(handle.read())
        out_handle.close()
    handle.close()
    return handle


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
