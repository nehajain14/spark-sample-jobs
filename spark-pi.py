import sys
import random
import pandas as pd
import pyspark

sc = pyspark.SparkContext('local[*]')
samples = 2000


def inside(p):
    x, y = random.random(), random.random()
    return x * x + y * y < 1


count = sc.parallelize(range(0, samples)) \
    .filter(inside).count()
print("Pi is around %f" % (4.0 * count / samples))
print(f"Python Path: {sys.executable}")
print(f"Pandas Version: {pd.__version__}")
