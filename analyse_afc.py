import pandas as pd
from fanalysis.ca import CA
import matplotlib.pyplot as plt

# We create the data frame by importing the CSV file
df = pd.read_csv("fromages.csv").dropna()
#print(df)
labels = df["Fromages"]
df = df.drop(columns=["Fromages"])

X = df.to_numpy()
my_ca = CA(row_labels=labels, col_labels=df.columns.values)
my_ca.fit(X)

#print(my_ca.eig_)

#my_ca.plot_eigenvalues()
my_ca.plot_eigenvalues(type="percentage")
#my_ca.plot_eigenvalues(type="cumulative")


df_rows = my_ca.row_topandas()
#print(df_rows)

my_ca.mapping(num_x_axis=1, num_y_axis=2)


my_ca.mapping_col(num_x_axis=1, num_y_axis=1)
my_ca.mapping_row(num_x_axis=1, num_y_axis=1)
my_ca.mapping(1, 2, figsize=(10, 8))