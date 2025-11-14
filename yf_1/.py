import pandas as pd


mydataset = {"names": ["Bildad", "Chilli", "Prime"], "ages": [20, 17, 5]}

df = pd.DataFrame(mydataset)

df["places"] = [5, 10, 20]
df["add"] = df["places"] + df["ages"]
print(df.to_string())
