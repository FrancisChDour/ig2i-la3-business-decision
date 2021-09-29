# ig2i-la3-business-decision

# Matrice de corrélation :
**Explications :**

//TODO

**Code complet :**
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# We create the data frame by importing the CSV file
data = pd.read_csv("fromages.csv")
print(data)

# Then we create the correlation matrix
corr_df = data.corr()
print("The correlation DataFrame is:")
print(corr_df, "\n")

# Finally, we show the matrix with colors
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True)
plt.show()
```