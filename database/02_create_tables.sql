-- ==========================================
-- File: 02_create_tables.sql
-- Project: College ERP Data Platform
-- Purpose: Create all database tables
-- ==========================================

-- Create Departments Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL,
    department_code VARCHAR(10) NOT NULL,
    department_block VARCHAR(50) NOT NULL,
    hod_id INT
);

-- Create Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    student_contact VARCHAR(15) NOT NULL,
    student_email VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20) NOT NULL,
    semester INT NOT NULL,
    department_id INT NOT NULL,
    grade VARCHAR(5) NOT NULL,
    father_name VARCHAR(50) NOT NULL
);

-- Create Faculty Table
CREATE TABLE faculty (
    faculty_id INT AUTO_INCREMENT PRIMARY KEY,
    faculty_name VARCHAR(50) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    email VARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    position VARCHAR(50) NOT NULL,
    dob DATE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    address VARCHAR(255) NOT NULL
);

-- Create Subjects Table
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL,
    semester INT NOT NULL,
    credits INT NOT NULL,
    subject_type VARCHAR(20) NOT NULL,
    department_id INT NOT NULL,
    faculty_id INT
);

-- Create Attendance Table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    faculty_id INT NOT NULL,
    attendance_date DATE NOT NULL,
    status VARCHAR(10) NOT NULL
);

-- Create Results Table
CREATE TABLE results (
    result_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    semester INT NOT NULL,
    exam_type VARCHAR(20) NOT NULL,
    marks DECIMAL(5,2) NOT NULL,
    grade VARCHAR(5) NOT NULL
);

-- Create Fees Table
CREATE TABLE fees (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    semester INT NOT NULL,
    total_fee DECIMAL(10,2) NOT NULL,
    paid_fee DECIMAL(10,2) NOT NULL,
    payment_date DATE,
    payment_status VARCHAR(20) NOT NULL
);

-- Create Placements Table
CREATE TABLE placements (
    placement_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    job_role VARCHAR(100) NOT NULL,
    package_lpa DECIMAL(5,2) NOT NULL,
    placement_date DATE NOT NULL,
    joining_date DATE,
    placement_status VARCHAR(20) NOT NULL
);