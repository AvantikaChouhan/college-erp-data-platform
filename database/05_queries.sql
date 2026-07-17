-- ==========================================
-- File: 05_queries.sql
-- Project: College ERP Data Platform
-- Purpose: Basic SQL queries to verify data
-- ==========================================

USE college_erp;

-- ==========================================
-- View All Student Records
-- ==========================================
SELECT * FROM students;

-- ==========================================
-- View All Faculty Records
-- ==========================================
SELECT * FROM faculty;

-- ==========================================
-- View All Subject Records
-- ==========================================
SELECT * FROM subjects;

-- ==========================================
-- View All Attendance Records
-- ==========================================
SELECT * FROM attendance;

-- ==========================================
-- View All Result Records
-- ==========================================
SELECT * FROM results;

-- ==========================================
-- View All Fee Records
-- ==========================================
SELECT * FROM fees;

-- ==========================================
-- View All Placement Records
-- ==========================================
SELECT * FROM placements;

-- ==========================================
-- Basic SELECT Queries
-- ==========================================

-- View all students
SELECT * FROM students;

-- View roll number and student name
SELECT roll_no, student_name
FROM students;

-- View student name and department
SELECT student_name, department
FROM students;

-- View all faculty
SELECT * FROM faculty;

-- View all subjects
SELECT * FROM subjects;

