# upsample to daily intervals with spline interpolation
from matplotlib import pyplot
from pandas import datetime
from pandas import read_csv


def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


series = read_csv('shampoo-sales.csv', header=0, index_col=0, parse_dates=True, squeeze=True, date_parser=parser)
upsampled = series.resample('D').mean()
interpolated = upsampled.interpolate(method='spline', order=2)
print(interpolated.head(32))
interpolated.plot()
pyplot.show()
