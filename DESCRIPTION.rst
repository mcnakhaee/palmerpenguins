
palmerpenguins
~~~~~~~~~~~~~~~~~~~~~~
The Palmer penguins dataset by Allison Horst, Alison Hill, and Kristen Gorman was first made publicly available as an R package. The goal of the Palmer Penguins dataset is to replace the highly overused Iris dataset for data exploration & visualization.
Using this python package you can easily load the Palmer penguins into your python environment.


Overview
~~~~~~~~~~~~~~~~~~~~~~
Size measurements, clutch observations, and blood isotope ratios for 344 adult foraging Adelie, Chinstrap, and Gentoo penguins observed on islands in the Palmer Archipelago near Palmer Station, Antarctica. Data were collected and made available by Dr. Kristen Gorman and the Palmer Station Long Term Ecological Research (LTER) Program.

Examples
~~~~~~~~~~~~~~~~~~~~~~
```
import pandas as pd
import seaborn as sns
from palmerpenguins import load_penguins
sns.set_style('whitegrid')
```



```python
penguins = load_penguins()
```


g = sns.boxplot(x = 'island',
            y ='body_mass_g',
            hue = 'species',
            data = penguins,
            palette=['#FF8C00','#159090','#A034F0'],
            linewidth=0.3)
g.set_xlabel('Island')
g.set_ylabel('Body Mass')



License
~~~~~~~~~~~~~~~~~~~~~~
Data are available by
[CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/) license in
accordance with the [Palmer Station LTER Data Policy](http://pal.lternet.edu/data/policies)
and the
[LTER Data Access Policy for Type I data](https://lternet.edu/data-access-policy/).




Bibliography
~~~~~~~~~~~~~~~~~~~~~~
Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental
Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3):
e90081. https://doi.org/10.1371/journal.pone.0090081

See also
~~~~~~~~~~~~~~~~~~~~~~
More information about the dataset is available in
[its official documentation](https://allisonhorst.github.io/palmerpenguins/).

The Palmer penguins dataset in Julia:
https://github.com/devmotion/PalmerPenguins.jl
