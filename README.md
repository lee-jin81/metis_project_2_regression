
**Links**

[Code](https://github.com/lee-jin81/metis_project_2_regression/tree/main/code) <br>
[Slides](https://github.com/lee-jin81/metis_project_2_regression/blob/main/slides_regression.pdf) <br>
[Write-up](https://github.com/lee-jin81/metis_project_2_regression/blob/main/writeup_regression.pdf) <br>
[MVP](https://github.com/lee-jin81/metis_project_2_regression/tree/main/mvp) <br>
[Proposal](https://github.com/lee-jin81/metis_project_2_regression/blob/main/proposal_regression.pdf) <br>

# Predicting the price of skincare products using linear regression

## Abstract
In this project, I am attempting to predict the price of skincare products using a linear regression model. What are the most important factors that influence the price of skincare products? I used collected data on skincare products using webs craping. Then, I use linear regression to model the relationship. Additionally, regression with regularization (lasso, ridge, and elastic net) was modeled. Data set was split into test and training for proper evaluation. The model scores the same on the test and train set using regression with and without regularization. I selected the regression model without regularization since it is less complex and model was not overfitting based on scores.

## Introduction
The beauty industry is a multibillion-dollar industry that is continuously growing since 2012 and is estimated to be $189.3 billion by 2025 (source: Statista.com). More people are beginning to use skincare at a younger age, and with so many products on the market, how could one decide what to buy based on their budget? By modeling the price of skincare products with various product features, business can understand what customers are valuing in an item. 

## Design
The clients will be cosmetic businesses who are bringing a new product on the market. Businesses can use the model to understand how products are priced when they are presenting a new product. 

## Data
The data set was 1,847 skincare products data obtained from ulta.com. The target was the price. The features of interest were price (target), volume (oz), number of reviews, product name, product description, benefits, ingredients list, clinical benefits, and clean product type.

## Algorithms
### Feature engineering
1. Creating binary features of the following:
* ingredients list: to account whether an active ingredient is present or not
* brand name based on list of brands
* presence of products to a list of clean ingredients obtained from ulta.com site.
* product type: moisturizer vs serum

2. Converting rating to rating2 based on pairplot where rating has a quadratic shape.<br>

### Models
Linear regression and Linear regression with regularization: Lasso, Ridge, and Elastic Net.

### Model evaluation and selection
The entire training set of 1501 data was split into 80% train and 20% test. The validation method
used was cross validation ideal or a small/medium dataset.<br>

Linear regression without regularization results:
* Train R2 [0.390, 0.412, 0.378, 0.522, 0.333]
* Mean train R2 0.409 +/- 0.063
* Test R2: 0.413
* MAE (mean absolute error) +- $: 13.66

## Tools
* Web scraping: BeautifulSoup 
* Linear regression: Python
* Modeling: Sklearn
* Visualizations: pandas, matplotlib, and seaborn

