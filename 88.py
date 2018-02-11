import pandas

data = pandas.read_csv("countries-by-area.txt",",", index_col=None)
data["densely"] = data["population_2013"]/data["area_sqkm"]
data = data.sort_values("densely",ascending=False)

# data = data[:5]["country"]
# for country in data:
#     print(country)

for index, row in data[:5].iterrows():
    print(row["country"])