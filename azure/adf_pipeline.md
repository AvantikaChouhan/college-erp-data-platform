# Azure Data Factory Pipeline

## Factory
collegeerp-adf-2026

## Pipeline
PL_Copy_Raw_Data

## Source
ADLS Gen2
Container: raw
File type: CSV
Wildcard: *.csv

## Sink
ADLS Gen2
Container: processed

## Flow

Raw CSV files
→ ADF Copy Data Activity
→ Processed CSV files

Pipeline validation and execution completed successfully.