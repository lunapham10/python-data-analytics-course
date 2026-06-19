import numpy as np
import pandas as pd

file = "Iris.csv"

try:
    df = pd.read_csv(file)

    species_col = None
    petal_width_col = None

    for col in df.columns:
        col_lower = col.lower()
        if "species" in col_lower:
            species_col = col
        elif "petalwidthcm" in col_lower:
            petal_width_col = col
    
    filted_df = df[(df[petal_width_col] == 1.5) & (df[species_col] == "Iris-versicolor")]

    print(len(filted_df))
except FileNotFoundError:
    print(f"Error: Folder doesn't have file named '{file}'")

