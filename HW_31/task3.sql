-- Task 1: 

-- 1) Display first name, last name, department number, and department name for each employee
SELECT
  e.first_name,
  e.last_name,
  e.department_id AS department_number,
  d.department_name
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id;

-- 2) Display first and last name, department, city, and state province for each employee
SELECT
  e.first_name,
  e.last_name,
  d.department_name AS department,
  l.city,
  l.state_province
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id
JOIN locations l
  ON d.location_id = l.location_id;

-- 3) Display first name, last name, department number, and department name for employees in departments 80 or 40
SELECT
  e.first_name,
  e.last_name,
  e.department_id AS department_number,
  d.department_name
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id
WHERE e.department_id IN (80, 40);

-- 4) Display all departments including those with no employees
SELECT
  d.department_id,
  d.department_name,
  e.employee_id,
  e.first_name,
  e.last_name
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
ORDER BY d.department_id;

-- 5) Display first name of all employees including the first name of their manager
SELECT
  e.first_name AS employee_first_name,
  m.first_name AS manager_first_name
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.employee_id;

-- 6) Display job title, full name, and the difference between max salary for the job and employee salary
SELECT
  j.job_title,
  (e.first_name || ' ' || e.last_name) AS full_name,
  (j.max_salary - e.salary) AS diff_to_job_max
FROM employees e
JOIN jobs j
  ON e.job_id = j.job_id;

-- 7) Display job title and the average salary of employees
SELECT
  j.job_title,
  AVG(e.salary) AS avg_salary
FROM employees e
JOIN jobs j
  ON e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY avg_salary DESC;

-- 8) Display full name and salary of employees who work in any department located in London
SELECT
  (e.first_name || ' ' || e.last_name) AS full_name,
  e.salary
FROM employees e
JOIN departments d
  ON e.department_id = d.department_id
JOIN locations l
  ON d.location_id = l.location_id
WHERE l.city = 'London';

-- 9) Display department name and the number of employees in each department
SELECT
  d.department_name,
  COUNT(e.employee_id) AS employees_count
FROM departments d
LEFT JOIN employees e
  ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
ORDER BY employees_count DESC, d.department_name;
