-- ==========================================
-- File: 03_constraints.sql
-- Project: College ERP Data Platform
-- Purpose: Add Foreign Key Constraints
-- ==========================================


-- ==========================================
-- Students → Departments
-- Ensures every student belongs to a valid department.
-- ==========================================
ALTER TABLE students
ADD CONSTRAINT fk_students_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id);


-- ==========================================
-- Faculty → Departments
-- Ensures every faculty member belongs to a valid department.
-- ==========================================
ALTER TABLE faculty
ADD CONSTRAINT fk_faculty_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id);


-- ==========================================
-- Subjects → Departments
-- Ensures every subject belongs to a valid department.
-- ==========================================
ALTER TABLE subjects
ADD CONSTRAINT fk_subjects_department
FOREIGN KEY (department_id)
REFERENCES departments(department_id);


-- ==========================================
-- Subjects → Faculty
-- Links each subject to the faculty member teaching it.
-- ==========================================
ALTER TABLE subjects
ADD CONSTRAINT fk_subjects_faculty
FOREIGN KEY (faculty_id)
REFERENCES faculty(faculty_id);


-- ==========================================
-- Attendance → Students
-- Ensures attendance records belong to valid students.
-- ==========================================
ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);


-- ==========================================
-- Attendance → Faculty
-- Records which faculty member marked attendance.
-- ==========================================
ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_faculty
FOREIGN KEY (faculty_id)
REFERENCES faculty(faculty_id);


-- ==========================================
-- Results → Students
-- Links each result to a valid student.
-- ==========================================
ALTER TABLE results
ADD CONSTRAINT fk_results_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);


-- ==========================================
-- Results → Subjects
-- Links each result to a valid subject.
-- ==========================================
ALTER TABLE results
ADD CONSTRAINT fk_results_subject
FOREIGN KEY (subject_id)
REFERENCES subjects(subject_id);


-- ==========================================
-- Fees → Students
-- Ensures fee records belong to valid students.
-- ==========================================
ALTER TABLE fees
ADD CONSTRAINT fk_fees_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);


-- ==========================================
-- Placements → Students
-- Ensures placement records belong to valid students.
-- ==========================================
ALTER TABLE placements
ADD CONSTRAINT fk_placements_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);