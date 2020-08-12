import pandas as pd
import numpy as np
from functools import partial
from janitor import clean_names


#Download Data
# ------------------------------------------------------------
# Adelie penguin data from: https://doi.org/10.6073/pasta/abc50eed9138b75f54eaada0841b9b86
uri_adelie = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.219.3&entityid=002f3893385f710df69eeebe893144ff"

# Gentoo penguin data from: https://doi.org/10.6073/pasta/2b1cff60f81640f182433d23e68541ce
uri_gentoo = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.220.3&entityid=e03b43c924f226486f2f0ab6709d2381"

# Chinstrap penguin data from: https://doi.org/10.6073/pasta/409c808f8fc9899d02401bdb04580af7
uri_chinstrap = "https://portal.edirepository.org/nis/dataviewer?packageid=knb-lter-pal.221.2&entityid=fe853aa8f7a59aa84cdd3197619ef462"

uris = [uri_adelie, uri_gentoo, uri_chinstrap]

dfs = list(map(partial(pd.read_csv,na_values = ["", "NA", "."]),uris))

penguins_raw_df = pd.concat(dfs)

# Clean Data
#--------------------------------------------------------------

penguins = (
 penguins_raw_df
 .pipe(clean_names)
)
