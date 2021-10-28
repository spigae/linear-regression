# Subrepository containing python scripts to perform Multiple Linear Regression using Ordinary Least Squares (OLS)

# Assumptions

1. The predictors, contained in the dataframe, are supposed to be numeric (floats or integers)
2. The responses, contained in the dataframe, are supposed to be in the last column

Before usage, please check the following files:
1. list-scripts.csv: it contains information about the operations performed by all the scripts
2. list-functions.csv: it contains information about the functions contained in all the scripts
3. log-versions.csv: it contains information about the versions

# Pipeline and Usage

1. Loading and describing data
   
   python loading-describing-data.py > loading-describing-data.log

2. Transforming data
   
   python transforming.py > transforming.log

3. Exploratory analysis
   
   3.1 Evaluating the relationship between predictors and response
       python exploratory-analysis-1.py > exploratory-analysis-1.log

   3.2 Creating pairwise scatterplots of predictors and response
       python exploratory-analysis-2.py > exploratory-analysis-2.log

   3.3 Calculating and plotting correlation matrix
       python exploratory-analysis-3.py > exploratory-analysis-3.log

4. Constructing the model using Ordinary Least Squares (OLS) and then fit
   python constructing-model-and-fit.py > constructing-model-and-fit.log

5. Diagnostics of model
   5.1 Diagnostic of Linearity: Rainbow and Harvey-Collier tests
       5.1.1 Rainbow Linearity Test
       5.1.2 Harvey-Collier Linearity Test
       python diagnostic-linearity.py > diagnostic-linearity.log
       
   5.2 Diagnostic of Normality
       5.2.1 Plots of predicted variables vs residuals
       5.2.2 Q-Q plot of normalized residuals
       5.2.3 Shapiro-Wilk Normality Test
       5.2.4 DAgostino K2 Normality Test
       5.2.5 Jarque-Bera Normality Test
       5.2.6 Omni Normality Test
       5.2.7 Histogram of Normalized Residuals
       python diagnostic-normality.py > diagnostic-normality.log
       
   5.3 Diagnostic of Influence
       5.3.1 Influence plot (Studentized Residuals vs H Leverage)
       5.3.2 Leverage plot (Leverage vs Normalized Residuals^2)
       python diagnostic-influence.py > diagnostic-influence.log

   5.4 Diagnostic of Multicollinearity
       5.4.1 Calculation Condition number (reference values?)
       5.4.2 Calculation Variance Inflation Factor (reference values?)
       5.4.3 Calculation Correlation Matrix
       5.4.4 Graph heatmap correlation matrix
       python diagnostic-multicollinearity.py > diagnostic-multicollinearity.log

   5.5 Diagnostic of Heteroskedasticity
       5.5.1 Breush-Pagan test (reference values?)
       5.5.2 Goldfeld Quandt test (reference values?)
       5.5.3 fitted vs residuals
       python diagnostic-heteroskedasticity.py > diagnostic-heteroskedasticity.log

6. Predictions
   Making predictions on the basis of the created model/fit
   python make-predictions.py > make-predictions.log

Please contact me at the following email address: spiga.enrico at gmail.com if you need clarifications or support in using the scripts.


Enrico Spiga

Chiamavamo noi stessi S'ARD, che nell'antica lingua significa danzatori delle stelle.

We called ourselves S'ARD, which in the ancient language means dancers of stars.

Sergio Atzeni
