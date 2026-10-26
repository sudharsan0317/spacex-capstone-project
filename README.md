# SpaceX Falcon 9 First-Stage Landing Success Prediction

## Project Overview

This project explores historical SpaceX Falcon 9 launch data to understand landing outcomes and build baseline machine-learning models for predicting first-stage landing success.

The project demonstrates a data science workflow involving data preparation, exploratory data analysis (EDA), SQL analysis, data visualization, and predictive modeling.

**GitHub Repository:** https://github.com/sudharsan0317/spacex-capstone-project

## Objectives

- Explore SpaceX Falcon 9 launch and landing outcomes.
- Clean and prepare launch data for analysis.
- Analyze launch sites, payloads, and yearly launch trends.
- Use SQL queries to summarize launch activity and landing outcomes.
- Visualize findings through charts and a launch-site map.
- Compare baseline machine-learning models.

## Dataset

The project uses `Spacex.csv`, containing historical launch records with fields such as:

- Launch date and time
- Booster version
- Launch site
- Payload and payload mass
- Orbit and customer
- Mission outcome
- Landing outcome

The dataset contains approximately 101 records spanning 2010–2020.

## Project Workflow

1. **Data collection:** Documented workflows for obtaining launch data from the SpaceX API and public web sources.
2. **Data wrangling:** Processed dates, payload values, missing data, and categorical features.
3. **Exploratory data analysis:** Examined launch outcomes, payload mass, launch sites, and yearly trends.
4. **SQL analysis:** Queried launch counts, outcome counts, and landing-success summaries.
5. **Interactive visualization:** Included a Folium launch-site map and a Plotly Dash application.
6. **Predictive analysis:** Compared Logistic Regression and Random Forest classifiers.

## Preliminary Machine-Learning Results

The following results were obtained from one stratified train/test split. The target label was defined as `1` when `Landing_Outcome` begins with `Success`, and `0` otherwise.

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 65.4% | 70.6% | 75.0% | 72.7% |
| Random Forest | 61.5% | 66.7% | 75.0% | 70.6% |

These results are preliminary. The dataset is small, and the simplified target groups several different non-success outcomes together. Further validation and cross-validation are recommended.

## Repository Contents

| File | Description |
|---|---|
| `Data_Science_Capstone_Project_Report_REVISED.pdf` | Revised capstone report |
| `SpaceX_Capstone_Resubmission_Bundle.zip` | Supporting project bundle |
| `Spacex.csv` | Launch dataset |
| `spacex_launches.db` | SQLite database |
| `sql_queries_and_results.txt` | SQL queries and findings |
| `sql_launches_by_site.csv` | Launch counts by site |
| `sql_outcome_counts.csv` | Landing-outcome counts |
| `sql_payload_by_orbit.csv` | Payload summaries by orbit |
| `sql_success_by_year.csv` | Yearly success summaries |
| `sql_success_labels_by_site.csv` | Labeled-success summaries by site |
| `spacex_launch_sites_map.html` | Folium launch-site map |
| `spacex_dashboard.py` | Plotly Dash dashboard source |
| `dashboard_preview.png` | Dashboard preview image |

## Running the Dashboard

Python 3 is required.

1. Download or clone this repository.
2. Install the required packages:

   ```bash
   pip install dash plotly pandas
   ```

3. Ensure `spacex_dashboard.py` and `Spacex.csv` are in the same directory.
4. Run the application:

   ```bash
   python spacex_dashboard.py
   ```

5. Open the local URL displayed in the terminal.

## Opening the Map

Download `spacex_launch_sites_map.html` and open it in a web browser. An internet connection may be required for the map tiles.

**Note:** Verify the launch-site coordinates before drawing proximity conclusions.

## Limitations

- The dataset is relatively small.
- The target label simplifies distinct landing outcomes into two categories.
- Model performance is based on a single holdout split and may vary with different splits.
- The SpaceX API and web-scraping sections document collection workflows; they should not be interpreted as proof that those workflows were executed unless supporting execution evidence is available.
- The interactive dashboard should be run locally to verify its behavior.

## Conclusion

This project demonstrates an end-to-end educational data science workflow for analyzing SpaceX Falcon 9 landing outcomes. The results provide an initial comparison of launch characteristics and baseline classifiers, while highlighting the need for more data, stronger validation, and further model evaluation.
