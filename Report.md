# Overview


Data
	-features
	-exploratory analysis

PCA
	-When comparing area=0 against not, no distinguishable difference in data
	-If we use logistic regression and random forest methods to attempt to simply distinguish data 	based on fire size=0 and not, success rate is only slightly above 50%.

Simple regression least squares analysis
	-looking at t-scores and values, none of the input variables seem to have a huge correlation with 	fire size. There are so many small fires mixed in with all conditions.


	Were these fires simply detected earlier and supressed before they could spread?


Other Regression methods:
	-If we try to squeeze all predictive accuracy out, we can do slightly better than presented in the 	academic paper, although it is using the same method, Support vector regression.

	This was achieved by testing more parameter values in the neighborhoods of the values use in 	the paper. Improvement is marginal though

	-Using subsets of features has a small effect of the results. Best results are achieved using on the 	4 meteorological data sources and omitting the spatio/temporal and FWIC data.


	Another method that ended up being quite close is gradient boosting regression.

We can take a look at our predictions vs the real data
	-it suggests that our predictive power is not strong at all. The only consolation is that when fires 	are small (=0), the error of prediction averages ~(7.4) and doesn’t exceed 8. Hence, predictions 	beyond this point have a high likelihood of indicating a fire larger than 0. However, a majority 	of large fires are predicted to be small with this model.




Tables to defend results
	different type of regression vs GBR and SVR, include guessing the mean as a benchmark

	show the setting of the parameters for svr

	show the graph of the results and the rec curve
