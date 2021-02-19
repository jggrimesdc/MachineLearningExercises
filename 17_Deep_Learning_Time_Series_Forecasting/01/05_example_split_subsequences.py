# example of splitting a univariate sequence into subsequences
from numpy import array

# define the dataset
data = list()
n = 5000
for i in range(n):
    data.append([i + 1, (i + 1) * 10])
data = array(data)
# drop time
data = data[:, 1]
# split into samples (e.g. 5000/200 = 25)
samples = list()
length = 200
# step over the 5,000 in jumps of 200
for i in range(0, n, length):
    # grab from i to i + 200
    sample = data[i:i + length]
    samples.append(sample)
print(len(samples))
