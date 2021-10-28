#
# name: diagnostic-linearity
name='diagnostic-linearity'
description='Diagnostic of Linearity: Rainbow and Harvey-Collier tests'
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
# sys
import sys
# traceback
import traceback
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
# import matplotlib
import matplotlib.pyplot as plt
# import statsmodels
import statsmodels.formula.api as smf
import statsmodels.stats.api as sms
from statsmodels.compat import lzip
# import seaborn
import seaborn as sn
#
# declaring the files of input and output
in1='dataframe-statsmodels.csv'
# output files
out0='fit-model.log'
out1='rainbow-linearity-test.log'
out2='harvey-collier-linearity-test.log'
#
# to calculate elapsed time
start_time = time.time()
print(' ')
print('',name)
print('',description)
print(' Python version:', platform.python_version())
print(' version: ',version)
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
# function for diagnostic linearity
# using the Rainbow Linearity Test
#---
def run_rainbow_linearity_test():
    rainbow_test = sms.linear_rainbow(fitted)
    # writing to file the result of the test
    rainbow_file = open(out1, "w")
    rainbow_file.write('Rainbow Linearity Test \n')
    rainbow_file.write('%s %10.4f\n' % ('Fstat  = ',rainbow_test[0]))
    rainbow_file.write('%s %10.4f\n' % ('Pvalue = ',rainbow_test[1]))
    return rainbow_test
#---
# function for diagnostic linearity
# using the Harvey-Collier Test
#---
def run_harvey_collier_linearity_test():
    try:
        harvey_collier_test = sms.linear_harvey_collier(fitted)
        harvey_collier_file = open(out2, "w")
        harvey_collier_file.write('Harvey-Collier Linearity Test \n')
        harvey_collier_file.write('%s %10.4f\n' % ('T value  = ',harvey_collier_test[0]))
        harvey_collier_file.write('%s %10.4f\n' % ('P value  = ',harvey_collier_test[1]))
    except:
        print(' Harvey-Collier Linearity Test Failed!')
        print(' Trigger Exception, traceback info forward to log file.')
        traceback.print_exc(file=open(out2,'w'))
        return()
    return harvey_collier_test
#
#-----
# main
#-----
#
# reading dataframe
df1 = read_df(input)
# constructing and fitting model
formula_str,model,fitted = construct_fit_model()
# running Rainbow Linearity Test
print(' Running Rainbow Linearity Test')
print(' ')
rainbow_test = run_rainbow_linearity_test()
# running Harvey-Collier Linearity Test
print(' Running Harvey-Collier Linearity Test')
print(' ')
harvey_collier_test = run_harvey_collier_linearity_test()
#
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
