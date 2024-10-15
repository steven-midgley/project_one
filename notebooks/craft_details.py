#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd

if not os.path.exists("../data/craft_details.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    flights_csv_path = os.path.join(current_dir, "../data/craft_details.csv")
else:
    flights_csv_path = "../data/craft_details.csv"

if os.path.exists(flights_csv_path):
    data_csv = pd.read_csv(flights_csv_path)
    f_sts_df = pd.DataFrame(data_csv)
else:
    raise FileNotFoundError(f"CSV file not found: {flights_csv_path}")


# In[ ]:




