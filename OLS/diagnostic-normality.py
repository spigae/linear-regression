#
# name: diagnostic-normality
name='diagnostic-normality'
description='Diagnostic of Normality: plots and various tests...'
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
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.graphics.gofplots import qqplot
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='predicted-variables-vs-residuals (plots)'
out2='Q-Q-plot-normalized-residuals (plots)'
out3='shapiro-wilk-normality-test.log'
out4='dagostino-K2-normality-test.log'
out5='jarque-bera-normality-test.log'
out6='omni-normality-test.log'
out7='histogram-normalized-residuals.jpeg'
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
print(' output 4: ',out4)
print(' output 5: ',out5)
print(' output 6: ',out6)
print(' output 6: ',out7)
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
# function for creating graphs of
# predicted variables vs residuals
#---
def graph_predicted_variables_vs_residuals():
    i = 0
    for c in df1.columns[:-1]:
        i += 1
        plt.figure(figsize=(8,5))
        plt.title("{} vs. Model residuals".format(c),fontsize=16)
        plt.scatter(x=df1[c],y=fitted.resid,color='blue',edgecolor='k')
        plt.grid(True)
        xmin=min(df1[c])
        xmax = max(df1[c])
        plt.hlines(y=0,xmin=xmin*0.9,xmax=xmax*1.1,color='red',linestyle='--',lw=3)
        plt.xlabel(c,fontsize=14)
        plt.ylabel('Residuals',fontsize=14)
        plt.savefig('predicted-variables-vs-residuals-' + str(i) + '.jpeg', dpi = 600)
        plt.close()
    return
#---
# function for creating graph of
# Q-Q plot of the residuals
#---
def graph_q_q_plot_residuals():
    plt.figure(figsize=(8,5))
    fig=qqplot(fitted.resid_pearson,line='45',fit='True')
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.xlabel("Theoretical quantiles",fontsize=15)
    plt.ylabel("Sample quantiles",fontsize=15)
    plt.title("Q-Q plot of normalized residuals",fontsize=18)
    plt.grid(True)
    plt.savefig('Q-Q-plot-normalized-residuals.jpeg', dpi = 600)
    plt.close()
    return
#---
# function to perform
# Normality (Shapiro-Wilk) test of the residuals
#---
def perform_normality_shapiro_wilk_test():
    # alpha threshold
    alpha = 0.05
    shapiro_test = shapiro(fitted.resid)
    w_stat = shapiro_test[0]
    pvalue = shapiro_test[1]
    #print w_stat,pvalue
    shapiro_file = open(out3, "w")
    shapiro_file.write('SciPy Shapiro Wilk Test \n')
    shapiro_file.write('The null hypothesis H0 is that \n')
    shapiro_file.write('the data is normally distributed \n')
    shapiro_file.write('%s %3.2f\n' % ('alpha  = ',alpha))
    shapiro_file.write(' \n')
    if pvalue < alpha:
        shapiro_file.write('%s %10.4f\n' % ('P-value  = ',pvalue))
        shapiro_file.write('Reject the null hypothesis H0, not normal \n')
    else:
        shapiro_file.write('%s %10.4f\n' % ('P-value  = ',pvalue))
        shapiro_file.write('Fail to reject the null hypothesis H0, normal \n')
    return
#---
# function to perform
# Normality (D'Agostino's K2) test of the residuals
#---
def perform_normality_dagostinos_test():
    # alpha threshold
    alpha = 0.05
    dagostinos_test = normaltest(fitted.resid)
    w_stat = dagostinos_test[0]
    pvalue = dagostinos_test[1]
    #print w_stat,pvalue
    dagostino_file = open(out4, "w")
    dagostino_file.write('SciPy D Agostino s K2 Test \n')
    dagostino_file.write('The null hypothesis H0 is that \n')
    dagostino_file.write('the data is normally distributed \n')
    dagostino_file.write('%s %3.2f\n' % ('alpha  = ',alpha))
    dagostino_file.write(' \n')
    if pvalue < alpha:
        dagostino_file.write('%s %10.4f\n' % ('P-value  = ',pvalue))
        dagostino_file.write('Reject the null hypothesis H0, not normal \n')
    else:
        dagostino_file.write('%s %10.4f\n' % ('P-value  = ',pvalue))
        dagostino_file.write('Fail to reject the null hypothesis H0, normal \n')
    return
#---
# function for diagnostic normality residuals
# with the Jarque-Bera test
#---
def perform_normality_jarque_bera_test():
    jarque_bera_test = sms.jarque_bera(fitted.resid)
    jarque_bera_file = open(out5, "w")
    jarque_bera_file.write('Jarque-Bera Normality Test \n')
    jarque_bera_file.write('%s %10.4f\n' % ('Jarque-Bera              = ',jarque_bera_test[0]))
    jarque_bera_file.write('%s %10.4f\n' % ('Chi^2 two-tail prob.     = ',jarque_bera_test[1]))
    jarque_bera_file.write('%s %10.4f\n' % ('Skew (Gaussian skew = 0)     = ',jarque_bera_test[2]))
    jarque_bera_file.write('%s %10.4f\n' % ('Kurtosis (Gaussian kurt = 3) = ',jarque_bera_test[3]))
    return jarque_bera_test
#---
# function for diagnostic normality residuals
# with the Omni test
#---
def perform_normality_omni_test():
    omni_test = sms.omni_normtest(fitted.resid)
    omni_file = open(out6, "w")
    omni_file.write('Omni Normality Test \n')
    omni_file.write('%s %10.4f\n' % ('Chi^2          = ',omni_test[0]))
    omni_file.write('%s %10.4f\n' % ('Two-tail prob. = ',omni_test[1]))
    return omni_test
#---
# function for creating graph of
# histogram normalized residuals
#---
def graph_histogram_normalized_residuals():
    plt.figure(figsize=(8,5))
    plt.hist(fitted.resid_pearson,bins=20,edgecolor='k')
    plt.ylabel('Count',fontsize=15)
    plt.xlabel('Normalized residuals',fontsize=15)
    plt.title("Histogram of normalized residuals",fontsize=18)
    plt.savefig(out7, dpi = 600)
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
# graph_predicted_variables_vs_residuals
print(' Graph Predicted Variables vs residuals')
graph_predicted_variables_vs_residuals()
# graph_q_q_plot_residuals
print(' Graph QQ residuals')
graph_q_q_plot_residuals()
# performing Normality (Shapiro-Wilk) test of the residuals
print(' Shapiro-Wilk Test of Normality')
perform_normality_shapiro_wilk_test()
# performing Normality D'Agostino's K2 test of the residuals
print(' D Agostino K2 Test of residual ')
perform_normality_dagostinos_test()
# jarque_bera_test
print(' Jarque-Bera Test of Normality')
jarque_bera_test = perform_normality_jarque_bera_test()
# omni_test
print(' Omni Test of Normality')
omni_test = perform_normality_omni_test()
# histogram normalized residuals
print( ' Graph histogram Normalized residuals')
graph_histogram_normalized_residuals()
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
