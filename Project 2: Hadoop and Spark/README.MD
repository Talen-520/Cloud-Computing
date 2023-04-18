Project 2: Hadoop and Spark
Due: 11:59 PM, April 23

The purpose of this project is to support your in-class understanding of how data analytics stacks work and get some hands-on experience in using them. You will need to deploy Apache Hadoop as the underlying file system and Apache Spark as the execution engine. You will then develop several small applications based on them.

Task 1: Launch a cluster of virtual machines in a cloud environment (e.g., AWS, Azure, or GCP). You will need to have one node as the master and at least two nodes as workers (slaves).

Task 2: Deploy the HDFS service on the cluster.

Task 3: Download the text version of Pride and Prejudice from Project Gutenberg, and save it to the HDFS cluster.

Task 4: Deploy the Spark service on the cluster.

Task 5: Use the file in HDFS as input, run a wordcount program in Spark to count the number of occurrences of each word. Sort the words by count, in descending order, and return a list of the (word, count) pairs for the 20 most used words.

Task 6: Write a Spark program that uses Monte Carlo methods to estimate the value of $π$.

Since the area of a circle of radius r is $A = πr^2$ , one way to estimate π is to estimate the area of the unit circle. A Monte Carlo approach to this problem is to uniformly sample points in the square $[−1, 1] × [−1, 1]$ and then count the percentage of points that land within the unit circle. The percentage of points within the circle approximates the percentage of the area occupied by the circle. Multiplying this percentage by 4 (the area of the square $[−1, 1] × [−1, 1]$) gives an estimate for the area of the circle.

Submit a report on Blackboard, describing the commands you run, code in any file(s), your observations, and output from all the steps in each task. Also explain the purpose of each step in your report.

 
