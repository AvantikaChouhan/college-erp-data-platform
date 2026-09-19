# College ERP Analytics Platform — Project Documentation

## 1. Project Overview

The College ERP Analytics Platform is an end-to-end Data Engineering and Analytics project designed to simulate and analyze academic and administrative data of a college.

The project generates realistic College ERP datasets using Python, stores relational data in MySQL, moves data through Azure Data Lake Storage Gen2 and Azure Data Factory, performs data transformation and analytical processing using PySpark and Databricks Free Edition, stores the final analytical dataset as a Delta table, and presents the analytical insights through an interactive Streamlit dashboard.

The project demonstrates a complete data engineering workflow from data generation and storage to transformation, analytics and visualization.

---

## 2. Project Objectives

The main objectives of the project are:

- Generate realistic College ERP datasets.
- Store structured ERP data in a relational MySQL database.
- Design relationships between academic and administrative datasets.
- Build a cloud-based data lake using Azure ADLS Gen2.
- Move raw data to a processed layer using Azure Data Factory.
- Perform data transformation using PySpark.
- Create a unified student-level analytical dataset.
- Perform analytical processing using Databricks Free Edition.
- Store analytical data using Delta Lake.
- Generate business and academic insights.
- Build an interactive Streamlit dashboard for data exploration.
- Maintain the complete project using Git and GitHub.

---

## 3. Project Architecture

```text
Python Data Generation
        ↓
CSV Datasets
        ↓
MySQL Database
        ↓
Azure Data Lake Storage Gen2
        ↓
Azure Data Factory
        ↓
Processed Data
        ↓
Databricks Free Edition
        ↓
PySpark / SQL
        ↓
Delta Lake
        ↓
Analytical Datasets
        ↓
Streamlit Dashboard
```

---

## 4. End-to-End Data Flow

The complete project workflow is:

```text
Generate College ERP Data
        ↓
Store CSV Files
        ↓
Load Data into MySQL
        ↓
Upload Raw Data to ADLS Gen2
        ↓
Azure Data Factory Copy Pipeline
        ↓
Processed Data in ADLS
        ↓
Load Analytical Data into Databricks
        ↓
PySpark Transformations
        ↓
Create Analytical Dataset
        ↓
Create Delta Table
        ↓
Generate Analytical Insights
        ↓
Export Analytical Outputs
        ↓
Streamlit Dashboard
```

---

# 5. Technology Stack

## Programming and Data Processing

- Python
- Pandas
- PySpark
- SQL

## Database

- MySQL

## Cloud

- Azure Data Lake Storage Gen2
- Azure Data Factory

## Big Data and Analytics

- Databricks Free Edition
- Apache Spark
- Delta Lake

## Visualization

- Streamlit
- Plotly

## Version Control

- Git
- GitHub

---

# 6. Dataset Overview

The project contains seven main College ERP datasets.

## 6.1 Students

The student dataset contains information about students such as:

- Roll number
- Student name
- Department
- Semester

Total records:

```text
500 students
```

Departments:

```text
AI
CE
CSE
IT
ME
```

Department-wise student count:

| Department | Students |
|---|---:|
| AI | 97 |
| CE | 81 |
| CSE | 106 |
| IT | 108 |
| ME | 108 |
| **Total** | **500** |

---

## 6.2 Faculty

The faculty dataset contains information about college faculty members.

Total faculty:

```text
100
```

Designation distribution:

| Designation | Count |
|---|---:|
| HOD | 5 |
| Professor | 10 |
| Associate Professor | 20 |
| Assistant Professor | 65 |
| **Total** | **100** |

---

## 6.3 Subjects

The subject dataset contains subject information used by attendance and results data.

Total subjects:

```text
200
```

The `subject_code` is used to connect subjects with attendance and result records.

---

## 6.4 Attendance

The attendance dataset contains student attendance records by subject.

Total attendance records:

```text
2500
```

The dataset is used for:

- Average attendance analysis
- Department attendance analysis
- Attendance risk identification
- Attendance and academic performance analysis

---

## 6.5 Results

The results dataset contains student academic performance by subject.

Total result records:

```text
2500
```

The dataset is used for:

- Average marks analysis
- Department performance
- Low marks analysis
- Student performance segmentation

---

## 6.6 Fees

The fees dataset contains student fee information.

Total fee records:

```text
500
```

The dataset contains:

- Total fee
- Amount paid
- Pending amount
- Payment status

---

## 6.7 Placements

The placement dataset contains student placement information.

Total placement records:

