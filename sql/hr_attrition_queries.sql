-- ==========================================
-- HR EMPLOYEE ATTRITION ANALYSIS
-- ==========================================


-- 1. Total Employees
SELECT COUNT(*) AS total_employees
FROM employees;


-- 2. Overall Attrition Count
SELECT
    Attrition,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Attrition;


-- 3. Attrition Rate
SELECT
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate_percentage
FROM employees;


-- 4. Attrition by Department
SELECT
    Department,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY Department
ORDER BY attrition_rate DESC;


-- 5. Attrition by Overtime
SELECT
    OverTime,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY OverTime
ORDER BY attrition_rate DESC;


-- 6. Attrition by Job Role
SELECT
    JobRole,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY JobRole
ORDER BY attrition_rate DESC;


-- 7. Average Monthly Income by Attrition
SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS average_monthly_income
FROM employees
GROUP BY Attrition;


-- 8. Attrition by Job Satisfaction
SELECT
    JobSatisfaction,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY JobSatisfaction
ORDER BY attrition_rate DESC;


-- 9. Attrition by Work-Life Balance
SELECT
    WorkLifeBalance,
    COUNT(*) AS total_employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY WorkLifeBalance
ORDER BY attrition_rate DESC;