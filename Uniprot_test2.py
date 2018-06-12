import requests
from bioservices.uniprot import UniProt


#full_url = "http://www.uniprot.org/uniprot/?query=name%3A%22polymerase+alpha%22+AND+taxonomy%3Amus+AND+reviewed%3Ayes&format=list"
full_url = "http://www.uniprot.org/uniprot/?query=tnf alfa&sort=score&format=list"
results = requests.get(full_url)

if results.ok:
    text = results.text
    text = text.rstrip()
    text_splitted = text.split("\n")
    #print(len(text_splitted))

else:
    print("Something went wrong. ",  results.status_code)




u = UniProt(verbose=False)


#entries = ["lp_001", "lp_0002", "lp_0004", "lp_0005"]

#Krijg veel te veel resultaten. Kan je even kijken? Bron: http://bioservices.readthedocs.io/en/master/references.html#bioservices.uniprot.UniProt
info = u.get_df(text_splitted, nChunk=100,)
u.get
print(info)

