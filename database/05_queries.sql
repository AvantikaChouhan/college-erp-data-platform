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


USE college_erp;

-- ==========================================
-- WHERE Clause
-- ==========================================

-- 1. Show only IT department students
SELECT *
FROM students
WHERE department = 'IT';

-- 2. Show only Semester 6 students
SELECT *
FROM students
WHERE semester = 6;

-- 3. Show only students whose grade is A
SELECT *
FROM students
WHERE grade = 'A';

-- 4. Show only Assistant Professors
SELECT *
FROM faculty
WHERE position = 'Assistant Professor';

-- 5. Show only students whose father name is Rajesh Kumar
SELECT *
FROM students
WHERE father_name = 'Rajesh Kumar';

-- ==========================================
-- Comparison Operators
-- ==========================================

-- Semester greater than 4
SELECT *
FROM students
WHERE semester > 4;

-- Grade is not C
SELECT *
FROM students
WHERE grade != 'C';

-- Subjects with credits greater than 3
SELECT *
FROM subjects
WHERE credits > 3;

-- Placement package greater than 10 LPA
SELECT *
FROM placements
WHERE package_lpa > 10;

-- Students having pending fees
SELECT *
FROM fees
WHERE pending_amount > 0;

-- ==========================================
-- AND Operator
-- ==========================================
-- IT department students in semester 6
SELECT *
FROM students
WHERE department = 'IT'
AND semester = 6;

-- Placed students with package greater than 8 LPA
SELECT *
FROM placements
WHERE placement_status = 'Placed'
AND package_lpa > 8;