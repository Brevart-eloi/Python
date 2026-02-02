import random
import pandas as pandasLib

def Zpredict(x):
    z = w * x + b
    if z >= 0:
        return 1
    else:
        return 0
    

DataFrame = pandasLib.read_csv("donnevrai.csv")
DataFrame["danger"] = DataFrame["danger"].map({"safe": 0, "danger": 1})
X = DataFrame["vitesse"].tolist()
Y = DataFrame["danger"].tolist()

w = random.randint(-10, 10)
b = random.randint(-10, 10)

print(f"w: {w}, b: {b}")
print(X[:5], Y[:5])

for x_val, y_attendu in zip(X, Y):
    y_pred = Zpredict(x_val)
    erreur = y_attendu - y_pred
    print(f"x = {x_val}, y = {y_attendu}, y_pred = {y_pred}, erreur = {erreur}")