# 🚀 Startup Ecosystem Funding & Risk Analysis

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?logo=pandas)](https://pandas.pydata.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Analysis-4479A1?logo=mysql)](https://www.mysql.com/)
[![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi)](https://powerbi.microsoft.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#)

An end-to-end **Data Analytics project** that analyzes startup funding data using **Python, SQL, and Power BI**.

The project focuses on data cleaning, validation, SQL-based business analysis, funding trends, city and sector analysis, funding volatility, and interactive Power BI visualization.

---

## 📑 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objectives](#-project-objectives)
- [Technologies Used](#️-technologies-used)
- [Project Structure](#-project-structure)
- [Part A — Data Cleaning & Validation](#-part-a--data-cleaning--validation)
- [Part B — SQL Analytics](#-part-b--sql-analytics)
- [Part C — Power BI Dashboard](#-part-c--power-bi-dashboard)
- [Major Project Outcomes](#-major-project-outcomes)
- [Business Insights](#-business-insights)
- [Future Improvements](#-future-improvements)
- [Project Deliverables](#-project-deliverables)
- [Skills Demonstrated](#-skills-demonstrated)
- [Final Outcome](#-final-outcome)
- [Author](#-author)

---

## 📌 Project Overview

The startup ecosystem generates large amounts of funding data, but raw datasets often contain missing values, inconsistent names, invalid dates, and improperly formatted investment amounts.

This project transforms raw startup funding data into a clean, analysis-ready dataset and then uses SQL and Power BI to generate meaningful business insights.

### Project Workflow

\`\`\`
Raw Startup Funding Data
          ↓
Python / Pandas
          ↓
Data Cleaning & Transformation
          ↓
Data Validation
          ↓
Cleaned Dataset
          ↓
MySQL / SQL Analysis
          ↓
Business Insights
          ↓
Power BI Dashboard
          ↓
Interactive Visualization
\`\`\`

---

## 🎯 Project Objectives

- Clean and preprocess startup funding data
- Handle missing and invalid values
- Standardize city and industry names
- Convert investment amounts into numeric format
- Correct invalid date values
- Validate the cleaned dataset
- Analyze yearly funding trends
- Calculate year-over-year funding growth
- Compare startup funding across cities
- Analyze funding across sectors
- Measure funding volatility
- Identify high-volatility and stable sectors
- Build an interactive Power BI dashboard
- Present the final findings through business insights

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Data cleaning and preprocessing |
| 🐼 Pandas | Data manipulation and validation |
| 🗄️ MySQL | SQL analysis and business queries |
| 💻 MySQL Workbench | Database and query execution |
| 📊 Power BI | Interactive dashboard and visualization |
| 📐 DAX | Power BI calculations and measures |
| 📄 CSV | Data storage and data exchange |
| 📝 Markdown | Project documentation |

---

## 📂 Project Structure

\`\`\`
Startup-Ecosystem-Funding-Analysis/
│
├── data/
│   ├── startup_funding.csv
│   ├── startup_funding_cleaned.csv
│   └── startup_funding_cleaned_final.csv
│
├── python/
│   └── data_cleaning.ipynb
│
├── sql/
│   └── startup_analysis.sql
│
├── powerbi/
│   └── Startup_Ecosystem_Dashboard.pbix
│
├── report/
│   ├── Part_A_Data_Cleaning_Report.txt
│   └── dashboard_screenshots.pdf
│
└── README.md
\`\`\`

---

## 🔹 Part A — Data Cleaning & Validation

The original dataset contained **3,044 rows** and multiple data-quality issues.

### Initial Data Issues

The raw dataset contained:

- Missing industry values
- Missing subvertical values
- Missing city values
- Missing investment amounts
- Missing remarks
- Inconsistent city names
- Inconsistent industry names
- Extra spaces
- Invalid date formats
- Invalid investment amounts
- Text values in numerical columns
- Different spellings and representations of the same city/industry

### 🧹 Data Cleaning Process

**1. Column Cleaning**

Column names were standardized and useful cleaned columns were created. Important cleaned columns include:

\`sr_no\` · \`date_clean\` · \`startup_name\` · \`industry_clean\` · \`subvertical\` · \`city_clean\` · \`investors_name\` · \`investment_type\` · \`amount_clean\` · \`remarks\`

**2. City Cleaning**

Different representations of cities were standardized into a new \`city_clean\` column.

Examples:

| Original | Standardized |
|---|---|
| Bangalore | Bengaluru |
| Gurgaon | Gurugram |
| Delhi | New Delhi |

**Top Cleaned Cities**

| City | Records |
|---|---|
| Bengaluru | 855 |
| Mumbai | 575 |
| New Delhi | 463 |
| Gurugram | 342 |
| Unknown | 195 |
| Pune | 112 |
| Hyderabad | 101 |
| Chennai | 99 |
| Noida | 94 |
| Ahmedabad | 41 |

> **City Insight:** Bengaluru had the highest number of funding records with 855 records, followed by Mumbai (575) and New Delhi (463) — the strongest startup funding hub by number of records in the cleaned dataset.

**3. Industry Cleaning**

Industry names were standardized into a cleaned \`industry_clean\` column, including: Consumer Internet, Technology, E-Commerce, Healthcare, Finance, Food & Beverage, Logistics, Education, EdTech, FinTech, Information Technology, Transportation, Automobile, and Real Estate. Missing or unusable values were categorized as \`Unknown\`.

**Top Cleaned Industries**

| Sector | Records |
|---|---|
| Consumer Internet | 943 |
| Technology | 478 |
| E-Commerce | 300 |
| Healthcare | 73 |
| Finance | 63 |
| Food & Beverage | 35 |
| Logistics | 32 |
| Education | 24 |
| EdTech | 21 |
| FinTech | 18 |

> **Sector Insight:** Consumer Internet was the most frequently recorded sector with 943 funding records, followed by Technology (478) and E-Commerce (300).

**4. Investment Amount Cleaning**

Raw values such as \`20,00,00,000\`, \`80,48,394\`, \`1,83,58,860\`, and \`30,00,000\` were converted into numeric format in a cleaned \`amount_clean\` column.

| Original | Cleaned |
|---|---|
| 20,00,00,000 | 200,000,000 |
| 80,48,394 | 8,048,394 |
| 30,00,000 | 3,000,000 |

Invalid textual values such as \`undisclosed\`, \`Undisclosed\`, and \`unknown\` were treated as missing values rather than being interpreted as funding amounts.

**Investment Amount Summary**

| Metric | Value |
|---|---|
| Count | 2,073 |
| Mean | 18,400,344.85 |
| Minimum | 16,000 |
| 25th Percentile | 486,000 |
| Median | 1,750,000 |
| 75th Percentile | 8,000,000 |
| Maximum | 3,900,000,000 |

**5. Date Cleaning**

The original date column contained inconsistent and malformed values, e.g. \`9/1/2020\`, \`13/01/2020\`, \`05/072018\`, \`01/07/015\`, \`22/01//2015\`. A cleaned \`date_clean\` column was created and converted to a proper date datatype.

| Metric | Value |
|---|---|
| Earliest Date | 2015-01-02 |
| Latest Date | 2020-01-13 |
| Invalid Entries Handled | 7 |

### 🔍 Data Validation

**Duplicate Check**

| Check | Result |
|---|---|
| Completely duplicate rows | 0 |
| Duplicate Startup + Date combinations | 0 |

**Final Dataset**

| Metric | Value |
|---|---|
| Rows | 3,044 |
| Columns | 14 |
| Duplicate Rows | 0 |
| Missing Dates | 0 |
| Missing Cities | 0 |
| Missing Industries | 0 |

The cleaned dataset was saved as \`startup_funding_cleaned_final.csv\`.

### 📊 Before vs After Cleaning

| Before Cleaning | After Cleaning |
|---|---|
| ❌ Inconsistent city names | ✅ Standardized city names |
| ❌ Inconsistent industry names | ✅ Standardized industry categories |
| ❌ Invalid date formats | ✅ Valid date datatype |
| ❌ Investment amounts stored as text | ✅ Numeric investment amounts |
| ❌ Invalid numerical values | ✅ Invalid amounts handled |
| ❌ Missing values | ✅ Clean analytical columns |
| ❌ Extra spaces | ✅ Duplicate validation completed |
| ❌ Difficult aggregation | ✅ Data ready for SQL analysis |
| ❌ Difficult visualization | ✅ Data ready for Power BI visualization |

---

## 🔹 Part B — SQL Analytics

The cleaned data was imported into MySQL Workbench for business analysis across four major areas:

1. Yearly Funding Trend
2. City Comparison
3. Sector Analysis
4. Funding Volatility

### 📈 1. Yearly Funding Trend

Metrics calculated: total funding per year, number of deals per year, average deal size, and year-over-year growth.

| Year | Total Funding | YoY Growth |
|---|---|---|
| 2015 | 8.67 Billion | — |
| 2016 | 3.83 Billion | -55.86% |
| 2017 | 7.91 Billion | +106.63% |
| 2018 | 5.12 Billion | -35.24% |
| 2019 | 5.80 Billion | +13.25% |
| 2020 | 0.39 Billion | -93.27% |

**Key Findings**

- Funding decreased by 55.86% in 2016.
- 2017 recorded the strongest year-over-year growth of 106.63%.
- Funding declined by 35.24% in 2018.
- Funding increased by 13.25% in 2019.
- 2020 recorded a 93.27% decline compared with 2019 in the available dataset.
- The overall funding trend was highly variable.

### 🏙️ 2. City Comparison

Cities were compared using total funding, number of startups funded, and average funding per startup — helping identify major startup funding hubs and their funding intensity.

Based on the cleaned dataset, **Bengaluru** had the highest number of funding records with 855 records. Other major cities included Mumbai, New Delhi, Gurugram, Pune, Hyderabad, Chennai, Noida, Ahmedabad, and Jaipur.

> Total funding by city was calculated separately in SQL — the exact highest-funded city should be taken from the final City Comparison SQL output.

### 🏭 3. Sector Analysis

Sector analysis was performed using \`industry_clean\`, calculating total funding per sector, number of deals per sector, and average deal size.

**Consumer Internet** had the highest number of funding records with 943 records, followed by Technology (478) and E-Commerce (300), then Healthcare (73) and Finance (63) — showing that Consumer Internet, Technology, and E-Commerce were the major areas of startup funding activity.

### ⚠️ 4. Funding Volatility

Funding volatility was measured using standard deviation (\`STDDEV(amount_clean)\`) to understand how much funding amounts varied between deals.

\`\`\`
Higher volatility
        ↓
Greater variation in funding
        ↓
Higher funding uncertainty / risk

Lower volatility
        ↓
More consistent funding amounts
        ↓
Greater stability
\`\`\`

Sector-level volatility was also analyzed to compare relatively high-volatility sectors with more stable sectors.

---

## 🔹 Part C — Power BI Dashboard

An interactive Power BI dashboard was developed with three pages.

### 📄 Page 1 — Executive Overview

A high-level summary of the startup funding ecosystem.

- **KPI Cards:** Total Funding, Total Deals, Average Deal Size
- **Visualization:** Line chart of the Yearly Funding Trend

This page allows users to quickly understand overall funding performance and trend.

### 📄 Page 2 — City & Sector Intelligence

Focuses on geographic and sector-level analysis.

- **Funding by City** — total startup funding across cities
- **Funding by Sector** — funding distribution across sectors
- **Growth Visual** — year-over-year funding growth

This page helps identify major startup hubs, leading sectors, and funding growth patterns.

### 📄 Page 3 — Risk & Volatility Monitoring

Focuses on funding risk and data quality.

- **Volatility Trend** — funding volatility across years
- **Sector Stability Comparison** — funding volatility between sectors
- **Data Completeness Indicators** — Total Records, Missing Amounts, Data Completeness %

This page helps users understand both funding risk and the completeness of the underlying data.

---
## 🏆 Final Key Outcomes — What the Data Tells Us

Based on number of funding records (deals) in the cleaned dataset:

### 🥇 Best Performing City
**Bengaluru** 🏙️ is the strongest startup hub in India, leading with **855 funding records** — nearly 1.5x more than the next city, Mumbai (575).

| Rank | City | Records |
|---|---|---|
| 🥇 1 | Bengaluru | 855 |
| 🥈 2 | Mumbai | 575 |
| 🥉 3 | New Delhi | 463 |
| 4 | Gurugram | 342 |

> 💡 **Insight:** Bengaluru's dominance reflects its position as India's tech and startup capital, attracting the highest deal volume year after year.

### 🥇 Best Performing Industry / Sector
**Consumer Internet** 🌐 is the most actively funded sector, with **943 funding records** — clearly ahead of Technology (478) and E-Commerce (300).

| Rank | Sector | Records |
|---|---|---|
| 🥇 1 | Consumer Internet | 943 |
| 🥈 2 | Technology | 478 |
| 🥉 3 | E-Commerce | 300 |
| 4 | Healthcare | 73 |
| 5 | Finance | 63 |

> 💡 **Insight:** Consumer Internet, Technology, and E-Commerce together account for the vast majority of all funding activity, showing investors strongly favor digital-first, consumer-facing business models over traditional sectors.

### 📈 Best Performing Year
**2017** was the standout year, posting the highest year-over-year growth at **+106.63%**, more than doubling the funding seen in 2016.

### 📉 Weakest Performing Year
**2020** recorded the sharpest decline at **-93.27%** compared to 2019 (note: this reflects the partial 2020 data available in the dataset, not a full calendar year).

### 📝 Note on "Best by Amount" vs "Best by Count"
The rankings above are based on **number of deals/records**, which shows *where startup activity is concentrated*. The **exact highest-funded city and sector by total ₹/$ amount** should be confirmed from the SQL `SUM(amount_clean)` output in `startup_analysis.sql`, since a city/sector can have fewer deals but larger average deal sizes (e.g. a sector with few but very large funding rounds could out-earn one with many small deals).

| Question | Where to look |
|---|---|
| Which city has the most **deals**? | Bengaluru (855) — confirmed above |
| Which city has the highest **total funding amount**? | See SQL `GROUP BY city_clean ORDER BY SUM(amount_clean) DESC` |
| Which sector has the most **deals**? | Consumer Internet (943) — confirmed above |
| Which sector has the highest **total funding amount**? | See SQL `GROUP BY industry_clean ORDER BY SUM(amount_clean) DESC` |

## 📌 Major Project Outcomes

| Category | Outcome |
|---|---|
| 🏙️ City | Bengaluru had the highest number of funding records with 855 records |
| 🏭 Sector | Consumer Internet had the highest number of funding records with 943 records |
| 📈 Growth | 2017 recorded the highest year-over-year funding growth at 106.63% |
| 📉 Decline | 2020 recorded the largest year-over-year decline at 93.27% in the available dataset |
| 💰 Funding Variation | Investment amounts varied significantly, from small deals to very large funding rounds |
| 🔎 Data Quality | 0 duplicate rows, 0 missing dates, 0 missing cleaned cities, 0 missing cleaned industries after
