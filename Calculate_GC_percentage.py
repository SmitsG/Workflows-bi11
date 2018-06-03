
# Dit kwam ik toevallig tegen op internet, daarom heb ik er alvast een scriptje van gemaakt. Hebben we later nodig.
# Berekent het GC-percentage.
from Bio.SeqUtils import GC

seq = "ACTGGCCAATTGCG"

print(GC(seq))


# Dit kan je negeren. Was een probeersel van mij, maar wil het nog niet weggooien. Misschien komt het nog van pas.
#
# class Gene:
#
#     def __init__(self, gene_id):
#         self.gene_id = gene_id
#
#     def get_gene_id(self):
#         return self.gene_id
#
#     def set_gene_sequence(self, gene_sequence):
#         self.gene_sequence = gene_sequence




