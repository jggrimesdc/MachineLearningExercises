# downsample to quarterly intervals
from matplotlib import pyplot
from pandas import datetime
from pandas import read_csv


def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


series = read_csv('shampoo-sales.csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
resample = series.resample('Q')
quarterly_mean_sales = resample.mean()
print(quarterly_mean_sales.head())
quarterly_mean_sales.plot()
pyplot.show()
