# Portuguese Fires - Springboard Capstone Project #1
##Overview
###Introduction
Forest fires are responsible for considerable environmental and monetary damage globally. Early detection and appropriate response can provide substantial relief, but what factors and data can be used to determine how threatening a fire is? While a handful of different metrics and sources of data have been used in the past to attempt prediction of fire, this project attempts to connect this same predictors to fire size and damage.  It is clear that simple meteorological data is the easiest to access, most abundant, and least expensive to gather, and thus is the cornerstone of the data collected here. The attempt of this study is to investigate the relationship between meteorological data and the area of fire damage.

A predictive model would give authorities a powerful tool in the fight against fire damage. Appropriate resources could be dedicated to a fire at inception, limiting cost and damage. More accurate alerts could be sent out to the public, increasing awareness as well as safety.

###The Data Source
The data to be used is available at http://archive.ics.uci.edu/ml/datasets/Forest+Fires, and is a collection curated by scientists Paulo Cortez and Anibal Morais from the Unviersity of Minho, Portugal. The data was used in their paper, [A Data Mining Approach to Predict Forest Fires using Meteorological Data](http://www3.dsi.uminho.pt/pcortez/fires.pdf).

The data includes meteorological measurements taken at the time the fire was reported, spatial/temporal measurements, and index metrics that take into a account weather data in the recent past. The index metrics are a part of the Canadian Fire Weather Index System (FWI). Exhaustive information regarding the calculation of these indices can be found here: [FWI Handbook](https://www.frames.gov/files/6014/1576/1411/FWI-history.pdf).

###Questions to Investigate

While the paper mentioned above did examine the correlation between the 4 meteorological measurements and fire damage area, it did not investigate the relationship between the 4 index metrics and fire damage area. Perhaps this is because the index metrics were not strongly correlated. I would like to compare the correlation between the immediate meteorological data and acreage burned and the correlation between the index metrics and acreage burned to see which is stronger. Month will be added in as well. Ultimately, I will try to find the combination of attributes of both types that leads to the strongest correlation.

###Approach

Since the output variable is a real number, I will attempt a regression analysis on the data using the contemporary best practices in machine learning. This will include various type of regression, including ridge regression, polynomial regression, regression trees, and regression SVM. It makes sense to me to also qualify the fire size as being either small or large (area equal to zero or greater than zero), and then run classification models as well.

###Deliverables

The final deliverables will consist of a slide deck, iPython notebook, and final paper writing up the details of the investigation and its conclusions.

##Data Wrangling

Data Wrangling was pretty straightforward in this case. The scientists had already assembled the data from several sources, merging it and dealing with null values.

I imported the data as a CSV, which was provided with column names. The 'month' and 'day' columns consisted of lower case string abbreviations of the month and day of the week. I converted both columns to integer values, standard for the months and Sunday=1 for the days of the week.

These steps have been refactored into a method called 'wrangle' and reside in the [utils.py](https://github.com/davidjwatts/portuguese_fires/blob/master/utils.py) file.

##Data Story

You can find the full data story here:

[Data_Story.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Data_Story.ipynb)

Many (almost half) of the fires have been rounded to size 0, and this prevents transformation to a Gaussian distribution. However, this does provide a binary classification, and this can be used later in different ways.

The several variables have a lot of skew, so several transformations may be useful when performing the machine learning phase. A logarithmic transformation help reduce skew considerably for FFMC and area, while the square root brings ISI and considerably closer to normal.

If we perform a logistic regression and random forest analysis to test whether the data with area=0 is distinguishable from the rest, we get poor areas under the ROC curves, only slightly above 50% on average.

##Machine Learning

[Machine_Learning.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Machine_Mearning.ipynb)
