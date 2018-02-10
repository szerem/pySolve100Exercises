import pandas

data1 = pandas.read_csv("http://atest.5v.pl/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")


data3 = pandas.concat([data1, data2])
data3.to_csv("sampledata3.txt", index=None)
