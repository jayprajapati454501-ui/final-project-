import io
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Built-in sample CSV dataset
SAMPLE_CSV_DATA = """Country,Confirmed,Deaths,Recovered,Active,Date
USA,100000,2000,80000,18000,2023-01-01
India,80000,1500,70000,8500,2023-01-01
Brazil,60000,1200,50000,8800,2023-01-01
France,40000,800,35000,4200,2023-01-01
Germany,35000,600,30000,4400,2023-01-01
USA,105000,2100,83000,19900,2023-01-02
India,82000,1520,72000,8480,2023-01-02
Brazil,62000,1250,52000,8750,2023-01-02
France,41000,810,36000,4190,2023-01-02
Germany,36000,610,31000,4390,2023-01-02
USA,110000,2200,86000,21800,2023-01-03
India,85000,1550,75000,8450,2023-01-03
Brazil,65000,1280,54000,9720,2023-01-03
France,43000,820,37500,4680,2023-01-03
Germany,38000,620,32000,5380,2023-01-03
"""


class CovidDataAnalyzer:

    def __init__(self, data_source=None):
        self.data_source = data_source
        self.data = pd.DataFrame()

    # -------------------------------------------------
    # LOAD DATA FROM INLINE CSV
    # -------------------------------------------------
    def load_data(self):
        try:
            if self.data_source:
                self.data = pd.read_csv(io.StringIO(self.data_source))
            else:
                print("\nERROR: No data source provided.")
                return False

            print("\n" + "=" * 60)
            print("CSV DATA LOADED SUCCESSFULLY")
            print("=" * 60)

            print("Rows:", self.data.shape[0])
            print("Columns:", self.data.shape[1])

            return True

        except Exception as e:
            print("\nERROR loading data:", e)
            return False

    # -------------------------------------------------
    # CHECK REQUIRED COLUMNS
    # -------------------------------------------------
    def check_columns(self, columns):
        missing_columns = [
            column for column in columns
            if column not in self.data.columns
        ]

        if missing_columns:
            print("\nMissing columns:")
            for column in missing_columns:
                print("-", column)

            print("\nAvailable columns:")
            print(list(self.data.columns))

            return False

        return True

    # -------------------------------------------------
    # EXPLORE DATA
    # -------------------------------------------------
    def explore_data(self):
        if self.data.empty:
            print("\nNo data available.")
            return

        print("\n" + "=" * 60)
        print("FIRST 5 RECORDS")
        print("=" * 60)
        print(self.data.head())

        print("\n" + "=" * 60)
        print("COLUMN NAMES")
        print("=" * 60)
        print(list(self.data.columns))

        print("\n" + "=" * 60)
        print("DATA INFORMATION")
        print("=" * 60)
        self.data.info()

        print("\n" + "=" * 60)
        print("STATISTICAL SUMMARY")
        print("=" * 60)
        print(self.data.describe(include="all"))

    # -------------------------------------------------
    # CLEAN DATA
    # -------------------------------------------------
    def clean_data(self):
        if self.data.empty:
            print("\nNo data available.")
            return

        print("\nMissing values before cleaning:")
        print(self.data.isnull().sum())

        # Remove duplicate rows
        duplicate_count = self.data.duplicated().sum()
        self.data.drop_duplicates(inplace=True)

        print("\nDuplicate rows removed:", duplicate_count)

        # Convert numeric columns
        numeric_columns = ["Confirmed", "Deaths", "Recovered", "Active"]
        for column in numeric_columns:
            if column in self.data.columns:
                self.data[column] = pd.to_numeric(self.data[column], errors="coerce").fillna(0)

        # Convert Date column
        if "Date" in self.data.columns:
            self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")

        print("\nData cleaning completed.")
        print("\nMissing values after cleaning:")
        print(self.data.isnull().sum())

    # -------------------------------------------------
    # TOTAL STATISTICS
    # -------------------------------------------------
    def total_statistics(self):
        required = ["Confirmed", "Deaths", "Recovered"]
        if not self.check_columns(required):
            return

        total_cases = self.data["Confirmed"].sum()
        total_deaths = self.data["Deaths"].sum()
        total_recovered = self.data["Recovered"].sum()

        if total_cases > 0:
            death_rate = (total_deaths / total_cases) * 100
            recovery_rate = (total_recovered / total_cases) * 100
        else:
            death_rate = 0
            recovery_rate = 0

        print("\n" + "=" * 60)
        print("COVID-19 TOTAL STATISTICS")
        print("=" * 60)
        print(f"Total Confirmed Cases : {total_cases:,.0f}")
        print(f"Total Deaths          : {total_deaths:,.0f}")
        print(f"Total Recovered       : {total_recovered:,.0f}")
        print(f"Death Rate            : {death_rate:.2f}%")
        print(f"Recovery Rate         : {recovery_rate:.2f}%")

    # -------------------------------------------------
    # COUNTRY ANALYSIS
    # -------------------------------------------------
    def country_analysis(self):
        required = ["Country", "Confirmed", "Deaths", "Recovered"]
        if not self.check_columns(required):
            return None

        country_data = self.data.groupby("Country").agg(
            Confirmed=("Confirmed", "sum"),
            Deaths=("Deaths", "sum"),
            Recovered=("Recovered", "sum")
        )

        country_data["Death_Rate"] = np.where(
            country_data["Confirmed"] > 0,
            country_data["Deaths"] / country_data["Confirmed"] * 100,
            0
        )

        country_data["Recovery_Rate"] = np.where(
            country_data["Confirmed"] > 0,
            country_data["Recovered"] / country_data["Confirmed"] * 100,
            0
        )

        country_data = country_data.sort_values("Confirmed", ascending=False)

        print("\n" + "=" * 60)
        print("COUNTRY ANALYSIS")
        print("=" * 60)
        print(country_data)

        return country_data

    # -------------------------------------------------
    # TOP COUNTRIES
    # -------------------------------------------------
    def top_countries(self):
        country_data = self.country_analysis()
        if country_data is None:
            return

        print("\n" + "=" * 60)
        print("TOP COUNTRIES BY CONFIRMED CASES")
        print("=" * 60)
        print(country_data.sort_values("Confirmed", ascending=False).head(10))

        print("\n" + "=" * 60)
        print("TOP COUNTRIES BY DEATHS")
        print("=" * 60)
        print(country_data.sort_values("Deaths", ascending=False).head(10))

        print("\n" + "=" * 60)
        print("TOP COUNTRIES BY RECOVERIES")
        print("=" * 60)
        print(country_data.sort_values("Recovered", ascending=False).head(10))

    # -------------------------------------------------
    # DATE ANALYSIS
    # -------------------------------------------------
    def date_analysis(self):
        required = ["Date", "Confirmed", "Deaths", "Recovered"]
        if not self.check_columns(required):
            return None

        self.data["Date"] = pd.to_datetime(self.data["Date"], errors="coerce")

        date_data = self.data.groupby("Date").agg(
            Confirmed=("Confirmed", "sum"),
            Deaths=("Deaths", "sum"),
            Recovered=("Recovered", "sum")
        ).reset_index()

        print("\n" + "=" * 60)
        print("COVID-19 DATE ANALYSIS")
        print("=" * 60)
        print(date_data)

        return date_data

    # -------------------------------------------------
    # VISUALIZATION
    # -------------------------------------------------
    def visualize(self):
        required = ["Country", "Confirmed", "Deaths", "Recovered"]
        if not self.check_columns(required):
            return

        os.makedirs("covid_plots", exist_ok=True)
        sns.set_theme()

        # 1. TOP COUNTRIES BAR CHART
        country_data = (
            self.data
            .groupby("Country")["Confirmed"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )

        plt.figure(figsize=(10, 6))
        country_data.plot(kind="bar")
        plt.title("Top Countries by Confirmed Cases")
        plt.xlabel("Country")
        plt.ylabel("Confirmed Cases")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("covid_plots/top_countries.png", dpi=150)
        plt.show()
        plt.close()

        # 2. OVERALL STATISTICS
        totals = [
            self.data["Confirmed"].sum(),
            self.data["Deaths"].sum(),
            self.data["Recovered"].sum()
        ]
        labels = ["Confirmed", "Deaths", "Recovered"]

        plt.figure(figsize=(8, 5))
        plt.bar(labels, totals)
        plt.title("COVID-19 Overall Statistics")
        plt.xlabel("Category")
        plt.ylabel("Number")
        plt.tight_layout()
        plt.savefig("covid_plots/overall_statistics.png", dpi=150)
        plt.show()
        plt.close()

        # 3. DATE TREND
        if "Date" in self.data.columns:
            date_data = self.date_analysis()
            if date_data is not None:
                plt.figure(figsize=(12, 6))
                plt.plot(date_data["Date"], date_data["Confirmed"], label="Confirmed")
                plt.plot(date_data["Date"], date_data["Deaths"], label="Deaths")
                plt.plot(date_data["Date"], date_data["Recovered"], label="Recovered")
                plt.title("COVID-19 Trend Over Time")
                plt.xlabel("Date")
                plt.ylabel("Cases")
                plt.legend()
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.savefig("covid_plots/covid_time_trend.png", dpi=150)
                plt.show()
                plt.close()

        # 4. CONFIRMED VS DEATHS
        plt.figure(figsize=(9, 6))
        sns.scatterplot(
            data=self.data,
            x="Confirmed",
            y="Deaths",
            hue="Country" if "Country" in self.data.columns else None
        )
        plt.title("Confirmed Cases vs Deaths")
        plt.xlabel("Confirmed Cases")
        plt.ylabel("Deaths")
        plt.tight_layout()
        plt.savefig("covid_plots/confirmed_vs_deaths.png", dpi=150)
        plt.show()
        plt.close()

        # 5. CORRELATION HEATMAP
        numeric_data = self.data.select_dtypes(include=np.number)
        if numeric_data.shape[1] >= 2:
            plt.figure(figsize=(8, 6))
            sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f")
            plt.title("COVID-19 Correlation Heatmap")
            plt.tight_layout()
            plt.savefig("covid_plots/correlation_heatmap.png", dpi=150)
            plt.show()
            plt.close()

        print("\nAll visualizations saved in 'covid_plots' folder.")

    # -------------------------------------------------
    # COMPLETE REPORT
    # -------------------------------------------------
    def generate_report(self):
        print("\n" + "=" * 70)
        print("         COVID-19 DATA ANALYSIS REPORT")
        print("=" * 70)
        self.total_statistics()
        self.top_countries()
        print("\n" + "=" * 70)
        print("REPORT COMPLETED")
        print("=" * 70)


def show_menu():
    print("""
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
""")


def main():
    print("=" * 60)
    print("       COVID-19 DATA ANALYSIS PROJECT")
    print("=" * 60)

    # Initialize analyzer with built-in embedded CSV string
    analyzer = CovidDataAnalyzer(SAMPLE_CSV_DATA)

    if not analyzer.load_data():
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            analyzer.explore_data()
        elif choice == "2":
            analyzer.clean_data()
        elif choice == "3":
            analyzer.total_statistics()
        elif choice == "4":
            analyzer.country_analysis()
        elif choice == "5":
            analyzer.top_countries()
        elif choice == "6":
            analyzer.date_analysis()
        elif choice == "7":
            analyzer.visualize()
        elif choice == "8":
            analyzer.generate_report()
        elif choice == "0":
            print("\nThank you for using COVID-19 Data Analyzer!")
            break
        else:
            print("\nInvalid choice. Please enter 0 to 8.")


if __name__ == "__main__":
    main()