-- ==========================================
-- File: 03_constraints.sql
-- Project: College ERP Data Platform
-- Purpose: Add Foreign Key Constraints
-- ==========================================

USE college_erp;

-- ==========================================
-- Attendance → Students
-- Each attendance record belongs to a student.
-- ==========================================

ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_student
FOREIGN KEY (roll_no)
REFERENCES students(roll_no);

-- ==========================================
-- Attendance → Subjects
-- Each attendance record belongs to a subject.
-- ==========================================

ALTER TABLE attendance
ADD CONSTRAINT fk_attendance_subject
FOREIGN KEY (subject_code)
REFERENCES subjects(subject_code);

-- ==========================================
-- Results → Students
-- Each result belongs to a student.
-- ==========================================

ALTER TABLE results
ADD CONSTRAINT fk_results_student
FOREIGN KEY (roll_no)
REFERENCES students(roll_no);

-- ==========================================
-- Results → Subjects
-- Each result belongs to a subject.
-- ==========================================

ALTER TABLE results
ADD CONSTRAINT fk_results_subject
FOREIGN KEY (subject_code)
REFERENCES subjects(subject_code);

-- ==========================================
-- Fees → Students
-- Each fee record belongs to a student.
-- ==========================================

ALTER TABLE fees
ADD CONSTRAINT fk_fees_student
FOREIGN KEY (roll_no)
REFERENCES students(roll_no);

-- ==========================================
-- Placements → Students
-- Each placement record belongs to a student.
-- ==========================================

ALTER TABLE placements
ADD CONSTRAINT fk_placements_student
FOREIGN KEY (roll_no)
REFERENCES students(roll_no);