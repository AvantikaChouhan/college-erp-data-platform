-- ==========================================
-- File: 04_import_csv_data.sql
-- Project: College ERP Data Platform
-- Purpose: Import generated CSV files into MySQL
-- ==========================================

-- Import Order

-- 1. students.csv
-- 2. faculty.csv
-- 3. subjects.csv
-- 4. attendance.csv
-- 5. results.csv
-- 6. fees.csv
-- 7. placements.csv

-- Verification Queries

SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM faculty;
SELECT COUNT(*) FROM subjects;
SELECT COUNT(*) FROM attendance;
SELECT COUNT(*) FROM results;
SELECT COUNT(*) FROM fees;
SELECT COUNT(*) FROM placements;