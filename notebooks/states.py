#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Importing necessary libraries for data manipulation and visualization
import sys
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium


# In[18]:


import os
import pandas as pd

# Example condition: only generate the path if the file does not already exist
if not os.path.exists("../data/flight_states.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    flights_csv_path = os.path.join(current_dir, "../data/flight_states.csv")
else:
    flights_csv_path = "../data/flight_states.csv"  # Use the relative path directly

# Print the path to debug (optional)
print(f"Using CSV file at: {flights_csv_path}")

# Check if the file exists and then read it
if os.path.exists(flights_csv_path):
    data_csv = pd.read_csv(flights_csv_path)
    f_sts_df = pd.DataFrame(data_csv)
else:
    raise FileNotFoundError(f"CSV file not found: {flights_csv_path}")


# In[19]:


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


# In[20]:


f_sts_df = f_sts_df[f_sts_df.category > 0]


# In[21]:


def get_flights():
    return f_sts_df


# In[22]:


def get_flight_details():
    icao24_craft = pd.DataFrame(f_sts_df[f_sts_df.icao24 == "adc9b6"])
    icao24_craft = icao24_craft.dropna(how="any")
    return icao24_craft


# In[ ]:
