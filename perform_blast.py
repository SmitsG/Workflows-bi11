from Bio.Blast import NCBIWWW, NCBIXML
import argparse
import os


def main():
    # Controls program
    args = parse_args()
    remove_old_result_file(args.output)
    blast_controller(args.output,
                     protein_sequence=[args.input], hitlist_size = 1)


def remove_old_result_file(output_path):
    """
    #output_path=path of the file that needs to be removed
    """
    if os.path.exists(output_path):
        os.remove(output_path)


def blast_controller(output, protein_sequence, hitlist_size):
    """
    # It is not possible to BLAST multiple sequences at once, so a for loop is needed
    # Calls perform_blast
    # Returns empty string
    """
    for item in protein_sequence:
        perform_blast(output, program="blastp", database="nr", sequence=item, hitlist_size=hitlist_size)
    return ""


def perform_blast(output, program, database, sequence, hitlist_size):
    """
    Called from blast_controller. Performs BLAST and writes to output file
    output= path for the output file
    program=the BLAST program to be used
    database=the database to BLAST against
    sequence=the sequence to be blasted
    hitlist_size=maximum number of hits
    """
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
    INFO = 'perform_blast'
    parser = argparse.ArgumentParser(description=INFO,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("--input",
                        type=str,
                        required=False,
                        default="output.fasta",
                        help="(Absolute) input file path")

    parser.add_argument("--output",
                        type=str,
                        required=False,
                        default="blast_output.xml",
                        help="(Absolute) output file path")

    # parse all arguments
    args = parser.parse_args()

    return args

main()
