# load and plot monthly airline passengers dataset
from matplotlib import pyplot
from pandas import read_csv

# load
series = read_csv('monthly-airline-passengers.csv', header=0, index_col=0)
# summarize shape
print(series.shape)
# plot
pyplot.plot(series)
pyplot.xticks([])
pyplot.show()
