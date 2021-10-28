#
# name: diagnostic-multicollinearity.py
name='diagnostic-multicollinearity'
description='Diagnostic of Multicollinearity: Condition Number and Variation Inflation'
# version: 0.1
version='0.1'
# date last revision: 26.10.2021
date_last_revision='26.10.2021'
# author: spigae
author='spigae'
# webpage: https://github.com/spigae
#
# importing libraries
# os
import os
# platform
import platform
# io
import io
# time
import time
# pandas
import pandas as pd
# import numpy
import numpy as np
# import scipy
from scipy.stats import shapiro
from scipy.stats import normaltest
# import matplotlib
import matplotlib.pyplot as plt
# import statsmodels
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.stats.outliers_influence import OLSInfluence
from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in0='Concrete_Data.xls'
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='variation-infation.csv'
out2='data-correlation-matrix-multicollinearity.csv'
out3='heatmap-correlation-values-multicollinearity.jpeg'
#
# to calculate elapsed time
start_time = time.time()
print(' ')
print('',name)
print(' Python version:', platform.python_version())
print(' version: ',version)
print('',description)
print(' date last revision: ',date_last_revision)
print(' author: ',author)
print(' ')
print(' Inputs:')
print(' input 1: ',in1)
print(' ')
print(' Outputs:')
print(' output 0: ',out0)
print(' output 1: ',out1)
print(' output 2: ',out2)
print(' output 3: ',out3)
print(' ')
print(' ... script running')
print(' ')
#
#---
# function for reading the dataframe for statsmodels
#---
def read_df(filename):
    df1 = pd.read_csv(in1, sep=',')
    return df1
#---
# function to construct and fit the model
#---
def construct_fit_model():
    # creating a formula string for using in the statsmodels.OLS()
    formula_str = df1.columns[-1]+' ~ '+'+'.join(df1.columns[:-1])
    # setting the model
    model=smf.ols(formula=formula_str, data=df1)
    # fit the model
    fitted = model.fit()
    # summary of the model 
    summary_fit = fitted.summary()
    # writing to file the summary of the model
    text_file = open(out0, "w")
    # please not the presence of str: this is used to make
    # possible to write to file the summary
    text_file.write(str(summary_fit))
    text_file.close()
    return formula_str,model,fitted
#---
# function to perform a multicollinearity test
# calculation of the condition number
#---
def calculate_condition_number():
    condition_number = np.linalg.cond(fitted.model.exog)
    condition_number = "{:.3f}".format(condition_number)
    return condition_number
#---
# function to perform a multicollinearity test
# calculation of variation inflation
#---
def calculate_variation_inflation_factor():
    matrix = []
    print(' ')
    print(' Multicollinearity test: calculation of Variance Inflation Factor')
    #
    for i in range(len(df1.columns[:-1])):
        v = vif(np.matrix(df1[:-1]),i)
        names = df1.columns[i]
        matrix.append([names, v])
        print(' Variance inflation factor for {}: {}'.format(df1.columns[i],round(v,2)))
    df_variation_inflation = pd.DataFrame(matrix)
    df_variation_inflation.columns = ['feature','Variance inflation factor']
    return df_variation_inflation
#---
# function to calculate correlation matrix and 
# write it to dataframe 
# this is a quantification/visualisation of multicollinearity too
#---
def calculate_correlation_matrix():
    corr = df1[:-1].corr()
    return corr
#---
# function for creating a heatmap 
# of the correlations
# this is a quantification/visualisation of multicollinearity too 
#---
def graph_heatmap_correlation():
    plt.figure(figsize=(8,5))
    plt.title('Heatmap Correlation Values (Multicollinearity)', fontsize=16)
    #
    heat_map = sn.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    #
    plt.yticks(fontsize=5)
    plt.xticks(fontsize=5,rotation = 30)
    plt.savefig(out3, dpi = 600)
    plt.close()
    return 
#
#-----
# main
#-----
#
# reading dataframe
df1 = read_df(input)
# constructing and fitting model
formula_str,model,fitted = construct_fit_model()
# calculating the condition number
condition_number = calculate_condition_number()
print(' ')
print(' Multicollinearity test: calculation of Condition number')
print(' Condition number:', condition_number)
# calculating variation inflation factor
df_variation_inflation = calculate_variation_inflation_factor()
df_variation_inflation.to_csv(out1, index=False)
# calculating correlation matrix
corr = calculate_correlation_matrix()
corr.to_csv(out2, index=False, float_format='%.3f')
# graph heatmap correlation values
graph_heatmap_correlation()
# elapsed time for the calculations
end_time = time.time()
elapsed_time = end_time - start_time
formatted_time = "{:.2f}".format(elapsed_time)
print(' ')
print(' Elapsed time:', formatted_time, 's')
#
print(' ')
print(' Done!')
print(' ')
print(' Please see the output files')
print(' for further information')
print(' ')
