from bioservices import *
from bioservices import ensembl
from importlib import reload

# s = Ensembl()
# res = s.get_lookup_by_id('ENSG00000157764', expand=True)
# print(res.keys())


































# for debugigng
# reload(ensembl)
# e = ensembl.Ensembl()
# res = e.get_archive('ENSG00000157764')
# print(res)
#
# print(len(e.get_info_analysis('human')))
# print(e.get_info_assembly('human')['karyotype'])
#
# res = e.get_genetree_by_member_id('ENSG00000157764', frmt='json',
#                                   nh_format='phylip')
# print(res[0:100])
#
# # If your identifier is incorrect, you'll get a 500 error code
# # returned (most probably)
# wrong = e.get_map_cds_to_region('ENST0000288602', '1..1000')
# good = e.get_map_cds_to_region('ENST00000288602', '1..1000')
# print(wrong, good['mappings'][0])

