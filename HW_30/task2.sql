-- Task 2: 

-- 1) Display employee names with aliases "First Name", "Last Name"
SELECT
  first_name AS "First Name",
  last_name  AS "Last Name"
FROM employees;

-- 2) Get unique department IDs from employees table
SELECT DISTINCT
  department_id
FROM employees;

-- 3) Get all employee details ordered by first_name descending
SELECT
  *
FROM employees
ORDER BY first_name DESC;

-- 4) Get first_name, last_name, salary, and PF (12% of salary)
SELECT
  first_name,
  last_name,
  salary,
  salary * 0.12 AS PF
FROM employees;

-- 5) Get maximum and minimum salary from employees table
SELECT
  MAX(salary) AS max_salary,
  MIN(salary) AS min_salary
FROM employees;

-- 6) Get monthly salary rounded to 2 decimal places for each employee
SELECT
  employee_id,
  first_name,
  last_name,
  ROUND(salary / 12.0, 2) AS monthly_salary
FROM employees;
