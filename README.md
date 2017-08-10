# Hadoop-Greenery-Comparison

This small exercise was done do compare the amount of greenery between two places using the map and reduce concepts of HADOOP.

# How to use the files:

1. Generate an input.txt file containing the BGR values of each pixel in the image in the following way :
72	62	72 <br/>
54	43	54 <br/>
46	35	50 <br/>
41	31	49 <br/>
...... <br/>
(the BGR values seperated by tabs)
      
2. Store this input.txt in the HDFS.

3. The percentage of greenery of the comparison place is already calculated in the same method and hardcoded for comparison with any new      image (Can be done dynamically instead of hard coding the value.)

4. Use hadoop streaming to run the map.py and reduce.py specifying the input file path and the Output path in hdfs. 
