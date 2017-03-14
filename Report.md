# Portuguese Forest Fires - Springboard Capstone Project

##Overview

###Introduction

Forest fires are responsible for considerable environmental and monetary damage globally. Early detection and appropriate response can provide substantial relief, but what factors and data can be used to determine how threatening a fire is? While several studies of this nature exist that attempt to predict fires, this project attempts to predict the size of a fire's burn area, given fire science metric, spatio/temporal, and meteorological data. It is clear that simple meteorological data is the easiest to access, most abundant, and least expensive to gather, and thus is the cornerstone of the data collected here. Coincidentally, these variables seem to fit the best predictive model.

A predictive model would give authorities a powerful tool in the fight against forest fires. Appropriate resources could be dedicated to a fire at inception, limiting cost and damage. More accurate alerts could be sent out to the public, increasing awareness as well as safety.

###The Data Source

The data to be used is available at http://archive.ics.uci.edu/ml/datasets/Forest+Fires, and is a collection curated by scientists Paulo Cortez and Anibal Morais from the Unviersity of Minho, Portugal. The data was used in their paper, [A Data Mining Approach to Predict Forest Fires using Meteorological Data](http://www3.dsi.uminho.pt/pcortez/fires.pdf).

The data includes meteorological measurements taken at the time the fire was reported, spatial/temporal measurements, and index metrics that take into a account weather data in the recent past. The index metrics are a part of the Canadian Fire Weather Index System (FWI). Exhaustive information regarding the calculation of these indices can be found here: [FWI Handbook](https://www.frames.gov/files/6014/1576/1411/FWI-history.pdf).

###Questions to Investigate

While the paper mentioned above did examine the correlation between the 4 meteorological measurements and fire damage area, it did not investigate the relationship between the 4 index metrics and fire damage area. Perhaps this is because the index metrics were not strongly correlated. I would like to compare the correlation between the immediate meteorological data and acreage burned and the correlation between the index metrics and acreage burned to see which is stronger. Month will also be considered.

###Approach

Since the output variable is a real number, I will attempt a regression analysis on the data using a variety of machine learning algorithms. This will include several variable shrinkage methods, regression trees, and support vector regression.

The data set is not extremely large, and there are extreme outliers, so random train/test groupings vary widely in their results. As a consequence, I will typically run 30 iterations of 10-fold cross-validation for each variable/parameter test, and average all results.

The research paper referenced above used mean absolute value (MAE) as the scoring metric, so I will use this as well in order to use the paper as a benchmark.

##Data Analysis

You can find the full data story in [Data_Story.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Data_Story.ipynb)

###Variables

There are 12 attributes included in the data, and 1 output variable.

Two of these variables refer to the x and y coordinates of a map specific to Montesinho natural park, the location of the fires. Two variables refer to the time of the fire, one being the day of the week the fire was reported and another is the month of the year.

Four variables are measurements taken when the fire was first reported and include temperature, relative humidity, rain over the last 30 minutes, and wind speed.

The remaining four variables, FMC, DMC, DC, and ISI, are various index metrics which take those four basic meteorologic measurements into account over longer periods of time and in different proportions to determine factors such as moisture levels at different depths of the soil, which suggest how quickly a fire might be likely to spread or the temperatures it might reach.

FMC, DMC, and DC all take longer term rainfall and temperature averages into account to measure how dry the land is. They consider the past 16 hours, 12 days, and 52 days respectively. FMC and DMC also consider relative humidity. ISI takes FMC and factors in wind speed to determine how easily surface level fire will spread.

The target variable is the area of fire damage, measured in hectares. While each entry is a record of a fire, if the damaged area was less than 0.1 hectare, the value was rounded to 0.

###Exploratory Analysis

~48% of the fires have been rounded to size 0, and this prevents transformation to a Gaussian distribution. However, this does provide a binary classification of the fires.

Several variables have a lot of skew, so several transformations may be useful when performing the machine learning phase. A logarithmic transformation help reduce skew considerably for FFMC and area, while the square root brings ISI and rain considerably closer to normal.

If we perform a logistic regression and random forest analysis to test whether the data with area=0 is distinguishable from the rest, we get poor areas under the ROC curves, only slightly above 50% on average.




##Machine Learning

    [Machine_Learning.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Machine_Mearning.ipynb)

    Off the bat, it is clear that this will be a difficult regression task. Least squares regression analysis and principle components analysis suggests that the input variables are not highly correlated with the target variable.

    I bring many different regression algorithms, including: ridge regression, elastic net, lasso lars, support vector regression, and gradient boosting regression. The clear leaders are gradient boosting regression and support vector regression with radial basis kernel. The ensemble method consisting of averaging the predictions from those two models yields the best average MAE scores over repeated tests.

    Hyper-parameters for the SVR model were fitted using 30 iterations of 10-fold cross-validation using a set of parameters surrounding base-line settings presented in the article. SVR parameters superior to those used in the article were achieved, but only reducing average MAE from 12.71 to 12.69. The ensemble method to shave another hundredth off average MAE.
