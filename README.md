# Portuguese Fires - Springboard Capstone Project #1
##Proposal
###Introduction
Forest fires are a serious issue globally, responsible for considerable environmental and monetary damage. Early detection can provide substantial relief, but what factors and data can be used to determine how threatening a fire is? While a handful of different metrics and sources of data have been used in the past to attempt prediction of fire, this project attempts to connect this same predictors to fire size and damage.  It is clear that simple meteorological data is the easiest to access, most abundant, and least expensive to gather, and thus is the cornerstone of the data collected here. The attempt of this study is to investigate the relationship between meteorological data and the area of fire damage.

A predictive model would give authorities a powerful tool in the fight against fire damage. Appropriate resources could be dedicated to a fire at inception, limiting cost and damage. More accurate alerts could be sent out to the public, increasing awareness as well as safety.

###The Data Source
The data to be used is available at http://archive.ics.uci.edu/ml/datasets/Forest+Fires, and is a collection curated by scientists Paulo Cortez and Anibal Morais from the Unviersity of Minho, Portugal. The data was used in their paper, [A Data Mining Approach to Predict Forest Fires using Meteorological Data](http://www3.dsi.uminho.pt/pcortez/fires.pdf).

There are 12 attributes included in the data, and 1 output variable. 4 of these variables refer to date and location, and are not currently central to the investigation. 4 variables are measurements taken when the fire was first reported and include temperature, relative humidity, wind speed, and rain over the last 30 minutes. The remaining 4 variables are various index metrics which take those four basic meteorologic measurements into account over longer periods of time and in different proportions to determine factors such as how quickly fire might be likely to spread or how hot it might be.

The index metrics are a part of the Canadian Fire Weather Index System (FWI). Exhaustive information regarding the calculation of these indices can be found here: [FWI Handbook](https://www.frames.gov/files/6014/1576/1411/FWI-history.pdf).

###Questions to Investigate

While the paper mentioned above did examine the correlation between the 4 meteorological measurements and fire damage area, it did not investigate the relationship between the 4 index metrics and fire damage area. Perhaps this is because the index metrics were not strongly correlated. I would like to compare the correlation between the immediate meteorological data and acreage burned and the correlation between the index metrics and acreage burned to see which is stronger. Ultimately, I will try to find the combination of attributes of both types that leads to the strongest correlation.

##Data Wrangling

Data Wrangling was pretty straightforward in this case. The scientists had already assembled the data from several sources, merging it and dealing with null values.

I imported the data as a CSV, which was provided with column names. The 'month' and 'day' columns consisted of lower case string abbreviations of the month and day of the week. I converted both columns to integer values, standard for the months and Sunday=1 for the days of the week.

There were no null values present in the data frame. I briefly analyzed the data for problematic outliers. It appears that the output variable is strongly skewed to the right. I think this might be helped by applying a log function to the column, so I have added the column 'log' which is equal to the natural log of (area+1). This column is skewed less to the right. It looks like some of the index metrics have some outliers. I don't think I should scrutinize these for accuracy, since the data has already been careful chosen, but I will be sure to consider their role in model fitting.

##Data Story

FMC, DMC, and DC all take longer term rainfall and temperature averages into account to measure how dry the land is. They consider the past 16 hours, 12 days, and 52 days respectively. FMC and DMC also consider relative humidity. ISI takes FMC and factors in wind speed to determine how easily surface level fuel will catch fire and begin to spread.

###Correlations between Predictors

It seems quite clear that FFMC and ISI have some sort of hyperbolic relationship. This makes sense since FFMC is considered along with wind to calculate ISI.

![FFMC vs ISI](https://github.com/davidjwatts/portuguese_fires/blob/master/images/FFMCvsISI.png "FFMC vs ISI")

DMC and DC are obviously calculated in a very similar way, and the difference is likely some integer value that represents relative humidity and rainfall over the long term. I say this because of the step nature between the implied lines on the chart.

![FFMC vs ISI](https://github.com/davidjwatts/portuguese_fires/blob/master/images/DMCvsDC.png "DMC vs DC")

There are many more fires in the Summer, but there are also a decent number in the late Winter/early Spring. While there are more larger fires in the Summer, December seems to have the highest average fire size.

###Connections to Month

![Fire Damage by Month](https://github.com/davidjwatts/portuguese_fires/blob/master/images/firesbymonth.png "Fire Damage by Month")

This leads me to wonder if the dryness is distributed in a similar way.

<INSERT CHART OF DMC by month>

###Outliers

Rain and ISI both seem to have some extreme outliers. However, I have no reason to think these data points are unreliable. I will experiment with removing this when fitting the models.

![ISI dist](https://github.com/davidjwatts/portuguese_fires/blob/master/images/ISIdist.png "ISI Distribution")

![Rain dist](https://github.com/davidjwatts/portuguese_fires/blob/master/images/raindist.png "Rain Distribution")

##Preliminary Statistical Analysis

Using Pearson correlation coefficient matrix, it is clear that none of the predictor variables have an overly strong co-linear relationship. It is also apparent that none of the predictors have a strong linear correlation with the target variable.

Ordinary least squares regression fails miserably with this data. The R^2 is less than 3%.  

##Approach

Since the output variable is a real number, I will attempt a regression analysis on the data using the contemporary best practices in machine learning. This will include various type of regression, including ridge regression, polynomial regression, regression trees, and regression SVM. It makes sense to me to also qualify the fire size as being either small or large (area equal to zero or greater than zero), and then run classification models as well.

##Deliverables

The final deliverables will consist of a slide deck, iPython notebook, and final paper writing up the details of the investigation and its conclusions.
