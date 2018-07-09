from Bio.KEGG import Enzyme
from Bio.KEGG import REST
from bioservices.kegg import KEGG

request = REST.kegg_get("ec:5.4.2.2")
open("ec_5.4.2.2.txt", "w").write(request.read())
records = Enzyme.parse(open("ec_5.4.2.2.txt"))
record = list(records)[0]
print(record.classname)