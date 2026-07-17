-- ==========================================
-- File: 02_create_tables.sql
-- Project: College ERP Data Platform
-- Purpose: Create all database tables
-- ==========================================

USE college_erp;

-- ==========================================
-- Students Table
-- ==========================================

CREATE TABLE students (
    roll_no VARCHAR(20) PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    student_contact VARCHAR(15) NOT NULL,
    student_email VARCHAR(100) NOT NULL,
    semester INT NOT NULL,
    department VARCHAR(10) NOT NULL,
    department_id INT NOT NULL,
    grade VARCHAR(5) NOT NULL,
    father_name VARCHAR(100) NOT NULL
);

-- ==========================================
-- Faculty Table
-- ==========================================

CREATE TABLE faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_name VARCHAR(100) NOT NULL,
    faculty_contact VARCHAR(15) NOT NULL,
    faculty_email VARCHAR(100) NOT NULL,
    department VARCHAR(10) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    position VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- ==========================================
-- Subjects Table
-- ==========================================

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    subject_code VARCHAR(20) NOT NULL UNIQUE,
    department VARCHAR(10) NOT NULL,
    department_id INT NOT NULL,
    semester INT NOT NULL,
    credits INT NOT NULL
);

-- ==========================================
-- Attendance Table
-- ==========================================

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY,
    roll_no VARCHAR(20) NOT NULL,
    subject_code VARCHAR(20) NOT NULL,
    attendance_percentage DECIMAL(5,2) NOT NULL
);

-- ==========================================
-- Results Table
-- ==========================================

CREATE TABLE results (
    result_id INT PRIMARY KEY,
    roll_no VARCHAR(20) NOT NULL,
    subject_code VARCHAR(20) NOT NULL,
    marks DECIMAL(5,2) NOT NULL,
    grade VARCHAR(5) NOT NULL,
    status VARCHAR(10) NOT NULL
);

-- ==========================================
-- Fees Table
-- ==========================================

CREATE TABLE fees (
    fee_id INT PRIMARY KEY,
    roll_no VARCHAR(20) NOT NULL,
    semester INT NOT NULL,
    total_fee DECIMAL(10,2) NOT NULL,
    amount_paid DECIMAL(10,2) NOT NULL,
    pending_amount DECIMAL(10,2) NOT NULL,
    payment_status VARCHAR(20) NOT NULL
);

-- ==========================================
-- Placements Table
-- ==========================================

CREATE TABLE placements (
    placement_id INT PRIMARY KEY,
    roll_no VARCHAR(20) NOT NULL,
    company VARCHAR(100),
    package_lpa DECIMAL(5,2),
    placement_status VARCHAR(20) NOT NULL
);