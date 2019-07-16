# Bikes Rental Analysis

![](https://github.com/klaudia-nazarko/bikes-rental-analysis/blob/master/img/header-img.jpg)

## Introduction

Leaving in the city is a transportation challenge. With increasing number of cars and cumbersome traffic jams, citizens tend to look for alternatives. Healthy lifestyle and concern about ecology encourage more and more people to select bike as their mean of transport. It's an interesting task to explore what factors influence cyclists' decisions.

Thanks to the data shared by [Capital Bikeshare](https://www.capitalbikeshare.com/) company this kind of analysis is possible. The project will focus on understanding behavior of people renting bikes in Washington D.C. in years 2012-2018.

## Project scope

### Downloading data

In order to make an analysis more interesting and comprehensive, not only were frequency and duration of bike rentals analyzed but also information about weather and stations' location was taken into consideration. The [data collection folder](https://github.com/klaudia-nazarko/bikes-rental-analysis/tree/master/1.%20data%20collection) contains scripts to download & scrape raw data.

### Exploratory analysis

Before starting to work with data, it's always good to get to know them better. In the first place the distribution of features was analyzed in order to understand the dataset better, detect outliers and to decide how to deal with them. As a result, final version of data (ready for an analysis) was prepared. Scripts with exploratory analysis may be found in [data exploration folder](https://github.com/klaudia-nazarko/bikes-rental-analysis/tree/master/2.%20data%20exploration).

### Regression model

Already knowing which features impact cyclists' decisions, the goal of this task was to predict number of bike rentals on a given day. [Regression model directory](https://github.com/klaudia-nazarko/bikes-rental-analysis/tree/master/3.%20regression%20model) contains preparing predictors and obtaining new data (eg. from Google Trends). In the next step, simple regression models were built as a baseline. The last notebook focuses on building top-performing model by feature engineering and hyperparameters tuning.


