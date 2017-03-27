# Portuguese Forest Fires - Springboard Capstone Project

## Overview

### Introduction

Forest fires are responsible for considerable environmental and monetary damage globally. Early detection and appropriate response can provide substantial relief, but what factors and data can be used to determine a the threat a fire poses? While several studies of this nature exist that attempt to predict fires, this project attempts to predict the size of a fire's burn area, given fire science metric, spatio/temporal, and meteorological data. It is clear that simple meteorological data is the easiest to access, most abundant, and least expensive to gather, and thus is the cornerstone of the data collected here. Coincidentally, these variables seem to fit the best predictive model.

A predictive model would give authorities a powerful tool in the fight against forest fires. Appropriate resources could be dedicated to a fire at inception, limiting cost and damage. More accurate alerts could be sent out to the public, increasing awareness as well as safety.

### The Data Source

The data to be used is available at http://archive.ics.uci.edu/ml/datasets/Forest+Fires, and is a collection curated by scientists Paulo Cortez and Anibal Morais from the Unviersity of Minho, Portugal. The data was used in their paper, [A Data Mining Approach to Predict Forest Fires using Meteorological Data](http://www3.dsi.uminho.pt/pcortez/fires.pdf).

The data includes meteorological measurements taken at the time the fire was reported, spatial/temporal measurements, and index metrics that take into a account weather data in the recent past. The index metrics are a part of the Canadian Fire Weather Index System (FWI). Exhaustive information regarding the calculation of these indices can be found here: [FWI Handbook](https://www.frames.gov/files/6014/1576/1411/FWI-history.pdf).

### Questions to Investigate

While the paper mentioned above did examine the correlation between the four meteorological measurements and fire damage area, it did not investigate the relationship between the four index metrics and fire damage area. My initial goal was to examine different subsets of features, but after starting the machine learning process, it became clear that there was an overall lack of signal in the data. From my own analysis, I can confirm that including the four index metrics does decrease overall performance, to a very small extent.

### Approach

Since the output variable is a real number, I will attempt a regression analysis on the data using a variety of machine learning algorithms. This will include several variable shrinkage methods, regression trees, and support vector regression.

The data set is not extremely large, and there are extreme outliers, so random train/test groupings vary widely in their results. As a consequence, I will run 30 iterations of 10-fold cross-validationm and average all results for each model to compare them, after fitting the models with optimal parameters.

The research paper referenced above used mean absolute value (MAE) as the scoring metric, so I will use this as well in order to use the paper as a benchmark.

## Data Analysis

You can find the full data story in [Data_Story.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Data_Story.ipynb)

### Variables

There are 531 data entries, each with 12 attributes and 1 output variable.

Two of these variables are positive integers and refer to the x and y coordinates of a map specific to Montesinho natural park, the location of the fires. Another two variables are also positive integers and refer to the time of the fire, one being the day of the week and the other being the month of the year the fire was reported.

Four variables are meteorological measurements (floats) taken when the fire was first reported and include temperature, relative humidity, rain over the last 30 minutes, and wind speed.

The remaining four variables, FMC, DMC, DC, and ISI, are FWIC index metrics (floats) which take those four basic meteorologic measurements into account over longer periods of time and in different proportions to determine factors such as moisture levels at different depths of the soil, which suggest how quickly a fire might be likely to spread or the temperature it might reach.

FMC, DMC, and DC all take longer term rainfall and temperature averages into account to measure how dry the land is. They consider the past 16 hours, 12 days, and 52 days respectively. FMC and DMC also consider relative humidity. ISI takes FMC and factors in wind speed to determine how easily surface level fire will spread.

The target variable is the area of fire damage, measured in hectares. While each entry is a record of a fire, if the damaged area was less than 0.1 hectare, the value was rounded to 0.

### Exploratory Analysis

~48% of the fires have been rounded to size 0, and this prevents transformation to a Gaussian distribution. However, this does provide a binary classification of the fires.

Several variables have a lot of skew, so several transformations may be useful when performing the machine learning phase. A logarithmic transformation helps reduce skew considerably for FFMC and area, while the square root brings ISI and rain considerably closer to normal.

The Pearson correlation coefficients between input variables suggest we don't have to worry about co-linearity:

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/coefmat.png "Pearson coefficient matrix")

Plotting each variable against the other gives more insight into the relationships:

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/pairplot.png "Pair plots")

It is apparent that the FWIC metrics are manufactured from each other since their pair plots have so much structure. For instance, ISI and FFMC have some sort of hyperbolic relationship, and DMC and DC have a very linear relationship with an additional parameter separating the data into distinct parallel lines.

Looking at the individual relationships between input variables and the target is informative as well:

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/targetplot1.png "Target plot 1")
![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/targetplot2.png "Target plot 2")

You can see vague trends but all of the data points with area=0 seem to drown the information of any predictive power.

Another thing to notice from both sets of pair plots is that they have been color coded to distinguish fires of size zero. Unfortunately, we do not see any separation of the colors when one of the axes is not area.

Looking at the breakdown of fire size by month provides relief by granting our intuition:

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/areabymonth.png "Area broken down by month")

You'll notice it resembles the break down of temperature by month:

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/tempbymonth.png "Temperature broken down by month")

