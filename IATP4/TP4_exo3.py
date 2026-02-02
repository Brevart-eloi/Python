import random
import pandas as pandasLib

def Zpredict(x):
    z = w * x + b
    if z >= 0:
        return 1
    else:
        return 0
    

DataFrame = pandasLib.read_csv("donnevrai.csv")
DataFrame["danger"] = DataFrame["danger"].map({0:"safe", 1: "danger"})
X = DataFrame["vitesse"].tolist()
Y = DataFrame["danger"].tolist()

w = random.randint(-10, 10)
b = random.randint(-10, 10)

print(f"w: {w}, b: {b}")
print(X[:5], Y[:5])