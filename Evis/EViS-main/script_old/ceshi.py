
import os
import pandas as pd


file_dir = 'E:/COVIDVS-master/dataset/ceshi/'
file_lists = os.listdir(file_dir)
print(file_lists)
tep = []
for file in file_lists:
    a_file = file_dir + file
    tep.extend(list(pd.read_csv(a_file, header=None, sep='\t')[0]))
dataf = pd.Series(tep)
dataf.to_csv('./huizong.csv', index=False, encoding='utf-8', header=False)