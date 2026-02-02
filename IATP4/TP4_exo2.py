import random
import pandas as pandasLib

DataFrame = pandasLib.read_csv("donnevrai.csv")
DataFrame["danger"] = DataFrame["danger"].map({"safe": 0, "danger": 1})
X = DataFrame["vitesse"].tolist()
Y = DataFrame["danger"].tolist()

w = random.randint(-10, 10)
b = random.randint(-10, 10)

print(f"w: {w}, b: {b}")
print(X[:5], Y[:5])