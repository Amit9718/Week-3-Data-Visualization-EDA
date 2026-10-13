# Week 3: Data Visualization & EDA
**Next Gen Software Hub Pvt. Ltd. – Internship**

## Overview
This project covers **Exploratory Data Analysis (EDA)** and **Data Visualization** using Python's Matplotlib and Seaborn libraries. A synthetic employee dataset is generated, cleaned, and analyzed through multiple chart types.

---

## Task Breakdown

| # | Task | Status |
|---|------|--------|
| 1 | Learn Matplotlib & Seaborn | ✅ |
| 2 | Create bar charts | ✅ |
| 3 | Create histograms | ✅ |
| 4 | Create scatter plots | ✅ |
| 5 | Missing data handling | ✅ |
| 6 | Correlation analysis | ✅ |

---

## Tools & Libraries

- **Python 3.x**
- **Pandas** – data manipulation
- **NumPy** – numerical operations
- **Matplotlib** – core plotting
- **Seaborn** – statistical visualizations

---

## Project Structure

```
week3_eda/
├── eda_analysis.py       # Main EDA script
├── README.md             # This file
└── outputs/              # Generated charts (auto-created on run)
    ├── bar_chart_department.png
    ├── histogram_age_salary.png
    ├── scatter_experience_salary.png
    ├── missing_data_heatmap.png
    ├── correlation_heatmap.png
    ├── boxplot_salary_department.png
    └── pairplot.png
```

---

## Setup & Installation

```bash
pip install pandas numpy matplotlib seaborn
```

---

## How to Run

```bash
cd week3_eda
python eda_analysis.py
```

All charts are saved automatically to the `outputs/` folder.

---

## Dataset

A synthetic employee dataset (200 rows) with these columns:

| Column | Type | Description |
|--------|------|-------------|
| Age | int | Employee age (18–60) |
| Salary | float | Annual salary with missing values |
| Department | str | One of HR, Engineering, Sales, Marketing, Finance |
| Experience | int | Years of experience (0–35) |
| Score | float | Performance score (40–100) with missing values |

---

## Visualizations Generated

### 1. Bar Chart – Employee Count by Department
Shows how employees are distributed across departments.

### 2. Histogram – Age & Salary Distribution
Side-by-side histograms revealing the spread of age and salary.

### 3. Scatter Plot – Experience vs Salary
Colored by department; shows the relationship between experience and salary.

### 4. Missing Data Heatmap
Visualizes null values across the dataset before handling.

### 5. Correlation Heatmap
Pearson correlation matrix for all numeric features.

### 6. Boxplot – Salary by Department
Compares salary ranges and outliers across departments.

### 7. Pairplot
Pairwise relationships between all numeric columns, colored by department.

---

## Key Findings

- **Missing data** was found in `Salary` (15 rows) and `Score` (10 rows); filled with column median.
- **Salary** follows an approximately normal distribution around ₹50,000.
- **Experience** shows a weak positive correlation with Salary.
- Department-wise salary spreads are broadly similar, with minor variation in Engineering and Finance.

---

## Resources

- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)

---

*Internship – Week 3 Submission | Next Gen Software Hub Pvt. Ltd.*
