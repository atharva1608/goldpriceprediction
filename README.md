# Gold Price Prediction
The gold price is being detected by using Linear Regression Model.Data imported from yahoo finance used for predicting the gold price and helpful for the stock market holders to invest in it. 
## Table of Contents
* [About](#about)
 * [Tech Stack](#tech-stack)
 
* [Getting Started](#getting-started)
 * [Prerequistes](#prerequistes)
 * [Installation](#installation)
* [Results](#results)
* [Contributor](#contributor)
* [Resources](#resources)

## About
Detecting the gold price gives us the brief idea that what will be the price.By importing the data from the yahoo finance the data is been split into 80:20 training and test set. After defining the dependent(Y) and independent(X) variables Linear Regression Model is created and then the variables is fitted by using the fit method.Gold ETF Prices is then detected by using test dataset. To check whether the data is fit effectively we will compute R-squared of the model, more the R-squared indicates that the Gold ETF Prices are well explained.Comparing the predicted price of the next day with the price of the current day plotting the graph of the cumulative returns and then the plot between actual price and the predicted price.

## Tech Stack
* [Python](#python)
* [Linear Regression Model](#linearregressionmodel)

## Getting Started
### Prerequisites
* List of softwares with version tested on
Download and run *Python3* file for suitable OS from the link
Download and run *Python3* file for suitable OS from the link
```sh
https://www.python.org/downloads/
```

Download and run *pip3* for suitable OS
Refer the below link for further instructions
```sh
https://pip.pypa.io/en/stable/installing/
```

To install yahoo finance library 
```sh
pip3 install yahoo-finance
```
### Installation
* Clone the repo
```sh
https://github.com/atharva1608/goldpriceprediction
```
## Results
**Cumulative Returns**
![**cumulative-returns**](https://github.com/atharva1608/goldpriceprediction/blob/master/cumulative_returns.png)

**Actual Price VS Predicted Price**
![**graph**](https://github.com/atharva1608/goldpriceprediction/blob/master/predicted_vs_actual_prices.png)
 
