# Transport Validation & Trip Reconstruction Analysis

This repository contains a data analysis pipeline for public transport systems, focused on validation processing and trip reconstruction using anonymized transactional data.

The project represents a clean, reproducible, and analytical version of a real-world ticketing and access-control workflow used in an urban cable transport system.  
All data has been fully anonymized and the repository is intended exclusively for analytical, academic, and demonstration purposes.

## Project Objectives

The main goals of this project are to:

- Clean and normalize raw validation records
- Anonymize sensitive identifiers
- Reconstruct complete and incomplete trips from time-ordered validation events
- Produce datasets ready for exploratory analysis, reporting, or modeling

This repository does not contain operational scripts or live system integrations.


## Notebooks Overview

### 01_validation_cleaning.ipynb

Validation cleaning and normalization.

This notebook performs:

- Reading the anonymized dataset
- Building a unified DateTime column
- Filtering valid transactions
- Normalizing station and equipment names
- Standardizing transaction types
- Exporting a clean validation dataset

Output:

- `outputs/validations_clean.csv`

### 02_trip_reconstruction.ipynb

Trip reconstruction logic.

Using the cleaned dataset, this notebook:

- Orders validations chronologically per card
- Detects ENTRY → EXIT sequences
- Identifies complete trips
- Identifies incomplete trips (missing exit)
- Handles multi-validation edge cases
- Supports multiple trips per card per day
- Generates consolidated Excel reports

Output:

- `outputs/viajes_generados.xlsx`

## Dataset Description

### validations_anon.csv

An anonymized CSV file containing only analysis-relevant fields, such as:

- Date and time
- Station name
- Transaction type
- User profile
- Equipment model
- Anonymized card identifier (SupportId)

No personal data, real card numbers, or operational identifiers are included.

## Technical Requirements

- Python 3.9+
- Jupyter Notebook

Required libraries:

- pandas
- numpy
- openpyxl


## How to Run

- Clone the repository
- Launch Jupyter Notebook
- Execute the notebooks in order:
01_validation_cleaning.ipynb
   02_trip_reconstruction.ipynb


All output files will be automatically generated in the `outputs/` directory.

## Scope and Limitations

- This is not a production system
- No live data ingestion or system connections are included
- No credentials, endpoints, or automation scripts are present
- Trip logic is analytical and can be adapted to other transport systems

## Use Cases

- Passenger flow and mobility analysis
- Station and time-based demand studies
- Foundations for fraud detection modeling
- Public transport ETL pipeline examples
- Data analytics portfolio demonstration

## Author

Diego Everaldo Fernández Villamar  
Data Analyst | Transport Systems & Fare Collection  
Guayaquil, Ecuador

## License

This project is published for educational and demonstration purposes only.  
The data provided does not represent real operational information.





