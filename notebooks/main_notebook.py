#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing Libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# something needed for heat maps..... 🤔
import seaborn as sns
import missingno as msno


# In[2]:


# Suppress Warning DO NOT LEAVE THIS ON ALL THE TIME CAN MUTE ERRORS!!
import warnings

# Suppress specific warnings
warnings.simplefilter(action="ignore", category=UserWarning)


# In[ ]:


# Read csv and create DataFrame
data_csv = pd.read_csv("../data/flights.csv")
df = pd.DataFrame(data_csv).set_index("id")


# In[ ]:


# Create column descriptions
"""
  
"""
columns_legend = {
    "id": "Unique identifier for each flight record",
    "year": "Year the flight was recorded (Gregorian calendar)",
    "month": "Numerical value of the month the flight occurred (1-12)",
    "day": "Day of the month when the flight occurred (1-31)",
    "dep_time": "Actual departure time (24-hour format, hhmm)",
    "sched_dep_time": "Scheduled departure time (24-hour format, hhmm)",
    "dep_delay": "Minutes difference between scheduled and actual departure (positive for delay, negative for early departure)",
    "arr_time": "Actual arrival time (24-hour format, hhmm)",
    "sched_arr_time": "Scheduled arrival time (24-hour format, hhmm)",
    "arr_delay": "Minutes difference between scheduled and actual arrival (positive for delay, negative for early arrival)",
    "carrier": "Two-letter airline carrier code (e.g., AA for American Airlines)",
    "flight": "Flight number assigned to the flight",
    "tailnum": "Unique aircraft tail number",
    "origin": "Three-letter code of the departure airport",
    "dest": "Three-letter code of the destination airport",
    "air_time": "Total time in the air, in minutes (excludes ground time)",
    "distance": "Distance traveled from origin to destination, in miles",
    "hour": "Hour of scheduled departure time (24-hour format)",
    "minute": "Minute of scheduled departure time",
    "time_hour": "Full timestamp for scheduled departure (yyyy-mm-dd hh:mm:ss, 24-hour format)",
    "name": "Full name of the airline carrier",
}

# Display legend as dataframe
df_cl = pd.DataFrame(
    list(columns_legend.items()), columns=["Column Name", "Description"]
)
df_cl = df_cl.style.set_properties(**{"text-align": "left"})
df_cl


# In[5]:


# Give columns_legend to df as attributes
df.attrs = columns_legend


# ## DataFrame Exploration
# - Summarize & Visualize Data
# - Identify Patterns
# - Find Relationships
# - Note Potential Anomalies
# 
# ## Exploration Scope
# We want to know two things:
# - which airlines have the max/min delays
# - which airport have the max/min delays
# 

# In[ ]:


# Examine df
df.attrs


# In[ ]:


df.info()


# ### Insights from df.info()
# 
# Right away we can see that these columns have missing data.
# This was most likely cause by canceled flights, error in data entry, or a just a simple reporting issue
# 
# ### Follow up Query
# 
# What (if any) patterns are there in the missing data? Such as certain airline, specific times of year, weather patterns, ect.

# In[ ]:


df.isnull().sum()


# In[ ]:


df.isnull().corr()


# In[ ]:


"""
  This is for fun.
  Try and create a heat map to visualize missing data patterns
"""

sns.heatmap(df.isnull())
plt.show()


# In[ ]:


msno.matrix(df)
msno.heatmap(df)


# In[12]:


df = df.dropna(how="any")


# In[ ]:


df.isnull().sum()


# In[ ]:


df.info()


# In[ ]:


df.sample(n=5)


# #### Examine data description
# Isolate relevant columns and study their deviations
# 
# What are we trying to isolate?
# 	- 
# What questions are we trying to answer?

# In[ ]:


"""
  Summarize dataframe.
  
  Not all columns need to or can be summarized. Look
  for columns that can be used to gain better insight
  into flight delays. Columns not specifically used
  for delay tracking may help gain greater insights.
"""

df[
    ["dep_time", "dep_delay", "arr_time", "arr_delay", "air_time", "distance"]
].describe().T


# #### What does this tell us?
# - Average departure delay: 12 minutes
# - Average arrival delay: 6 minutes
# - Average airtime: 150 minutes
# - Average distance: 1048 miles
# 
# ##### follow up questions?
# - What do these numbers tell us?
# - What can we learn from summarizing data based on airlines, aircraft or specific craft number
# Note: Most data analysis is best done with numerical values. 

