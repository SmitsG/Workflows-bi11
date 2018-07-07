from bioservices import *
from IPython.display import SVG
s = WikiPathways()
im = s.getColoredPathway("WP2320")
print(SVG(im))