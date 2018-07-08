#!/usr/bin/env python
import pandas as pd
from bioservices import *
import matplotlib.pyplot as plt

s = ChEMBL()
res = s.get_compounds_by_chemblId(['CHEMBL%s' % i for i in range(0,300)])
print(res[1])

# here this look a bit esoteric but what we do if to remove the 404 numbers
# and transform the data into a nice dataframe for easy plotting of some
# relevant information
df = pd.DataFrame(
    [dict(this['compound']) for this in res if this!=404],
    index=[this['compound']['chemblId'] for this in res if this!=404])

print(df)

plot = df.plot(x='molecularWeight', y='alogp', marker='o', kind='scatter',
        fontsize=20)

plt.savefig("foo.png")
plt.show(plot)