But the problem remains that many size zero fires occur in all circumstances. Indeed, simply distinguishing fires of size zero and those larger using the input variables is no easy feat. Running multiple iterations of logistic regression and random forests results in ~53% success prediction rate, with receiver operating characteristic (ROC) curves that resemble guessing.

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/rocs.png "ROC Curves")

This suggests the input variables are really very close to noise relative to the size of the fire.


## Machine Learning

See the details in [Machine_Learning.ipynb](https://github.com/davidjwatts/portuguese_fires/blob/master/Machine_Mearning.ipynb)

Off the bat, it is clear that this will be a difficult regression task. Least squares regression analysis and principle components analysis suggests that the input variables are not highly correlated with the target variable. Extremely high p-values for the coefficients of each input variable imply that it is likely there is no correlation between that variable and the output.

Principle component analysis allows us to project the cloud of data onto the two-dimensional plane of greatest variance. This typically has the effect of displaying some amount of structure, and breaks up the data into groups with similarities. Our results differ according to which variables we include.

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/pca.png "PCA graphs")

All of the variables, or even just FWIC metrics show us plenty of structure, but the structure exists between the metrics themselves, as we've seen before. There is no spread of fires by size. Looking at the meteorological variables, we see just an undifferentiated cloud of mixed color. Fires of size zero can be found everywhere.

### Algorithms

Several variable shrinking regression methods were tested in addition to standard least squares, including: ridge regression, lasso regression, and elastic net. These all had very similar results, which isn't surprising because they are trying to minimize a function that penalizes coefficients for overall size. However, since the data is so noisy, the models did worse than guessing zero for each fire. 

Support vector regression with linear and radial basis kernels was tested. Hyper-parameters for both include C and epsilon values which determine what to do with error values within certain ranges. The gamma parameter is usually related to the spread of the target data set. The radial basis kernel consistently outperforms the linear kernel, and both consistently outperformed guessing a fire size of 0.

Lastly, gradient boosting regression was tried. Hyper-parameters include the loss function to be minimized and the function to determine the quality of each tree split. The optimal settings for both were absolute deviation, since our score to optimize for, MAE, is based on absolute deviation. This model performed between the two support vector regression models. 

The clear leaders are gradient boosting regression and support vector regression with radial basis kernel. I constructed an ensemble method consisting of averaging the predictions from those two models, and this yields the best average MAE scores over repeated tests. This makes sense since the two methods are substantially different in their approach, and there should be some reduction in bias by combining them.

Technique |   MAE (30 trial avg)
---|---
Linear Regression |  13.00
Ridge Regression |  12.98
Elastic Net |  12.98
Lasso |  12.98
Guessing 0 fire size |  12.85
SVR Linear |  12.84
GBR |  12.70
SVR Rbf |  12.67
Hybrid |  12.66

### Best Model

The best model is ensemble that averages the the predictions from the support vector regression model with radial basis kernel and the gradient boosting regression model with maximum depth of one, with absolute value for the criterion and loss functions. Parameters for the SVR are C = 4.76, epsilon = 0.294, and gamma = 0.075.

Hyperparameters were found in part by starting with those cited in the paper and searching the surrounding neighborhoods.
SVR MAE scores superior to those used in the article were achieved, but only reducing average MAE from 12.71 to 12.67. The ensemble method managed to shave another hundredth off average MAE.

### Results

The results are far from excellent, and it is questionable how useful they could be. Looking at this graph, which shows the comparison of all 30*531=15,930 predictions compared with the actual size of the fire shows just far off most predictions are.

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/predvsact.png "Predictions vs Actual Size")

Many of the predictions seem to just be a guess in the 0-5 region, while predictions venture into the +5 region when the fires actually are larger than 5. A prediction of less than 5 may not be very meaningful, but a prediction of greater than 10 is highly indicative of a fire greater than 5. This model could be used to lend further support to an argument that a specific fire deserved a great deal of attention because it threatened to be large.

![alt text](https://github.com/davidjwatts/portuguese_fires/blob/master/images/rec.png "Regression Error Characteristic")

The regression error characteristic curve suggests that the model contains many predictions within a reasonable error threshold. For example, 60% of the predictions are within 2 hectares of error. However, the tail suggests an extreme degree of error for 10% or more of the test predictions. When compared with the guess of 0 for each fire, we see that there is laughably little difference.

### Reflection and Further Research

I believe I have successfully shown that the data is more noise than signal, and that even an exhaustive survey of machine learning methods would fail to improve much on my results. However, it is only clear that the data and features at hand fail to show a useful correlation.

Fire science expertise should be used to ascertain additional features related to forest fire activity. For instance, fire fighting efforts probably played a large role in limiting fire damage area, and this data completely obscures that. There are other fire issues such as the state of underbrush in the forest, which could be natural or due to controlled burns, and a factor called aspect takes into consideration the gradient of the land near the fire, which has an impact on how quickly fire spreads. More relevant features will improve model accuracy.

The target variable, fire damage area, may not be misguided. I think including this variable as an input variable could be useful in determining other targets, such as likelihood of a fire. This likelihood could be thought of as a probability density function or cumulative distribution function, and could even be mapped geographically to determine areas of highest risk.
