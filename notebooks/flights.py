#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[30]:


data_csv = pd.read_csv("../data/flights.csv")
df = pd.DataFrame(data_csv).set_index("id")


# In[ ]:


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

df_cl = pd.DataFrame(
    list(columns_legend.items()), columns=["Column Name", "Description"]
)
df_cl = df_cl.style.set_properties(**{"text-align": "left"})
df_cl  


# In[32]:


df.attrs = columns_legend


# ## DataFrame Exploration
# 
# - Summarize & Visualize Data
# - Identify Patterns
# - Find Relationships
# - Note Potential Anomalies
# 
# ## Exploration Scope
# 
# We want to know two things:
# 
# - What causes flight delays
# - How can we better predict delays
# 

# In[ ]:


# Examine DataFrame attributes and structure
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
# 

# In[ ]:


df.isnull().sum()


# In[36]:


df = df.dropna(how="any")


# In[ ]:


df.isnull().sum()


# In[ ]:


df.sample(n=5)


# In[39]:


df.dep_time = df.dep_time.astype(int)  
df.dep_time = df.dep_time.astype(str).str.zfill(4) 
df.sched_dep_time = df.sched_dep_time.astype(str).str.zfill(
    4
)  

df.dep_time = pd.to_datetime(df.dep_time, format="%H%M%S").dt.strftime("%H:%M:%S")
df.sched_dep_time = pd.to_datetime(df.sched_dep_time, format="%H%M%S").dt.strftime(
    "%H:%M:%S"
)


# In[ ]:


df[["dep_time", "sched_dep_time"]].sample(n=5)


# In[ ]:


x = df.sched_dep_time[::15000]
y = df.dep_time[::15000]

plt.title = "Departure Discrepancies"
plt.xlabel = "Departure Time"
plt.ylabel = "Scheduled Departure Time"

plt.figure(figsize=(18, 12)).tight_layout()
plt.plot(x, y)

plt.show()


# In[ ]:


y1 = df.dep_time[::1500]
y2 = df.sched_dep_time[::1500]

fig, ax1 = plt.subplots()

ax1.plot(y1, color="purple")
ax1.set_xlabel("Scheduled Departure Time")
ax1.tick_params(axis="y", labelcolor="#89d728")
ax1.set_yticks(range(0, 24))  
ax1.set_ylabel("Hour of day")

ax2 = ax1.twin()
ax2.plot(y2, color="pink", label="Departure Time")
ax2.tick_params(axis="y", labelcolor="#89d728")

fig.tight_layout()

plt.show()


# In[ ]:




