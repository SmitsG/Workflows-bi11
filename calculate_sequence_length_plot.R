library("Biostrings")
indices = fasta.index("output.fasta")
plot(indices$recno, indices$seqlength)
