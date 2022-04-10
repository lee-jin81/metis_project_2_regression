In my initial proposal, I wanted to predict the ratings of skincare products, but after some preliminary results, I noticed that price might be a better predictor in my data.

### Heatmap
Below is a heat map of the features, and as indicated in the figure, there doesn't seem to be correlations between the variables other than `len_ingredients` and `price_USD`.

![Heat map](Skincare_heatmap.png)

### Regression model
Then, I ran a linear regression module using `price_USD` as the predictor. Below is a summary of my model. The R-squared value was 0.257, which is quite low for the results and corresponds with the heat map that there is low or no correlation. Next, is the DB value of 2.046, which again suggest that there is no correlation.

![Linear_regression](OLS_regression_results.png)

Skincare products might not be fit for a linear regression model considering that other factors such as marketing, use of social media, and current trends are known to influence the purchase behavior of an item. These are variables that are subjective and not readily predictable. This could explains why a low R-squared value was obtained since these features have not been considered in the model.

### Summary
Before moving to the next part of modeling, I would like to give some thought on what factors I would like to look into. 

