import pandas as pandasLib
DataFrame = pandasLib.read_csv("donnevrai.csv")
DataFrame["danger"] = DataFrame["danger"].map({"safe": 0, "danger": 1})
X = DataFrame["vitesse"].tolist()
Y = DataFrame["danger"].tolist()