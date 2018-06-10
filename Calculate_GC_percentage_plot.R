library("Biostrings")
fasta_file = readDNAStringSet(filepath = file.choose(), "fasta")
gc_percentages = letterFrequency(fasta_file, as.prob = T, letters = c("GC"))
plot(gc_percentages)