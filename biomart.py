from bioservices import biomart
import pandas as pd
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# reload(biomart)

s = biomart.BioMart()

# First, we need to know the datasets of ensembl database
# From the Ensembl web page, the database is "Ensembl genes" but it looks like "ensembl" is enough
datasets = s.datasets("ensembl")
print(datasets)

# From the list of datasets, the suggested name is "Homo sapiens genes"
# Can we find it ?
for d in datasets:
    if 'sapiens' in d.lower():
        print(d)

#What are the filters ?
filters = s.filters('hsapiens_gene_ensembl')
print(filters['ensembl_gene_id'])

attributes = s.attributes('hsapiens_gene_ensembl')

# Let us first build the XML request
# Note that the list of identifiers should be actually a string separated by commas
s.new_query()
s.add_dataset_to_xml('hsapiens_gene_ensembl')
s.add_attribute_to_xml('affy_hc_g110')
s.add_attribute_to_xml('entrezgene')
s.add_attribute_to_xml('hgnc_symbol')
s.add_attribute_to_xml('ensembl_gene_id')
s.add_filter_to_xml('ensembl_gene_id', 'ENSG00000162367,ENSG00000187048')
xml = s.get_xml()
print(xml)

# now we call the requests itself
res = s.query(xml)
print(res)

df = pd.read_csv(StringIO.StringIO(res), sep="\t", header=None)
df.columns=['affyhc_g110', 'entrezgene', 'hgnc_symbol', 'ensembl_gene_id']
df = df.drop_duplicates()
df = df.set_index('ensembl_gene_id')
# df.ix['ENSG00000162367']['hgnc_symbol']
print(df)

