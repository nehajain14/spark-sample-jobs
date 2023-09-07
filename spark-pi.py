import random
import pyspark

sc = pyspark.SparkContext('local[*]')
samples = 2000


def inside(p):
    x, y = random.random(), random.random()
    return x * x + y * y < 1


count = sc.parallelize(range(0, samples)) \
    .filter(inside).count()
print("Pi is around %f" % (4.0 * count / samples))
