<div style="text-align: center; color: blue;">
    <h1>Project 1: Analyzing Flight Behavior Patterns</h1>
</div>

<div style="text-align: center;">
    <img src="images/airplane.jpeg" alt="Airplane" width="500" />
</div>

## Project Overview

Add info here... (Describe the purpose of the project, the data you're using, and the goals you want to achieve.)

## Objectives

- Add info here ... (Include measurable goals like predicting flight delays, identifying delay trends, etc.)

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

## Results and Insights

- Add info here.... (Describe the results you obtained, highlighting any important findings related to flight delays or predictions.) 

## Conclusion

Add info here... (Summarize the overall findings and the value of the analysis.)

### Future Work:
- Add info here... (List any areas for improvement or further analysis, such as incorporating weather data or expanding the dataset.) 

## How to Use

1. **Download Flight Data:** The dataset is available in the `data/` folder. You can also download the latest data from Kaggle as mentioned in the [Quickstart Guide](#quickstart-guide).
2. **Run the Jupyter Notebook:** Navigate to the `notebooks/` folder and open `flight_analysis.ipynb`. The notebook includes all code and explanations for the data analysis and machine learning models.
3. **View Visualizations:** All visualizations are saved in the `images/` folder.

## References and Credits
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [OpenSky Network API](https://openskynetwork.github.io/opensky-api/)
- [Kaggle Dataset](https://www.kaggle.com/datasets/mahoora00135/flights)

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

## Branch Discipline

- **Protected Branch:** `main` – Managed by the project manager. No direct pushes allowed.
- **Testing Branch:** `stage` – All code contributions are merged into `stage` .
- Once `stage` is stable and conflict-free, it will be merged into `main`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.