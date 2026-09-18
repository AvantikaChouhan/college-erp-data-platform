# College ERP Analytics Platform

## Project Overview

This project is an end-to-end College ERP Data Engineering and Analytics platform that simulates academic and administrative data of a college.

The project generates realistic college datasets, stores relational data in MySQL, performs data processing using PySpark, uses Azure services for cloud storage and data movement, and performs analytical processing in Databricks.

## Architecture

Python
↓
CSV Datasets
↓
MySQL
↓
Azure Data Lake Storage Gen2
↓
Azure Data Factory
↓
Processed Data
↓
Databricks Free Edition + PySpark
↓
Delta Table
↓
Analytical Datasets

## Tech Stack

- Python
- MySQL
- SQL
- Git
- GitHub
- Azure Data Lake Storage Gen2
- Azure Data Factory
- PySpark
- Databricks
- Delta Lake

## Datasets

The project contains the following College ERP datasets:

- Students
- Faculty
- Subjects
- Attendance
- Results
- Fees
- Placements

## Azure Data Platform

### Azure Data Lake Storage Gen2

Storage Account:

`collegeerpdata2026`

Region:

`East Asia`

Containers:

- `raw`
- `processed`

The Raw container stores the source College ERP CSV datasets.

The Processed container stores the data after the Azure Data Factory pipeline execution.

### Azure Data Factory

Data Factory:

`collegeerp-adf-2026`

Pipeline:

`PL_Copy_Raw_Data`

The pipeline copies CSV files from the ADLS Gen2 Raw container to the Processed container.

### Azure Data Flow
```text
Raw CSV Files
      ↓
ADLS Gen2 - Raw
      ↓
Azure Data Factory
      ↓
ADLS Gen2 - Processed
```text
## Repository Structure

college-erp-data-platform/
│
├── azure/
│   ├── README.md
│   ├── adls_setup.md
│   └── adf_pipeline.md
│
├── data/
│   ├── attendance.csv
│   ├── faculty.csv
│   ├── fees.csv
│   ├── placements.csv
│   ├── results.csv
│   ├── students.csv
│   ├── subjects.csv
│   └── processed/
│
├── data_generator/
│
├── database/
│
│
├── pyspark/
│   ├── 01_read_students.py
│   ├── 02_transform_students.py
│   ├── 03_transform_attendance.py
│   ├── 04_transform_results.py
│   ├── 05_transform_fees.py
│   ├── 06_transform_placements.py
│   ├── 07_create_analytical_dataset.py
│   ├── 08_write_analytical_dataset.py
│   └── CollegeERP_Analytical_Dataset.ipynb
│
│
├── docs/
│
├── README.md
└── requirements.txt