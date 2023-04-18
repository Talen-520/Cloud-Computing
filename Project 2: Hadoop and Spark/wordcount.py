from pyspark import SparkContext, SparkConf

# create Spark context
conf = SparkConf().setAppName("WordCount")
sc = SparkContext(conf=conf)

# load file from HDFS
file = sc.textFile("hdfs:///CS381/1342.txt.utf-8")

# split each line into words
words = file.flatMap(lambda line: line.split())

# map each word to a tuple (word, 1) for counting
word_counts = words.map(lambda word: (word, 1))

# count the occurrences of each word
counts = word_counts.reduceByKey(lambda x, y: x + y)

# sort the words by count in descending order and take the top 20
top20 = counts.sortBy(lambda pair: pair[1], ascending=False).take(20)

# print the top 20 words with their counts
for pair in top20:
    print(pair[0], pair[1])
