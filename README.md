# Clinical Trials Pipeline

A Python data pipeline that fetches live clinical trial data from
the [ClinicalTrials.gov API](https://clinicaltrials.gov/data-api/api), stores it in a SQLite database, and displays it
in an interactive Streamlit dashboard.

## What it does

- Pulls real-time trial data for a given medical condition
- Cleans and structures the data using pandas
- Saves it into a SQLite database
- Displays it in a dashboard with filtering, sorting, and charts

## Tech stack

- Python
- Requests (API calls)
- Pandas (data processing)
- SQLite (database)
- Streamlit (dashboard)

## How to run it

1. Clone this repo
2. Install dependencies: `pip install requests pandas streamlit`
3. Run the pipeline: `python main.py`
4. Launch the dashboard: `streamlit run dashboard.py`

## Why I built this

As someone transitioning from a biology background into computer science, I wanted a project that combined both —
showing I can work with real domain data (clinical trials) using a full data pipeline, from raw API to an interactive
dashboard.