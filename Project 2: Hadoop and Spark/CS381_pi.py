from pyspark import SparkConf, SparkContext
import random

# create Spark context
conf = SparkConf().setAppName("MonteCarloPi")
sc = SparkContext(conf=conf)

# set the number of samples to generate
num_samples = 1000000

# generate random points within a square of size 2
points = sc.parallelize(range(num_samples)).map(lambda i: (random.uniform(-1, 1), random.uniform(-1, 1)))

# count the number of points within the unit circle
num_inside_circle = points.filter(lambda point: point[0]**2 + point[1]**2 <= 1).count()

# estimate the value of pi as 4 times the ratio of points within the circle to total points
pi_estimate = 4.0 * num_inside_circle / num_samples

# print the estimated value of pi
print("Estimated value of pi:", pi_estimate)