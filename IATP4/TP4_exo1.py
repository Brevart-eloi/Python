import pandas as pandasLib
DataFrame = pandasLib.read_csv("donnevrai.csv")
DataFrame["danger"] = DataFrame["danger"].map({0:"safe", 1: "danger"})
X = DataFrame["vitesse"].tolist()
Y = DataFrame["danger"].tolist()