import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # MÅSTE BORT


filePath = 'data/housing.csv'
housing_df = pd.read_csv(filePath)

print(housing_df)