```text
64
```

Placement information includes:

- Placement status
- Company
- Package in LPA

Unplaced students are represented using:

```text
Company = N/A
Package = 0.00
```

---

# 7. MySQL Database

The generated ERP datasets are stored in a MySQL database.

Database name:

```text
college_erp
```

Tables:

```text
students
faculty
subjects
attendance
results
fees
placements
```

## Database Relationships

The main relationships are:

```text
students.roll_no
        ↓
attendance.roll_no

students.roll_no
        ↓
results.roll_no

students.roll_no
        ↓
fees.roll_no

students.roll_no
        ↓
placements.roll_no

subjects.subject_code
        ↓
attendance.subject_code

subjects.subject_code
        ↓
results.subject_code
```

This relational design allows student-level information to be combined with attendance, academic, fee and placement data.

---

# 8. Azure Data Lake Storage Gen2

Azure Data Lake Storage Gen2 is used as the cloud data storage layer.

Storage Account:

```text
collegeerpdata2026
```

Region:

```text
East Asia
```

Storage configuration:

```text
StorageV2
Standard
LRS
Hierarchical Namespace Enabled
Hot Access Tier
```

Containers:

```text
raw
processed
```

## Raw Layer

The `raw` container contains the source CSV datasets.

```text
raw/
├── attendance.csv
├── faculty.csv
├── fees.csv
├── placements.csv
├── results.csv
├── students.csv
└── subjects.csv
```

## Processed Layer

The `processed` container contains the CSV files after Azure Data Factory processing.

---

# 9. Azure Data Factory

Azure Data Factory is used for data movement between the raw and processed layers.

Data Factory:

```text
collegeerp-adf-2026
```

Pipeline:

```text
PL_Copy_Raw_Data
```

## Pipeline Flow

```text
ADLS Gen2 Raw
      ↓
Copy Data Activity
      ↓
ADLS Gen2 Processed
```

The pipeline uses:

- ADLS Gen2 source
- Delimited Text dataset
- CSV files
- Wildcard path `*.csv`
- Processed container as sink

The pipeline was validated, published and executed successfully.

All seven source CSV files were copied to the processed layer.

---

# 10. PySpark Processing

PySpark is used for data transformation and analytical dataset creation.

The PySpark scripts are organized as follows:

```text
pyspark/
├── 01_read_students.py
├── 02_transform_students.py
├── 03_transform_attendance.py
├── 04_transform_results.py
├── 05_transform_fees.py
├── 06_transform_placements.py
├── 07_create_analytical_dataset.py
├── 08_write_analytical_dataset.py
└── CollegeERP_Analytical_Dataset.ipynb
```

---

## 10.1 Read Student Data

The first PySpark script reads the student CSV dataset.

Output:

```text
500 student records
```

The schema and basic student information are validated.

---

## 10.2 Student Transformation

Student data is transformed to select required fields and perform department-level analysis.

Department counts:

| Department | Students |
|---|---:|
| ME | 108 |
| IT | 108 |
| CSE | 106 |
| AI | 97 |
| CE | 81 |

---

## 10.3 Attendance Transformation

Attendance data is aggregated at the student and department levels.

Key result:

```text
Students below 75% average attendance: 361
```

Department average attendance:

| Department | Average Attendance |
|---|---:|
| IT | 70.85% |
| ME | 70.42% |
| AI | 70.29% |
| CSE | 69.56% |
| CE | 69.27% |

---

## 10.4 Results Transformation

Result data is aggregated to calculate average marks.

Department average marks:

| Department | Average Marks |
|---|---:|
| CE | 60.24 |
| IT | 59.71 |
| ME | 57.40 |
| AI | 57.31 |
| CSE | 53.81 |

Result records with marks below 50:

```text
1050 subject-level result records
```

---

## 10.5 Fee Transformation

Fee data is analyzed to calculate:

- Total fees
- Amount paid
- Pending fees
- Payment status
- Department-level collection

Total fee records:

```text
500
```

Students with pending fees:

```text
159
```

Department-wise amount paid:

| Department | Amount Paid |
|---|---:|
| ME | 4,812,422 |
| IT | 4,349,602 |
| CSE | 4,278,232 |
| AI | 3,649,130 |
| CE | 3,398,729 |

---

## 10.6 Placement Transformation

Placement data is analyzed to identify placed and unplaced students.

Total placement records:

```text
64
```

Placed students:

```text
27
```

Unplaced students:

```text
37
```

Department-level placement information:

