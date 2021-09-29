import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("fromages.csv")
print(data)

corr_df = data.corr(method='pearson')
print("The correlation DataFrame is:")
print(corr_df, "\n")

plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True)
plt.show()

