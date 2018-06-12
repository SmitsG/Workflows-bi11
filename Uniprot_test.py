from bioservices.uniprot import UniProt

u = UniProt(verbose=False)
print(u.mapping(fr="P_ENTREZGENEID", to="ID", query='7124'))
# info = u.search("lp_0001", frmt="txt")
# info = u.search("lp_0001", columns="id")
#info = u.search("lp_0001", frmt="txt")
#print(type(info))

#entries = ["lp_001", "lp_0002", "lp_0004", "lp_0005"]

#Krijg veel te veel resultaten. Kan je even kijken? Bron: http://bioservices.readthedocs.io/en/master/references.html#bioservices.uniprot.UniProt
#info = u.get_df(entries, nChunk=100, organism="Lactobacillus plantarum")
#print(info)

