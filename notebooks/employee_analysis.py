#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Employee Data Analysis

## 1. Load the Data

## 2. Explore the Employees

## 3. Salary Analysis

## 4. Findings and Conclusion


# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("../data/employees.csv")

print(df.head())
print(df.info())
print(df.describe())


# In[5]:


get_ipython().run_line_magic('timeit', 'df["salary"].mean()')


# In[6]:


print(df[df["city"] == "Chennai"])


# In[7]:


df.groupby("department")["salary"].mean().plot(kind="bar")
plt.ylabel("Average Salary")
plt.title("Average Salary by Department")
plt.tight_layout()
plt.show()


# In[ ]:




