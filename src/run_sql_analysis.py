import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("database/hr_employee_attrition.db")

print("==========================================")
print("HR EMPLOYEE ATTRITION SQL ANALYSIS")
print("==========================================")

# 1. Total Employees
query = """
SELECT COUNT(*) AS total_employees
FROM employees;
"""

result = pd.read_sql_query(query, conn)

print("\n========== TOTAL EMPLOYEES ==========")
print(result.to_string(index=False))


# 2. Overall Attrition
query = """
SELECT
    Attrition,
    COUNT(*) AS employee_count
FROM employees
GROUP BY Attrition;
"""

result = pd.read_sql_query(query, conn)

print("\n========== OVERALL ATTRITION ==========")
print(result.to_string(index=False))


# 3. Attrition Rate
query = """
SELECT
    ROUND(
        SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS attrition_rate_percentage
FROM employees;
"""

result = pd.read_sql_query(query, conn)

print("\n========== OVERALL ATTRITION RATE ==========")
print(result.to_string(index=False))


# 4. Attrition by Department
query = """
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
"""

result = pd.read_sql_query(query, conn)

print("\n========== ATTRITION BY DEPARTMENT ==========")
print(result.to_string(index=False))


# 5. Attrition by Overtime
query = """
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
"""

result = pd.read_sql_query(query, conn)

print("\n========== ATTRITION BY OVERTIME ==========")
print(result.to_string(index=False))


# 6. Attrition by Job Role
query = """
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
"""

result = pd.read_sql_query(query, conn)

print("\n========== ATTRITION BY JOB ROLE ==========")
print(result.to_string(index=False))


# 7. Average Income by Attrition
query = """
SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS average_monthly_income
FROM employees
GROUP BY Attrition;
"""

result = pd.read_sql_query(query, conn)

print("\n========== AVERAGE MONTHLY INCOME ==========")
print(result.to_string(index=False))


# 8. Attrition by Job Satisfaction
query = """
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
"""

result = pd.read_sql_query(query, conn)

print("\n========== ATTRITION BY JOB SATISFACTION ==========")
print(result.to_string(index=False))


# Close database connection
conn.close()

print("\n==========================================")
print("SQL ANALYSIS COMPLETED SUCCESSFULLY!")
print("==========================================")
