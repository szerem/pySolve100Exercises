import pandas

data = pandas.read_csv("http://atest.5v.pl/sampledata.txt")
print(data)
data_2 = data * 2
print(data_2)
data_2.to_csv("sampledata_x_2.txt", index=None)