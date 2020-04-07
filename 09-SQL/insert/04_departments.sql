DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    dept_no VARCHAR(4) PRIMARY KEY,
    dept_name VARCHAR(32) NOT NULL
);

INSERT INTO departments (dept_no, dept_name)
VALUES
    ('d001', 'Marketing'),
    ('d002', 'Finance'),
    ('d003', 'Human Resources'),
    ('d004', 'Production'),
    ('d005', 'Development'),
    ('d006', 'Quality Management'),
    ('d007', 'Sales'),
    ('d008', 'Customer Service'),
    ('d009', 'Research');