# Subrepository containing python scripts to perform Multiple Linear Regression using Ordinary Least Squares (OLS)

# Assumptions

1. The predictors, contained in the dataframe, are supposed to be numeric (floats or integers)
2. The responses, contained in the dataframe, are supposed to be in the last column

Before usage, please check the following files:
1. list-scripts.csv: it contains information about the operations performed by all the scripts
2. list-functions.csv: it contains information about the functions contained in all the scripts
3. log-versions.csv: it contains information about the versions

# Pipeline and Usage

## 1. Loading and describing data
Script: loading-describing-data.py

Usage (from a terminal):
python loading-describing-data.py > loading-describing-data.log

## 2. Transforming data
Script: transforming.py

python transforming.py > transforming.log

## 3. Exploratory analysis
### 3.1 Evaluating the relationship between predictors and response
python exploratory-analysis-1.py > exploratory-analysis-1.log

### 3.2 Creating pairwise scatterplots of predictors and response
python exploratory-analysis-2.py > exploratory-analysis-2.log

### 3.3 Calculating and plotting correlation matrix
python exploratory-analysis-3.py > exploratory-analysis-3.log

## 4. Constructing the model using Ordinary Least Squares (OLS) and then fit
python constructing-model-and-fit.py > constructing-model-and-fit.log

## 5. Diagnostics of the model
### 5.1 Diagnostic of Linearity: Rainbow and Harvey-Collier tests
python diagnostic-linearity.py > diagnostic-linearity.log
       
### 5.2 Diagnostic of Normality:
Plots of predicted variables vs residuals, 
Q-Q plot of normalized residuals,
Shapiro-Wilk Normality Test,
D' Agostino K2 Normality Test,
Jarque-Bera Normality Test,
Omni Normality Test,
Histogram of Normalized Residuals.

python diagnostic-normality.py > diagnostic-normality.log
       
### 5.3 Diagnostic of Influence:
Influence plot (Studentized Residuals vs H Leverage), 
Leverage plot (Leverage vs Normalized Residuals^2)

python diagnostic-influence.py > diagnostic-influence.log

### 5.4 Diagnostic of Multicollinearity:
Calculation Condition number,
Calculation Variance Inflation Factor,
Calculation Correlation Matrix,
Graph heatmap correlation matrix.

python diagnostic-multicollinearity.py > diagnostic-multicollinearity.log

### 5.5 Diagnostic of Heteroskedasticity:
Breush-Pagan test,
Goldfeld Quandt test,
fitted vs residuals.

python diagnostic-heteroskedasticity.py > diagnostic-heteroskedasticity.log

## 6. Predictions
Making predictions on the basis of the created model/fit

python make-predictions.py > make-predictions.log


Please contact me at the following email address: spiga.enrico at gmail.com if you need clarifications or support in using the scripts.

---
Enrico Spiga

Chiamavamo noi stessi S'ARD, che nell'antica lingua significa danzatori delle stelle.

We called ourselves S'ARD, which in the ancient language means dancers of stars.

Sergio Atzeni
