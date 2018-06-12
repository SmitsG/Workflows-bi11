library("Biostrings")
indices = fasta.index(file.choose())
plot(indices$recno, indices$seqlength)
