# seed the pseudorandom number generator
from numpy.random import rand
from numpy.random import seed

# seed random number generator
seed(1)
# generate some random numbers
print(rand(3))
# reset the seed
seed(1)
# generate some random numbers
print(rand(3))
