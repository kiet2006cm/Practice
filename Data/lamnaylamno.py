import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

file=pd.read_csv('C:\\Users\\HP\\Downloads\\Documents\\Kiet\\py\\Data\\Code\\A4_Matplotlib\\data\\california_cities.csv')

(
    latd,
    longd,
    area,
    population
    )=(
    file['latd'],
    file['longd'],
    file['area_total_km2'],
    file['population_total']
)


mpl.scatter(
    latd, longd,
    c=np.log10(population), cmap='viridis',
    s=area
)
mpl.colorbar(label='log$_{10}$(population)')
mpl.axis='equal'
mpl.show()