| Department | Placed Students | Average Package |
|---|---:|---:|
| ME | 9 | 8.15 LPA |
| IT | 8 | 10.27 LPA |
| CE | 5 | 7.70 LPA |
| AI | 3 | 8.94 LPA |
| CSE | 2 | 11.78 LPA |

---

# 11. Analytical Dataset

The project combines multiple ERP datasets into one student-level analytical dataset.

The final dataset contains:

```text
500 records
14 columns
```

Main columns:

```text
roll_no
student_name
department
semester
avg_attendance
avg_marks
total_subjects
total_fee
amount_paid
pending_amount
payment_status
company
package_lpa
placement_status
```

This dataset acts as the main analytical layer for Databricks and the dashboard.

---

# 12. Databricks Free Edition

Databricks Free Edition is used for Spark-based analytical processing.

The analytical CSV is uploaded into a Unity Catalog managed volume.

Volume:

```text
collegeerp_data
```

The dataset is loaded using Spark:

```python
df = spark.read.csv(
    "/Volumes/workspace/default/collegeerp_data/student_analytics.csv",
    header=True,
    inferSchema=True
)
```

The dataset was validated with:

```text
500 records
14 columns
```

---

# 13. Delta Lake

The analytical dataset is stored as a Delta table.

Main Delta table:

```text
collegeerp_student_analytics
```

The table is created using:

```python
df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("collegeerp_student_analytics")
```

The Delta table is then queried using Spark SQL.

Example:

```sql
SELECT *
FROM collegeerp_student_analytics
LIMIT 10;
```

---

# 14. KPI Analysis

The project generates a consolidated KPI dataset containing the major college-level metrics.

## Overall KPIs

| KPI | Value |
|---|---:|
| Total Students | 500 |
| Average Attendance | 70.12% |
| Average Marks | 57.58 |
| Total Pending Fees | 17,011,885 |
| Total Fees Collected | 20,488,115 |
| Students Below 75% Attendance | 361 |
| Students Below 50 Marks | 210 |
| Placed Students | 27 |
| Placement Rate | 5.40% |
| Average Package | 9.05 LPA |
| Highest Package | 14.48 LPA |

These KPIs are calculated from the generated analytical dataset.

---

# 15. Attendance Insights

The attendance analysis divides students into attendance bands.

| Attendance Band | Students | Average Marks |
|---|---:|---:|
| Below 60% | 47 | 56.23 |
| 60% - 74% | 314 | 56.47 |
| 75% - 84% | 126 | 60.65 |
| 85%+ | 13 | 59.62 |

The analysis shows differences in average marks across attendance bands.

These results are descriptive observations from the generated sample dataset and do not establish a causal relationship between attendance and academic performance.

---

# 16. Department 360 Analysis

The project creates a department-level 360-degree analytical view combining:

- Student count
- Attendance
- Academic performance
- Fees
- Placement
- Package information

This enables department-level comparison across multiple ERP dimensions.

The department analysis combines data from:

```text
Students
Attendance
Results
Fees
Placements
```

---

# 17. Student Segmentation

The project creates student-level analytical segments using academic, attendance, fee and placement information.

The student segmentation supports identification of:

- Academic performance groups
- Attendance risk
- Fee-related risk
- Placement status
- Overall student profiles

This provides a unified view of individual student records.

---

# 18. Fee and Academic Insights

The project combines fee and academic information to analyze relationships between:

- Payment status
- Pending fees
- Attendance
- Academic performance

The resulting dataset:

```text
fee_academic_insights.csv
```

is used for analytical exploration and dashboard visualization.

---

# 19. Placement Insights

The placement analysis includes:

- Placement status
- Placement rate
- Department placement
- Average package
- Highest package
- Company-wise placement
- Top packages

Main placement KPIs:

```text
Placed Students: 27
Unplaced Students: 37
Placement Rate: 5.40%
Average Package: 9.05 LPA
Highest Package: 14.48 LPA
```

---

# 20. Company Insights

The project generates company-level placement analytics.

Output:

```text
company_insights.csv
```

The analysis supports:

- Recruiter-level student counts
- Placement distribution
- Company-level package analysis

---

# 21. Semester Insights

Semester-level analytical data is generated to analyze student performance across semesters.

Output:

```text
semester_insights.csv
```

The dataset supports:

- Student distribution by semester
- Academic performance analysis
- Attendance analysis
- Semester-level comparisons

---

# 22. Top Package Analysis

The project generates:

```text
top_packages.csv
```

This dataset is used to analyze the highest placement packages in the generated sample data.

