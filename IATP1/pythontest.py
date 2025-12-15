import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

print("✅ Tous les modules sont importés avec succès par Eloi !")
df = pd.read_csv("donneevrai.csv") 

sns.boxplot(x="danger", y="vitesse", data=df)
plt.title("Exemple graphique : vitesse selon danger")
plt.show()

    