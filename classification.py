import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

df = pd.read_csv("fromages.csv").dropna()
#print(df)
labels = df["Fromages"]
df = df.drop(columns=["Fromages"])

Z = linkage(df, method='ward', metric='euclidean')

plt.title("CAH")
dendrogram(Z, labels=labels, orientation='left', color_threshold=0)
plt.show()