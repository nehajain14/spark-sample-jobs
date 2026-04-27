from pyspark.sql import SparkSession
from pyspark.sql.functions import rand, col
import pandas as pd
import sys

# Initialize Spark
spark = SparkSession.builder.appName("ComplexShuffleTest").getOrCreate()

# Print Environment Info for verification
print(f"Python Path: {sys.executable}")
print(f"Pandas Version: {pd.__version__}")

# 1. Disable Broadcast Join to force a SHUFFLE
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", -1)

# 2. Create Dataset A (1 million rows)
df_a = spark.range(0, 1000000).withColumn("join_key", (rand() * 1000).cast("int")) \
            .withColumn("data_a", rand())

# 3. Create Dataset B (1 million rows)
df_b = spark.range(0, 1000000).withColumn("join_key", (rand() * 1000).cast("int")) \
            .withColumn("data_b", rand())

# 4. Perform a Shuffle Sort-Merge Join
print("Starting Shuffle Join...")
joined_df = df_a.join(df_b, "join_key")

# 5. Perform a heavy aggregation
result = joined_df.groupBy("join_key").avg("data_a", "data_b").orderBy("join_key")

# 6. Trigger action and print result
print(f"Total Joined Rows: {joined_df.count()}")
result.show(5)

spark.stop()
