"""
Week 3: Data Visualization & Exploratory Data Analysis (EDA)
Next Gen Software Hub Pvt. Ltd. - Internship Task
Tools: Matplotlib, Seaborn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Output folder ────────────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)

# ── 1. Generate Sample Dataset ───────────────────────────────────────────────
np.random.seed(42)
n = 200

data = {
    "Age":        np.random.randint(18, 60, n).astype(float),
    "Salary":     np.random.normal(50000, 15000, n).round(2),
    "Department": np.random.choice(["HR", "Engineering", "Sales", "Marketing", "Finance"], n),
    "Experience": np.random.randint(0, 35, n).astype(float),
    "Score":      np.random.uniform(40, 100, n).round(2),
}

# Introduce missing values intentionally
missing_idx_salary = np.random.choice(n, 15, replace=False)
missing_idx_score  = np.random.choice(n, 10, replace=False)
data["Salary"][missing_idx_salary] = np.nan
data["Score"][missing_idx_score]   = np.nan

df = pd.DataFrame(data)

print("=" * 55)
print("  Week 3 – Data Visualization & EDA")
print("=" * 55)

# ── 2. Basic Info ─────────────────────────────────────────────────────────────
print("\n[Dataset Shape]:", df.shape)
print("\n[First 5 Rows]:\n", df.head())
print("\n[Data Types]:\n", df.dtypes)
print("\n[Statistical Summary]:\n", df.describe())

# ── 3. Missing Data Analysis ──────────────────────────────────────────────────
print("\n[Missing Values Before Handling]:\n", df.isnull().sum())

# Fill numeric missing values with column median
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Score"]  = df["Score"].fillna(df["Score"].median())

print("\n[Missing Values After Handling]:\n", df.isnull().sum())

# ── 4. Bar Chart – Employee Count by Department ───────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
dept_counts = df["Department"].value_counts()
colors = sns.color_palette("Blues_d", len(dept_counts))
ax.bar(dept_counts.index, dept_counts.values, color=colors, edgecolor="white")
ax.set_title("Employee Count by Department", fontsize=14, fontweight="bold")
ax.set_xlabel("Department")
ax.set_ylabel("Count")
ax.set_ylim(0, dept_counts.max() + 10)
for i, v in enumerate(dept_counts.values):
    ax.text(i, v + 1, str(v), ha="center", fontsize=10)
plt.tight_layout()
plt.savefig("outputs/bar_chart_department.png", dpi=150)
plt.close()
print("\n[Saved] outputs/bar_chart_department.png")

# ── 5. Histogram – Age & Salary Distribution ─────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].hist(df["Age"], bins=15, color="#4C72B0", edgecolor="white")
axes[0].set_title("Age Distribution", fontsize=13, fontweight="bold")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Frequency")

axes[1].hist(df["Salary"], bins=20, color="#55A868", edgecolor="white")
axes[1].set_title("Salary Distribution", fontsize=13, fontweight="bold")
axes[1].set_xlabel("Salary (₹)")
axes[1].set_ylabel("Frequency")

plt.suptitle("Histograms – Age & Salary", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/histogram_age_salary.png", dpi=150)
plt.close()
print("[Saved] outputs/histogram_age_salary.png")

# ── 6. Scatter Plot – Experience vs Salary ────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 6))
palette = sns.color_palette("Set2", len(df["Department"].unique()))
dept_colors = dict(zip(df["Department"].unique(), palette))

for dept, grp in df.groupby("Department"):
    ax.scatter(grp["Experience"], grp["Salary"],
               label=dept, color=dept_colors[dept], alpha=0.7, edgecolors="white", s=60)

ax.set_title("Experience vs Salary by Department", fontsize=14, fontweight="bold")
ax.set_xlabel("Years of Experience")
ax.set_ylabel("Salary (₹)")
ax.legend(title="Department")
plt.tight_layout()
plt.savefig("outputs/scatter_experience_salary.png", dpi=150)
plt.close()
print("[Saved] outputs/scatter_experience_salary.png")

# ── 7. Missing Data Heatmap ───────────────────────────────────────────────────
# Re-introduce missing for visual only
df_missing_demo = df.copy()
df_missing_demo.loc[missing_idx_salary, "Salary"] = np.nan
df_missing_demo.loc[missing_idx_score,  "Score"]  = np.nan

fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(df_missing_demo.isnull(), cbar=False, cmap="YlOrRd",
            yticklabels=False, ax=ax)
ax.set_title("Missing Data Heatmap (Before Handling)", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/missing_data_heatmap.png", dpi=150)
plt.close()
print("[Saved] outputs/missing_data_heatmap.png")

# ── 8. Correlation Heatmap ────────────────────────────────────────────────────
numeric_df = df[["Age", "Salary", "Experience", "Score"]]
corr = numeric_df.corr()

fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm",
            linewidths=0.5, ax=ax, square=True)
ax.set_title("Correlation Matrix", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=150)
plt.close()
print("[Saved] outputs/correlation_heatmap.png")

# ── 9. Boxplot – Salary by Department ────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))
sns.boxplot(data=df, x="Department", y="Salary", palette="Set3", ax=ax)
ax.set_title("Salary Distribution by Department", fontsize=13, fontweight="bold")
ax.set_xlabel("Department")
ax.set_ylabel("Salary (₹)")
plt.tight_layout()
plt.savefig("outputs/boxplot_salary_department.png", dpi=150)
plt.close()
print("[Saved] outputs/boxplot_salary_department.png")

# ── 10. Pairplot ──────────────────────────────────────────────────────────────
pairplot_fig = sns.pairplot(df[["Age", "Salary", "Experience", "Score", "Department"]],
                            hue="Department", palette="Set2", plot_kws={"alpha": 0.6})
pairplot_fig.fig.suptitle("Pairplot of Numeric Features", y=1.02, fontsize=13, fontweight="bold")
pairplot_fig.savefig("outputs/pairplot.png", dpi=120)
plt.close()
print("[Saved] outputs/pairplot.png")

print("\n[Done] All charts saved to outputs/ folder.")
