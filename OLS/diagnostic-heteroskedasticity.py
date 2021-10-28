#
# name: diagnostic-heteroskedasticity.py
name='diagnostic-heteroskedasticity'
description='Diagnostic of Heteroskedasticity: Breush-Pagan and Goldfeld-Quandt'
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
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='breush-pagan-heteroskedasticity-test.log'
out2='goldfeld-quandt-heteroskedasticity-test.log'
out3='fitted-vs-residuals-heteroskedasticity.jpeg'
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
# function to perform a Breush-Pagan test
# Heteroskedasticity
#---
def perform_Breush_Pagan_test():
    name = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
    breush_pagan_test = sms.het_breuschpagan(fitted.resid, fitted.model.exog)
    breush_pagan_file = open(out1, "w")
    breush_pagan_file.write('Breush-Pagan Heteroskedasticity Test \n')
    breush_pagan_file.write('%s %10.10f\n' % ('Lagrange multiplier statistic = ',breush_pagan_test[0]))
    breush_pagan_file.write('%s %10.10f\n' % ('p-value                       = ',breush_pagan_test[1]))
    breush_pagan_file.write('%s %10.10f\n' % ('f-value                       = ',breush_pagan_test[2]))
    breush_pagan_file.write('%s %10.10f\n' % ('f p-value                     = ',breush_pagan_test[3]))
    return breush_pagan_test
#---
# function to perform a Goldfeld-Quandt test
# Heteroskedasticity
#---
def perform_Goldfeld_Quandt_test():
    name = ['F statistic', 'p-value']
    goldfeld_quandt_test = sms.het_goldfeldquandt(fitted.resid, fitted.model.exog)
    goldfeld_quandt_file = open(out2, "w")
    goldfeld_quandt_file.write('Goldfeld-Quandt Heteroskedasticity Test \n')
    goldfeld_quandt_file.write('%s %10.10f\n' % ('F statistic = ',goldfeld_quandt_test[0]))
    goldfeld_quandt_file.write('%s %10.10f\n' % ('p-value     = ',goldfeld_quandt_test[1]))
    return goldfeld_quandt_test
#---
# function for creating graph of
# fitted vs residuals (visualising constant variance assumption)
# Heteroskedasticity
#---
def graph_fitted_vs_residuals_heteroskedasticity():
    plt.figure(figsize=(8,5))
    p=plt.scatter(x=fitted.fittedvalues,y=fitted.resid,edgecolor='k')
    xmin=min(fitted.fittedvalues)
    xmax = max(fitted.fittedvalues)
    plt.hlines(y=0,xmin=xmin*0.9,xmax=xmax*1.1,color='red',linestyle='--',lw=3)
    plt.xlabel("Fitted values",fontsize=15)
    plt.ylabel("Residuals",fontsize=15)
    plt.title("Fitted vs. residuals plot",fontsize=18)
    plt.grid(True)
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
# performing the Breush-Pagan test
breush_pagan_test = perform_Breush_Pagan_test()
# performing the Goldfeld Quandt test
goldfeld_quandt_test = perform_Goldfeld_Quandt_test()
# plotting fitted vs residuals for visualisation of heteroskedasticity
graph_fitted_vs_residuals_heteroskedasticity()
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
