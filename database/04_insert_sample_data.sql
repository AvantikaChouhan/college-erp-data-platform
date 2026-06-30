-- ==========================================
-- File: 04_insert_sample_data.sql
-- Project: College ERP Data Platform
-- Purpose: Insert sample data for testing
-- ==========================================


-- ==========================================
-- Insert Sample Departments
-- ==========================================
INSERT INTO departments (
    department_name,
    department_code,
    department_block,
    hod_id
)
VALUES
('Computer Science', 'CSE', 'A Block', NULL),
('Information Technology', 'IT', 'A Block', NULL),
('Artificial Intelligence', 'AI', 'B Block', NULL),
('Mechanical Engineering', 'ME', 'C Block', NULL),
('Civil Engineering', 'CE', 'D Block', NULL);


-- ==========================================
-- Insert Sample Faculty
-- ==========================================
INSERT INTO faculty (
    faculty_name,
    contact_number,
    email,
    department_id,
    salary,
    position,
    dob,
    gender,
    address
)
VALUES
('Rajesh Sharma', '9876543210', 'rajesh.sharma@college.edu', 1, 85000.00, 'Professor', '1980-05-12', 'Male', 'Jaipur'),
('Priya Verma', '9876543211', 'priya.verma@college.edu', 2, 72000.00, 'Assistant Professor', '1988-09-21', 'Female', 'Delhi'),
('Amit Singh', '9876543212', 'amit.singh@college.edu', 3, 68000.00, 'Associate Professor', '1985-01-15', 'Male', 'Kota'),
('Neha Gupta', '9876543213', 'neha.gupta@college.edu', 4, 70000.00, 'Assistant Professor', '1990-07-08', 'Female', 'Ajmer'),
('Vikas Mehta', '9876543214', 'vikas.mehta@college.edu', 5, 90000.00, 'Professor', '1978-11-30', 'Male', 'Udaipur');


-- ==========================================
-- Insert Sample Students
-- ==========================================
INSERT INTO students (
    student_name,
    student_contact,
    student_email,
    roll_no,
    semester,
    department_id,
    grade,
    father_name
)
VALUES
('Aarav Sharma', '9876500001', 'aarav.sharma@student.edu', 'CSE24001', 1, 1, 'A', 'Ramesh Sharma'),
('Ananya Verma', '9876500002', 'ananya.verma@student.edu', 'IT24001', 1, 2, 'A+', 'Suresh Verma'),
('Rohan Singh', '9876500003', 'rohan.singh@student.edu', 'AI24001', 2, 3, 'B+', 'Mahesh Singh'),
('Priya Meena', '9876500004', 'priya.meena@student.edu', 'ME24001', 2, 4, 'A', 'Rajesh Meena'),
('Karan Yadav', '9876500005', 'karan.yadav@student.edu', 'CE24001', 3, 5, 'B', 'Mohan Yadav'),
('Sneha Gupta', '9876500006', 'sneha.gupta@student.edu', 'CSE24002', 3, 1, 'A+', 'Anil Gupta'),
('Aditya Jain', '9876500007', 'aditya.jain@student.edu', 'IT24002', 4, 2, 'A', 'Sunil Jain'),
('Khushi Patel', '9876500008', 'khushi.patel@student.edu', 'AI24002', 4, 3, 'B+', 'Dinesh Patel'),
('Yash Agarwal', '9876500009', 'yash.agarwal@student.edu', 'ME24002', 5, 4, 'A', 'Rakesh Agarwal'),
('Muskan Choudhary', '9876500010', 'muskan.choudhary@student.edu', 'CE24002', 5, 5, 'A+', 'Vijay Choudhary');