# #### Convert dep_time & sched_dep_time to 24H timestamp

# In[17]:


"""
  It may be best to create new columns containing the seconds-since-midnight.
  This will let us numerically evaluate the data. As well as create pandas
  datetimestamps for other evaluation methods
"""

dfc = df.copy()

# clean & normalize time columns
dfc.dep_time = dfc.dep_time.astype(int)  # whole int for minutes
dfc.dep_time = dfc.dep_time.astype(str).str.zfill(
    4
)  # zfill(4) is to ensure that all timestamps have 4 digits

dfc.sched_dep_time = dfc.sched_dep_time.astype(str).str.zfill(4)

dfc.dep_delay = dfc.dep_delay.astype(int)

dfc.arr_time = dfc.arr_time.astype(int)
dfc.arr_time = dfc.arr_time.astype(str).str.zfill(4)

dfc.sched_arr_time = dfc.sched_arr_time.astype(str).str.zfill(4)

dfc.arr_delay = dfc.arr_delay.astype(int)

dfc.air_time = dfc.air_time.astype(int)

# Convert columns to datetime
dfc.dep_time = pd.to_datetime(dfc.dep_time, format="%H%M%S").dt.strftime("%H:%M:%S")

dfc.sched_dep_time = pd.to_datetime(dfc.sched_dep_time, format="%H%M%S").dt.strftime(
    "%H:%M:%S"
)

dfc.arr_time = pd.to_datetime(dfc.arr_time, format="%H%M%S").dt.strftime("%H:%M:%S")
dfc.sched_arr_time = pd.to_datetime(dfc.sched_arr_time, format="%H%M%S").dt.strftime(
    "%H:%M:%S"
)

# Create minutes columns
dfc.insert(
    4,
    "dt_min",
    pd.to_datetime(dfc.dep_time).dt.hour * 60 + pd.to_datetime(dfc.dep_time).dt.minute,
)  # this is to keep the original str formate in the dfc.dep_time column

dfc.insert(
    6,
    "sdt_min",
    pd.to_datetime(dfc.sched_dep_time).dt.hour * 60
    + pd.to_datetime(dfc.sched_dep_time).dt.minute,
)

dfc.insert(
    8,
    "rt_min",
    pd.to_datetime(dfc.arr_time).dt.hour * 60 + pd.to_datetime(dfc.arr_time).dt.minute,
)  # this is to keep the original str formate in the dfc.dep_time column

dfc.insert(
    10,
    "srt_min",
    pd.to_datetime(dfc.sched_arr_time).dt.hour * 60
    + pd.to_datetime(dfc.sched_arr_time).dt.minute,
)


# In[ ]:


dfc.sample(n=5)


# In[ ]:


dfc.plot(
    kind="scatter",
    x="dt_min",
    y="sdt_min",
    c="sdt_min",
    cmap="plasma",
    xlabel="departure time",
    ylabel="scheduled departure time",
)
ticks = np.arange(0, 1440, 60)
t_labels = range(24)
plt.xticks(ticks, t_labels)
plt.yticks(ticks, t_labels)
plt.tight_layout()


# In[ ]:


dfc.sample(n=5)


# In[21]:


dfc.dep_time = pd.to_datetime(dfc.dep_time)
dfc.sched_dep_time = pd.to_datetime(dfc.sched_dep_time)

dfc["dep_in_min"] = dfc.dep_time.dt.hour * 60 + dfc.dep_time.dt.minute
dfc["sched_dep_in_min"] = dfc.sched_dep_time.dt.hour * 60 + dfc.sched_dep_time.dt.minute


# In[ ]:


y1 = dfc.dep_time[::500]

y2 = dfc.sched_dep_time[::500]

fig, ax1 = plt.subplots()

# x-axis 1
ax1.scatter(y1, range(len(y1)), color="red", label="Actual Departure")
ax1.tick_params(axis="y", labelcolor="red")

ax1.set_yticks(range(25))
ax1.set_ylabel("Hour of day")

# x-axis 2
ax2 = ax1.twiny()
ax2.scatter(y2, range(len(y2)), color="blue", label="Scheduled Departure")
ax2.tick_params(axis="x", labelcolor="blue")

fig.tight_layout()
plt.show()


# In[ ]:




