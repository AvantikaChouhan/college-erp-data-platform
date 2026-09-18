# Azure ADLS Gen2 Setup

## Storage Account
- Name: collegeerpdata2026
- Region: East Asia
- Storage: ADLS Gen2
- Performance: Standard
- Replication: LRS
- Hierarchical Namespace: Enabled

## Containers
- raw
- processed

## Data
The raw container contains the College ERP CSV datasets.

## Data Flow

Python CSV
→ ADLS Gen2 Raw
→ Azure Data Factory
→ ADLS Gen2 Processed