#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Importing necessary libraries for data manipulation and visualization
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium


# In[41]:


current_dir = os.path.dirname(os.path.abspath(__file__))

flights_csv_path = os.path.join(current_dir, "../data/flight_states.csv")

if os.path.exists(flights_csv_path):
    data_csv = pd.read_csv(flights_csv_path)
    f_sts_df = pd.DataFrame(data_csv)
else:
    raise FileNotFoundError(f"CSV file not found: {flights_csv_path}")


# In[43]:


f_sts_df.isna().sum()


# In[44]:


if (
    "sensors" in f_sts_df.columns
    or "position_source" in f_sts_df.columns
    or "spi" in f_sts_df.columns
):
    f_sts_df = f_sts_df.drop("sensors", axis=1)
    f_sts_df = f_sts_df.drop("position_source", axis=1)
    f_sts_df = f_sts_df.drop("spi", axis=1)
else:
    pass


# In[45]:


f_sts_df = f_sts_df[f_sts_df.category > 0]


# In[46]:


f_sts_df.origin_country.value_counts()


# In[47]:


f_sts_df.callsign.value_counts()


# In[48]:


f_sts_df.icao24.value_counts()


# In[49]:


f_sts_df.sample(n=5)


# In[50]:


def get_us_flights():
    US_flights = pd.DataFrame(f_sts_df[f_sts_df.origin_country == "United States"])
    US_flights = US_flights.dropna(how="any")
    return US_flights


# In[53]:


def get_craft_flights():
    icao24_craft = pd.DataFrame(f_sts_df[f_sts_df.icao24 == "adc9b6"])
    icao24_craft = icao24_craft.dropna(how="any")
    return icao24_craft


# In[ ]:




