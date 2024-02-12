# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 08:30:00 2023

@author: sai
"""


import pandas as pd
df=pd.read_csv("C:/2-dataset/ethnic.csv")
df.var()

#here empid and zip is nominal data so ignor it.
# for checking var is zero or not
df.var()==0  

#none of them are equal to zero
df.var(axis=0)==0 

#there is no varience so it give false as output.if var is present then true















