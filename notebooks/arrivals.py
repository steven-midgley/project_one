#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing necessary libraries 
import sys
import os

os.path.exists("../data/arrivals.csv")

sys.path.append(os.path.abspath(".."))
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


data_csv = pd.read_csv("../data/arrivals.csv")
arv_df = pd.DataFrame(data_csv)


# In[3]:


data_csv = pd.read_csv("../data/flights_by_aircraft.csv")
a_crft_df = pd.DataFrame(data_csv)


# In[ ]:


a_crft_df.sample(n=5)


# In[ ]:


arv_df.sample(n=5)


# In[ ]:


arv_df.info()


# In[ ]:


arv_df.isnull().sum()


# In[ ]:


arv_df.isna().sum()


# In[9]:


arv_df = arv_df.dropna(how="any")


# In[ ]:


arv_df.isna().sum()


# In[ ]:


arv_df.info()


# In[ ]:


arv_df[["dist_frm_orig_v", "dist_frm_orig_h"]].plot()


# In[ ]:


arv_df.sample(n=5)


# In[ ]:




