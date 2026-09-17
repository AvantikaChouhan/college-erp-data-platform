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

-- ==========================================
-- OR Operator
-- ==========================================

-- Students from CSE or IT
SELECT *
FROM students
WHERE department = 'CSE'
OR department = 'IT';

-- Students in semester 1 or semester 8
SELECT *
FROM students
WHERE semester = 1
OR semester = 8;


-- ==========================================
-- NOT Operator
-- ==========================================

-- Students whose grade is not C
SELECT *
FROM students
WHERE NOT grade = 'C';

-- Students who are not from CSE
SELECT *
FROM students
WHERE NOT department = 'CSE';


-- ==========================================
-- ORDER BY
-- ==========================================

-- Students ordered by semester
SELECT *
FROM students
ORDER BY semester;

-- Students ordered by semester descending
SELECT *
FROM students
ORDER BY semester DESC;

-- Placements ordered by package
SELECT *
FROM placements
WHERE placement_status = 'Placed'
ORDER BY package_lpa DESC;


-- ==========================================
-- LIMIT
-- ==========================================

-- First 10 students
SELECT *
FROM students
LIMIT 10;

-- Top 5 highest packages
SELECT *
FROM placements
WHERE placement_status = 'Placed'
ORDER BY package_lpa DESC
LIMIT 5;


-- ==========================================
-- DISTINCT
-- ==========================================

-- Unique departments
SELECT DISTINCT department
FROM students;

-- Unique semesters
SELECT DISTINCT semester
FROM students;

-- Unique faculty positions
SELECT DISTINCT position
FROM faculty;


-- ==========================================
-- LIKE
-- ==========================================

-- Students whose name starts with A
SELECT *
FROM students
WHERE student_name LIKE 'A%';

-- Students whose name contains 'an'
SELECT *
FROM students
WHERE student_name LIKE '%an%';

-- Emails ending with gmail.com
SELECT *
FROM students
WHERE student_email LIKE '%gmail.com';


-- ==========================================
-- IN
-- ==========================================

-- Students from CSE, IT or ECE
SELECT *
FROM students
WHERE department IN ('CSE', 'IT', 'AI');

-- Students from semester 6 or 8
SELECT *
FROM students
WHERE semester IN (6, 8);


-- ==========================================
-- BETWEEN
-- ==========================================

-- Students from semester 4 to 8
SELECT *
FROM students
WHERE semester BETWEEN 4 AND 8;

-- Placements with package between 5 and 10 LPA
SELECT *
FROM placements
WHERE package_lpa BETWEEN 5 AND 10;


-- ==========================================
-- Aggregate Functions
-- ==========================================

-- Total students
SELECT COUNT(*) AS total_students
FROM students;

-- Average placement package
SELECT AVG(package_lpa) AS average_package
FROM placements
WHERE placement_status = 'Placed';

-- Highest package
SELECT MAX(package_lpa) AS highest_package
FROM placements
WHERE placement_status = 'Placed';

-- Lowest package
SELECT MIN(package_lpa) AS lowest_package
FROM placements
WHERE placement_status = 'Placed';

-- Total fees collected
SELECT SUM(amount_paid) AS total_amount_paid
FROM fees;

-- Total pending fees
SELECT SUM(pending_amount) AS total_pending_amount
FROM fees;


-- ==========================================
-- GROUP BY
-- ==========================================

-- Number of students in each department
SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department;

-- Number of students in each semester
SELECT semester, COUNT(*) AS student_count
FROM students
GROUP BY semester;

-- Average package by company
SELECT company, AVG(package_lpa) AS average_package
FROM placements
WHERE placement_status = 'Placed'
GROUP BY company;


-- ==========================================
-- HAVING
-- ==========================================

-- Departments having more than 50 students
SELECT department, COUNT(*) AS student_count
FROM students
GROUP BY department
HAVING COUNT(*) > 50;

-- Companies having average package greater than 7 LPA
SELECT company, AVG(package_lpa) AS average_package
FROM placements
WHERE placement_status = 'Placed'
GROUP BY company
HAVING AVG(package_lpa) > 7;


-- ==========================================
-- JOINS
-- ==========================================

-- Student name with their results
SELECT
    s.roll_no,
    s.student_name,
    r.subject_code,
    r.marks,
    r.grade
FROM students s
JOIN results r
    ON s.roll_no = r.roll_no;


-- Student name with fee information
SELECT
    s.roll_no,
    s.student_name,
    f.total_fee,
    f.amount_paid,
    f.pending_amount,
    f.payment_status
FROM students s
JOIN fees f
    ON s.roll_no = f.roll_no;


-- Student name with placement information
SELECT
    s.roll_no,
    s.student_name,
    p.company,
    p.package_lpa,
    p.placement_status
FROM students s
JOIN placements p
    ON s.roll_no = p.roll_no;


-- Student + Subject + Result
SELECT
    s.student_name,
    sub.subject_name,
    r.marks,
    r.grade
FROM students s
JOIN results r
    ON s.roll_no = r.roll_no
JOIN subjects sub
    ON r.subject_code = sub.subject_code;

-- ==========================================
-- Data Validation
-- ==========================================

SELECT 'students' AS table_name, COUNT(*) AS record_count
FROM students

UNION ALL

SELECT 'faculty', COUNT(*)
FROM faculty

UNION ALL

SELECT 'subjects', COUNT(*)
FROM subjects

UNION ALL

SELECT 'attendance', COUNT(*)
FROM attendance

UNION ALL

SELECT 'results', COUNT(*)
FROM results

UNION ALL

SELECT 'fees', COUNT(*)
FROM fees

UNION ALL

SELECT 'placements', COUNT(*)
FROM placements;

-- ==========================================
-- End of SQL Practice
-- ==========================================