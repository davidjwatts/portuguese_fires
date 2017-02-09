# Portuguese Fires
##Springboard Capstone Project #1

###Introduction
Forest fires are a serious issue globally, responsible for considerable environmental and monetary damage. Early detection can provide substantial relief, but what factors and data can be used for such a complex phenomenon? While a handful of different metrics and sources of data have been used in the past to attempt prediction of fire, it is clear that simple meteorological data is the easiest to access, most abundant, and least expensive to gather. The attempt of this study is to investigate the relationship between meteorological data and the area of fire damage.

A predicitive model would give authorities a powerful tool in the fight against fire damage. Appropriate resources could be dedicated to a fire at inception, limiting cost and damage. More accurate alerts could be sent out to the public, increasing public awareness as well as safety. 

###The Data
The data to be used is available at http://archive.ics.uci.edu/ml/datasets/Forest+Fires, and is a data set collected by scientists Paulo Cortez and Anibal Morais from the Unviersity of Minho, Portugal. The data was used in their paper, [A Data Mining Approach to Predict Forest Fires using Meteorological Data](http://www3.dsi.uminho.pt/pcortez/fires.pdf).

There are 12 attributes included in the data, and 1 output variable. 4 of these variables refer to date and location, and are not currently central to the investigation. 4 variables are measurements taken when the fire was first reported and include temperature, relative humidity, wind speed, and rain over the last 30 minutes. The remaining 4 variables are various index metrics which take those four basic meteorologic measurements into account over longer periods of time and in different proportions to determine factors such as how quickly fire might be likely to spread or how hot it might be.

###Approach and Questions to Investigate

While the paper mentioned above did examine the correlation between the 4 meteorological measurements and fire damage area, it did not investigate the relationship between the 4 index metrics and fire damage area. Perhaps this is because the index metrics were not strongly correlated. I would like to compare the correlation between the immediate meteorological data and acreage burned and the correlation between the index metrics and acreage burned to see which is stronger. Ultimately, I will try to find the combination of attributes of both types that leads to the strongest correlation.

Since the output variable is a real number, I will be performing a regression analysis on the data using the contemporary best practices in machine learning.

###Deliverables

The final deliverables will consis of a slide deck, ipython notebook, and final paper writing up the details of the investigation and its conclusions.
