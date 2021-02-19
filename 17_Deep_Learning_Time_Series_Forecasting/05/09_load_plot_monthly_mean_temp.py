# load and plot monthly mean temp dataset
from matplotlib import pyplot
from pandas import read_csv

# load
series = read_csv('monthly-mean-temp.csv', header=0, index_col=0)
# summarize shape
print(series.shape)
# plot
pyplot.plot(series)
pyplot.xticks([])
pyplot.show()
