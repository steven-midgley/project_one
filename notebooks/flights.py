#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[30]:


# Read CVS and create DataFrame
data_csv = pd.read_csv("../data/flights.csv")
df = pd.DataFrame(data_csv).set_index("id")


# In[ ]:


# Create a dictionary that describes the columns in the DataFrame
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

# Display legend as DataFrame
df_cl = pd.DataFrame(
    list(columns_legend.items()), columns=["Column Name", "Description"]
)
df_cl = df_cl.style.set_properties(**{"text-align": "left"})
df_cl  # Display the colum legend DataFrame


# In[32]:


# Give columns_legend to the DataFrame as attributes
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
df.attrs  # Display the column legents attached to the DataFrame


# In[ ]:


# Provide a summary of the DataFrame, including data tyoes and non-null counts
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


# Check for null values in the DataFrame and display the count
df.isnull().sum()


# In[36]:


# Drop rows with any null values
df = df.dropna(how="any")


# In[ ]:


# Verify that there are no more null values
df.isnull().sum()


# In[ ]:


# Display a random sample of 5 rows from the DataFrame
df.sample(n=5)


# In[39]:


# Convert departure time to integer and then to a string with zero-padding
df.dep_time = df.dep_time.astype(int)  # Convert to int
df.dep_time = df.dep_time.astype(str).str.zfill(4)  # Pad with zeros
df.sched_dep_time = df.sched_dep_time.astype(str).str.zfill(
    4
)  # Same for scheduled departure time

# Convert the string representation of time to datetime format and format it as HH:MM:SS
df.dep_time = pd.to_datetime(df.dep_time, format="%H%M%S").dt.strftime("%H:%M:%S")
df.sched_dep_time = pd.to_datetime(df.sched_dep_time, format="%H%M%S").dt.strftime(
    "%H:%M:%S"
)


# In[ ]:


# Display a random sample of 5 rows for the updated departure times
df[["dep_time", "sched_dep_time"]].sample(n=5)


# In[ ]:


# Select every 15000th entry for both scheduled and actual departure times
x = df.sched_dep_time[::15000]
y = df.dep_time[::15000]

# Set plot title and labels for the first plot
plt.title = "Departure Discrepancies"
plt.xlabel = "Departure Time"
plt.ylabel = "Scheduled Departure Time"

# Create the first plot with specified figure size and layout
plt.figure(figsize=(18, 12)).tight_layout()
plt.plot(x, y)

# Show the plot
plt.show()


# In[ ]:


# Select every 1500th entry for a more detailed view
y1 = df.dep_time[::1500]
y2 = df.sched_dep_time[::1500]

# Create a new figure for the second plot with dual y-axes
fig, ax1 = plt.subplots()

# Plot the scheduled departure time on the first y-axis
ax1.plot(y1, color="purple")
ax1.set_xlabel("Scheduled Departure Time")
ax1.tick_params(axis="y", labelcolor="#89d728")
ax1.set_yticks(range(0, 24))  # Set y-ticks to hours of the day
ax1.set_ylabel("Hour of day")

# Create a twin y-axis for the actual departure time
ax2 = ax1.twin()
ax2.plot(y2, color="pink", label="Departure Time")
ax2.tick_params(axis="y", labelcolor="#89d728")

# Adjust layout for the second plot
fig.tight_layout()

# Show the second plot
plt.show()


# In[ ]:




