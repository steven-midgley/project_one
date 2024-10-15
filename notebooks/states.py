#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
import pandas as pd

if not os.path.exists("../data/flight_states.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    flights_csv_path = os.path.join(current_dir, "../data/flight_states.csv")
else:
    flights_csv_path = "../data/flight_states.csv"

if os.path.exists(flights_csv_path):
    data_csv = pd.read_csv(flights_csv_path)
    f_sts_df = pd.DataFrame(data_csv)
else:
    raise FileNotFoundError(f"CSV file not found: {flights_csv_path}")


# In[10]:


f_sts_df = f_sts_df[f_sts_df.category > 0]
f_sts_df = f_sts_df.dropna(how="any")


# In[11]:


def get_flights():
    return f_sts_df


# In[12]:





# In[ ]:




