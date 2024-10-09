# Project 1: Analyzing Flight Behavior Patterns ✈️

<div style="text-align: center;">
    <img src="images/airplane.jpeg" alt="Airplane" width="500" />
</div>

---

## Table of Contents

- [Project Overview](#project-overview)
- [Objectives](#objectives)
- [Data Sources](#data-sources)
- [Quickstart Guide](#quickstart-guide)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Results and Insights](#results-and-insights)
- [Conclusion](#conclusion)
- [How to Use](#how-to-use)
- [References and Credits](#references-and-credits)
- [Deployment Workflow](#deployment-workflow)
- [Branch Discipline](#branch-discipline)
- [Team Members](#team-members)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This project focuses on analyzing flight behavior patterns using a comprehensive dataset sourced from Kaggle and the OpenSky API. By examining various aspects of flight data, including departure and arrival times, flight durations, delays, and other relevant variables, we aim to uncover meaningful patterns and correlations that can provide insights into airline operations.

Our primary goal is to identify trends that can assist airlines and stakeholders in optimizing flight schedules, improving operational efficiency, and enhancing passenger experience. Through data analysis techniques such as statistical analysis, and data visualization, we hope to reveal insights that can lead to actionable recommendations for decision-makers in the aviation industry.

By leveraging advanced analytics, this project aspires to contribute to the ongoing efforts to enhance the effectiveness and reliability of air travel, ultimately benefiting both airlines and their passengers.

---

## Objectives

- Add info here ... (Include measurable goals like predicting flight delays, identifying delay trends, etc.)

---

## Data Sources 

### Kaggle Flight Data
- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights)
The dataset from Kaggle includes historical flight data with over 1 million records. Key columns include:

| Column         | Description                                                  |
|----------------|--------------------------------------------------------------|
| `id`           | Unique flight identifier                                     |
| `dep_time`     | Actual departure time (24-hour format)                       |
| `arr_time`     | Actual arrival time (24-hour format)                         |
| `dep_delay`    | Departure delay in minutes                                   |
| `arr_delay`    | Arrival delay in minutes                                     |
| `carrier`      | Two-letter airline carrier code                              |
| `origin`       | Origin airport code                                          |
| `dest`         | Destination airport code                                     |
| `distance`     | Distance traveled (miles)                                    |
| `air_time`     | Total time in the air (minutes)

### OpenSky API Data
- [OpenSky API](https://github.com/openskynetwork/opensky-api)
The OpenSky API provides real-time flight tracking. This data can be used to compare with historical data to enhance predictions or validate findings.

---

## Quickstart Guide

### 1. **Install Project Dependencies**

**All required dependencies are stored in [requirements.txt](requirements.txt)**

- Open the terminal (VS Code terminal shortcut: macOS `Control + tilde` | Windows `Ctrl + backtick`).
- Ensure you are in the project root directory, then run:

     ```bash
     pip install -r requirements.txt
     ```

### 2. **Download Flight Data from Kaggle**

   **(Note: Data is already included; skip unless necessary.)**  

- Steps to download the data:
     1. Create a free [Kaggle account](https://www.kaggle.com/account/login).
     2. In Kaggle's settings, generate an API key and download `kaggle.json`.
     3. Copy `kaggle.json` to the project root and set permissions (Linux/macOS/WSL):

        ```bash
        chmod 600 kaggle/kaggle.json
        ```

     4. Download the dataset:

        ```bash
        kaggle datasets download -d mahoora00135/flights
        ```

     5. Unzip and move the `flights.csv` file to the `data` folder.

### 3. **Install OpenSky API**

**(Optional: Use the OpenSky API if additional features are needed after completing tasks with the Kaggle data.)**

- Install OpenSky API dependencies:

     ```bash
     pip install -e src/python3/python
     ```

- If you encounter issues with `python3`, use `python`.

---

## Exploratory Data Analysis (EDA)

### Key Insights from Flight Data
- Add info here... (Summarize the key insights and trends found during your data exploration, such as peak delay times or busiest airports.)

### Sample Visualizations

#### Visualization 1 
![XXXXXX](images/XXXX.png)
Explanation:

#### Visualization 2 
![XXXXXX](images/XXXX.png)
Explanation:

- **Recommendation:** Add info here.... (Offer any recommendations based on your analysis.)

---

## Results and Insights

- Add info here.... (Describe the results you obtained, highlighting any important findings related to flight delays or predictions.) 

---

## Conclusion

Add info here... (Summarize the overall findings and the value of the analysis.)

### Future Work:
- Add info here... (List any areas for improvement or further analysis, such as incorporating weather data or expanding the dataset.) 

---

## How to Use

1. **Download Flight Data:** The dataset is available in the `data/` folder. You can also download the latest data from Kaggle as mentioned in the [Quickstart Guide](#quickstart-guide).
2. **Run the Jupyter Notebook:** Navigate to the `notebooks/` folder and open `flight_analysis.ipynb`. The notebook includes all code and explanations for the data analysis and machine learning models.
3. **View Visualizations:** All visualizations are saved in the `images/` folder.

## References and Credits
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/)
- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights)

---

## Deployment Workflow

### 1. **Branching and Git Commands**

- Create a new branch for each task.
- If not on `main`, switch to it:

     ```bash
     git switch main
     git pull origin main
     git checkout -b <branch-name>
     ```

- Commit and push frequently:

     ```bash
     git status
     git add .
     git commit -m 'commit message'
     git push
     ```

- For the first push of a new branch:

     ```bash
     git push --set-upstream origin <branch-name>
     ```
---

## Branch Discipline

- **Protected Branch:** `main` – Managed by the project manager. No direct pushes allowed.
- **Testing Branch:** `stage` – All code contributions are merged into `stage` .
- Once `stage` is stable and conflict-free, it will be merged into `main`.

--- 

## Team Members

- **Steven Midgley**
- **Dane Larsen**
- **Leslie Barrera Dorantes**

--- 

## Acknowledgments

We would like to express our sincere gratitude to the following individuals and organizations for their invaluable contributions to this project:

- **Firas Obeid**: For providing guidance and support throughout the project.
- **Kaggle**: For the dataset that served as a foundation for our analysis.
- **OpenSky API**: For providing essential data to enhance our understanding of flight behavior.

Additionally, we appreciate the collaborative environment fostered by our AI boot camp, which enabled us to work together effectively and learn from each other.

Thank you to everyone who has contributed to this project’s success! 