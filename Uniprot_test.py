from bioservices.uniprot import UniProt
u = UniProt(verbose=False)
#print(u.mapping(fr="ACC+ID", to="KEGG_ID", query='P43403'))
#info = u.search("lp_0001", frmt="txt")
info = u.search("lp_0001", columns="id")
print(info)




