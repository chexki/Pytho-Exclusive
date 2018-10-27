# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:17:24 2018

@author: Qlc
"""

#%%
## How to load data into python
## ( Following are examples to load CSV, XLSX, TXT [comma delimited] files)

dataset = pd.read_csv(r'E:\Folder1\Foleder\File.csv,encoding='utf-8')     # For CSV
dataset = pd.read_excel(r'E:\Folder1\Foleder\File.xlsx,encoding='utf-8')     # For XLSX
dataset = pd.read_csv(r'E:\Folder1\Foleder\File.txt',header=0,delimiter='\t',low_memory=False)     # For TXT [comma delimited]
                        

#%%
## Find Missing Values

print(dataset.isnull().sum())       # for whole dataset
print(dataset['variable'].isnull().sum())       # for specific variable in dataset    
                        
                        
# Treat Missing Values
                        
dataset = dataset.dropna(subset=['variable']) 

                        
