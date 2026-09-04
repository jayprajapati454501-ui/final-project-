# COVID-19 Data Analysis and Visualization

## Project Overview

This is a Python-based **COVID-19 Data Analysis and Visualization**
project. It uses Pandas and NumPy for data processing and Matplotlib and
Seaborn for creating visualizations.

The project analyzes COVID-19 information such as:

-   Confirmed cases
-   Deaths
-   Recovered cases
-   Active cases
-   Country-wise statistics
-   Date-wise trends
-   Death rate
-   Recovery rate

The current Python program includes a small CSV dataset directly inside
the source code and loads it using Pandas. The dataset contains the
columns `Country`, `Confirmed`, `Deaths`, `Recovered`, `Active`, and
`Date`.

## Features

1.  Load CSV-style COVID-19 data
2.  Explore the dataset
3.  Display the first five records
4.  Display column names
5.  Display dataset information
6.  Generate a statistical summary
7.  Clean duplicate and numeric/date data
8.  Calculate total confirmed cases, deaths, and recoveries
9.  Calculate death and recovery rates
10. Perform country-wise analysis
11. Find countries with the highest confirmed cases, deaths, and
    recoveries
12. Perform date-wise analysis
13. Generate data visualizations
14. Generate a correlation heatmap
15. Generate a complete analysis report
16. Use a menu-driven interface

## Technologies Used

-   **Python**
-   **Pandas** - data loading, cleaning, grouping, and analysis
-   **NumPy** - numerical calculations
-   **Matplotlib** - charts and graphs
-   **Seaborn** - statistical visualizations
-   **io** - reading the embedded CSV string
-   **os** - creating the visualization output folder

## Python Libraries

Install the required libraries with:

``` bash
pip install numpy pandas matplotlib seaborn
```

## Project Structure

``` text
COVID19_Data_Analysis/
│
├── final project rnw.py
├── README.md
│
└── covid_plots/
    ├── top_countries.png
    ├── overall_statistics.png
    ├── covid_time_trend.png
    ├── confirmed_vs_deaths.png
    └── correlation_heatmap.png
```

The `covid_plots` folder is created automatically when the visualization
option is selected.

## Dataset Columns

  Column      Description
  ----------- ------------------------------------
  Country     Name of the country
  Confirmed   Number of confirmed COVID-19 cases
  Deaths      Number of reported deaths
  Recovered   Number of recovered cases
  Active      Number of active cases
  Date        Date of the recorded data

## How the Program Works

### 1. Data Loading

The project stores sample CSV data in the `SAMPLE_CSV_DATA` variable and
uses `io.StringIO()` with Pandas to read it as a CSV dataset.

### 2. Data Exploration

The **Explore Data** option displays:

-   First five records
-   Column names
-   Data information
-   Statistical summary

### 3. Data Cleaning

The **Clean Data** option:

-   Checks missing values
-   Removes duplicate rows
-   Converts numeric columns to numeric data types
-   Converts the `Date` column to Pandas datetime format
-   Replaces invalid numeric values with zero

### 4. Total Statistics

The program calculates:

-   Total confirmed cases
-   Total deaths
-   Total recovered cases
-   Death rate
-   Recovery rate

### 5. Country Analysis

The country analysis groups the data by country and calculates:

-   Total confirmed cases
-   Total deaths
-   Total recovered cases
-   Death rate
-   Recovery rate

### 6. Top Countries

The program displays the top countries based on:

-   Confirmed cases
-   Deaths
-   Recoveries

### 7. Date Analysis

The program groups the data by date and calculates confirmed cases,
deaths, and recoveries for each date.

### 8. Visualization

The project creates the following graphs:

#### Top Countries Bar Chart

Shows countries with the highest confirmed COVID-19 cases.

#### Overall Statistics Chart

Compares total confirmed cases, deaths, and recoveries.

#### COVID-19 Time Trend

Shows confirmed cases, deaths, and recoveries over time.

#### Confirmed Cases vs Deaths

A scatter plot showing the relationship between confirmed cases and
deaths.

#### Correlation Heatmap

Shows correlations between numerical COVID-19 variables.

## Menu

When the program runs, the following menu is displayed:

``` text
============================================================
                COVID-19 DATA ANALYZER
============================================================

1. Explore Data
2. Clean Data
3. Total COVID-19 Statistics
4. Country Analysis
5. Top Countries
6. Date Analysis
7. Generate Visualizations
8. Generate Complete Report
0. Exit

============================================================
```

## How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation:

``` bash
python --version
```

### Step 2: Install Libraries

``` bash
pip install numpy pandas matplotlib seaborn
```

### Step 3: Run the Project

Open a terminal in the project folder and run:

``` bash
python "final project rnw.py"
```

### Step 4: Select an Option

Enter a number from `0` to `8`.

For example:

``` text
Enter your choice: 7
```

This generates the visualization files in the `covid_plots` folder.

## Example Output

``` text
============================================================
       COVID-19 DATA ANALYSIS PROJECT
============================================================

============================================================
CSV DATA LOADED SUCCESSFULLY
============================================================
Rows: 15
Columns: 6
```

A complete report can be generated by selecting:

``` text
8. Generate Complete Report
```

## Visualization Output

After selecting option `7`, the program saves:

``` text
covid_plots/
├── top_countries.png
├── overall_statistics.png
├── covid_time_trend.png
├── confirmed_vs_deaths.png
└── correlation_heatmap.png
```

## Main Class

The project uses an object-oriented programming approach with the class:

``` python
class CovidDataAnalyzer:
```

Important methods include:

``` python
load_data()
explore_data()
clean_data()
total_statistics()
country_analysis()
top_countries()
date_analysis()
visualize()
generate_report()
```

## Learning Objectives

This project helps demonstrate practical use of:

-   Python classes and objects
-   Functions and methods
-   Pandas DataFrames
-   CSV data handling
-   Data cleaning
-   Data grouping
-   NumPy calculations
-   Statistical analysis
-   Matplotlib visualization
-   Seaborn visualization
-   File/folder handling
-   Menu-driven programming
-   Exception handling

## Future Improvements

The project can be extended by:

-   Allowing the user to enter an external CSV file path
-   Adding an interactive Plotly dashboard
-   Adding more countries and dates
-   Adding filters by country and date
-   Exporting analysis results to a new CSV file
-   Creating an interactive web dashboard
-   Adding more statistical metrics

## Author

**Python Data Analysis Project**

## License

This project is intended for educational and learning purposes.
