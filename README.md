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

# Compte Rendu Business Decision

Le but de ce TP est d'utiliser plusieurs méthodes d'analyses de données.
Pour chaque technique d’analyse, nous devons choisir un ou plusieurs exemples adaptés, définir les objectifs, définir une démarche d’analyse et présenter l’ensemble des outils permettant d’expliquer et quantifier les résultats (ex : corrélations, contributions…)

##ACP : étude d’un tableau individus-caractères quantitatifs

##AFC : étude d’un tableau de contingence
### Objectif
L'objectif de la méthode AFC est que l'on va regarder les corrélations entre les lignes pour ensuite situer sur un graphique les caractéristiques qui reviennent le plus et quels sont les noms des lignes associés.

###Démarches

La première étape est de formatter les données pour avoir un tableau exploitable.
On garde les labels sur le côté pour pouvoir afficher un plot cohérent par la suite.



##Classification : étude d’un tableau individus-caractères quantitatifs

##Analyse discriminante

##Anova