The highest package recorded in the current analytical dataset is:

```text
14.48 LPA
```

---

# 23. Analytical Output Files

The project generates the following analytical outputs:

```text
attendance_performance.csv
company_insights.csv
department_360.csv
fee_academic_insights.csv
insight_df.csv
placement_insights.csv
semester_insights.csv
student_segments.csv
top_packages.csv
student_analytics_powerbi.csv
```

These datasets are used as analytical outputs and dashboard data sources.

---

# 24. Streamlit Dashboard

The final analytical results are presented through a Streamlit dashboard.

Dashboard application:

```text
dashboard/app.py
```

Dashboard requirements:

```text
streamlit
pandas
plotly
```

## Dashboard Sections

### 24.1 Overview

Provides:

- Overall KPIs
- Department snapshot
- Student segments
- Risk segmentation

### 24.2 Academics & Attendance

Provides:

- Department filter
- Academic performance
- Attendance distribution
- Semester trends
- Attendance analysis

### 24.3 Fees & Risk

Provides:

- Payment status
- Pending fees
- Department fee analysis
- Risk categories

### 24.4 Placements

Provides:

- Placement rate
- Placed vs unplaced students
- Top recruiters
- Top packages
- Department placement analysis

### 24.5 Departments & Students

Provides:

- Department comparison
- Student explorer
- Student-level analytical information
- Search and filtering

---

# 25. Running the Streamlit Dashboard

Navigate to the dashboard directory:

```bash
cd dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The dashboard runs locally at:

```text
http://localhost:8501
```

---

# 26. Complete Repository Structure

```text
college-erp-data-platform/
│
├── azure/
│   ├── README.md
│   ├── adls_setup.md
│   └── adf_pipeline.md
│
├── dashboard/
│   ├── app.py
│   ├── requirements.txt
│   └── data/
│       ├── insight_df.csv
│       ├── top_packages.csv
│       ├── company_insights.csv
│       ├── semester_insights.csv
│       ├── fee_academic_insights.csv
│       ├── placement_insights.csv
│       ├── attendance_performance.csv
│       ├── student_segments.csv
│       ├── department_360.csv
│       └── student_analytics_powerbi.csv
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
├── docs/
│   └── project_documentation.md
│
├── README.md
└── requirements.txt
```

---

# 27. Project Status

The following components have been completed:

- Python data generation
- College ERP CSV datasets
- MySQL relational database
- SQL analysis
- Azure ADLS Gen2 setup
- Azure Data Factory setup
- Azure Data Factory pipeline
- Raw to Processed data movement
- PySpark transformations
- Analytical dataset creation
- Databricks Free Edition analytics
- Delta Lake table
- Analytical KPI generation
- Analytical insight datasets
- Streamlit analytics dashboard
- Git version control
- GitHub repository

---

# 28. Azure and Databricks Implementation Note

Azure is used for cloud storage and data movement through:

```text
Azure Data Lake Storage Gen2
Azure Data Factory
```

Databricks is used separately through Databricks Free Edition for:

```text
Spark Processing
SQL Analytics
Delta Lake
```

The Azure Data Factory pipeline successfully moves data from the ADLS Gen2 raw layer to the processed layer.

The analytical dataset is then used in Databricks Free Edition for Spark-based processing and Delta Lake analytics.

---

# 29. Project Outcome

This project demonstrates a complete data engineering and analytics workflow:

```text
Data Generation
      ↓
Data Storage
      ↓
Relational Database
      ↓
Cloud Data Lake
      ↓
Data Movement
      ↓
Data Transformation
      ↓
Big Data Analytics
      ↓
Delta Lake
      ↓
Analytical Datasets
      ↓
KPI & Insight Generation
      ↓
Interactive Dashboard
```

The project brings together Python, SQL, MySQL, Azure, PySpark, Databricks, Delta Lake and Streamlit into a single College ERP Analytics Platform.

---

# 30. Future Enhancements

Possible future improvements include:

- Automated MySQL to ADLS ingestion
- Incremental data pipelines
- Data quality validation
- Azure Key Vault integration
- CI/CD pipeline
- Automated dashboard refresh
- Advanced Spark optimization
- More analytical datasets
- Production-grade cloud orchestration
- Role-based access control
- Automated end-to-end pipeline scheduling

---

# 31. Author

**Avantika Chouhan**

GitHub:

https://github.com/AvantikaChouhan/college-erp-data-platform

---

# 32. License

This project is created for educational and portfolio purposes.