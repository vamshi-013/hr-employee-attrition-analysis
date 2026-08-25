import pandas as pd
import matplotlib.pyplot as plt
import os

# -------------------------------
# Load Dataset
# -------------------------------

df = pd.read_csv("data/hr_employee_attrition.csv")

print("==========================================")
print("HR EMPLOYEE ATTRITION ANALYSIS")
print("==========================================")

print(f"\nTotal Employees: {len(df)}")

# -------------------------------
# Overall Attrition
# -------------------------------

attrition_counts = df["Attrition"].value_counts()

print("\n========== ATTRITION OVERVIEW ==========")
print(attrition_counts)

attrition_rate = (
    (df["Attrition"] == "Yes").sum() / len(df) * 100
)

print(f"\nOverall Attrition Rate: {attrition_rate:.2f}%")

# -------------------------------
# Attrition by Department
# -------------------------------

department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
) * 100

print("\n========== ATTRITION BY DEPARTMENT ==========")
print(department_attrition.round(2))

# -------------------------------
# Attrition by Overtime
# -------------------------------

overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print("\n========== ATTRITION BY OVERTIME ==========")
print(overtime_attrition.round(2))

# -------------------------------
# Attrition by Job Role
# -------------------------------

jobrole_attrition = pd.crosstab(
    df["JobRole"],
    df["Attrition"],
    normalize="index"
) * 100

print("\n========== ATTRITION BY JOB ROLE ==========")
print(jobrole_attrition.round(2))

# -------------------------------
# Average Monthly Income
# -------------------------------

income_by_attrition = df.groupby(
    "Attrition"
)["MonthlyIncome"].mean()

print("\n========== AVERAGE MONTHLY INCOME ==========")
print(income_by_attrition.round(2))

# -------------------------------
# Create Output Folder
# -------------------------------

os.makedirs("output", exist_ok=True)

# -------------------------------
# Chart 1: Attrition Count
# -------------------------------

attrition_counts.plot(
    kind="bar",
    title="Employee Attrition Count"
)

plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.tight_layout()

plt.savefig("output/attrition_count.png")
plt.close()

# -------------------------------
# Chart 2: Attrition by Department
# -------------------------------

department_attrition["Yes"].sort_values(
    ascending=False
).plot(
    kind="bar",
    title="Attrition Rate by Department"
)

plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("output/attrition_by_department.png")
plt.close()

# -------------------------------
# Chart 3: Attrition by Overtime
# -------------------------------

overtime_attrition["Yes"].plot(
    kind="bar",
    title="Attrition Rate by Overtime"
)

plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.tight_layout()

plt.savefig("output/attrition_by_overtime.png")
plt.close()

# -------------------------------
# Chart 4: Monthly Income
# -------------------------------

income_by_attrition.plot(
    kind="bar",
    title="Average Monthly Income by Attrition"
)

plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")
plt.tight_layout()

plt.savefig("output/income_by_attrition.png")
plt.close()

print("\n==========================================")
print("ANALYSIS COMPLETED SUCCESSFULLY!")
print("==========================================")

print("\nCharts saved in the output folder.")
