#
# name: diagnostic-influence.py
name='diagnostic-influence'
description='Diagnostic of Influence: plots and various tests...'
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
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='influence-tests.csv'
out2='influence-plot.jpeg'
out3='leverage-plot.jpeg'
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
# function to perform influence tests and writing it to a dataframe
#---
def perform_influence_tests():
    df_summary_influence = OLSInfluence(fitted).summary_frame()
    return df_summary_influence
#---
# function to create an influence plot 
# studentized residuals vs H leverage
#---
def graph_influence_plot():
    plt.figure(figsize=(8,5))
    fig = sm.graphics.influence_plot(fitted)
    plt.savefig(out2, dpi = 600)
    plt.close()
    return
#---
# function to create a leverage plot
# leverage vs Normalized residuals
#--- 
def graph_leverage_plot():
    plt.figure(figsize=(8,5))
    sm.graphics.plot_leverage_resid2(fitted)
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
# performing influence tests
print(' Performing influence test')
df_summary_influence = perform_influence_tests()
df_summary_influence.to_csv(out1, index=False)
# creating influence plot
print(' Influence plot')
graph_influence_plot()
# creating leverage plot
print(' Leverage plot')
graph_leverage_plot()
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
