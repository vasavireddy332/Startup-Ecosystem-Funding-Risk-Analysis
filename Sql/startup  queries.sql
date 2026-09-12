SELECT * FROM startup_analysis.startup_funding_cleaned;

USE startup_analysis;

SELECT COUNT(*) AS total_rows
FROM startup_funding_cleaned;

DESCRIBE startup_funding_cleaned;

SELECT *
FROM startup_funding_cleaned
LIMIT 5;

-- Date range
SELECT
    MIN(date_clean) AS earliest_date,
    MAX(date_clean) AS latest_date
FROM startup_funding_cleaned;

-- Number of cities (48)

select count(distinct city_clean) as total_cities
from startup_funding_cleaned;

-- Number of industries(564)
SELECT COUNT(DISTINCT industry_clean) AS total_industries
FROM startup_funding_cleaned;

-- total investment amount

SELECT
    SUM(amount_clean) AS total_investment
FROM startup_funding_cleaned;

-- date_clean type changing ---

alter table startup_funding_cleaned
add column date_temp DATE;
set sql_safe_updates=0;
update startup_funding_cleaned 
set date_temp = str_to_date(date_clean,'%m/%d/%Y');

alter table startup_funding_cleaned
drop column date_clean;

alter table startup_funding_cleaned
change column date_temp date_clean DATE;


















-- Yearly Funding Trend --
-- Total funding per year --
SELECT
    YEAR(STR_TO_DATE(date_clean, '%m/%d/%Y')) AS year,
    SUM(amount_clean) AS total_funding
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY YEAR(STR_TO_DATE(date_clean, '%m/%d/%Y'))
ORDER BY year;

-- Number of deals per year --
SELECT
    YEAR(STR_TO_DATE(date_clean, '%m/%d/%Y')) AS year,
    COUNT(*) AS number_of_deals
FROM startup_funding_cleaned
GROUP BY YEAR(STR_TO_DATE(date_clean, '%m/%d/%Y'))
ORDER BY year;

-- Average deal size per year --
SELECT
    YEAR(date_clean) AS year,
    ROUND(AVG(amount_clean), 2) AS average_deal_size
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY YEAR(date_clean)
ORDER BY year;

-- Growth % YOY --

 WITH yearly_funding AS (
    SELECT
        YEAR(date_clean) AS year,
        SUM(amount_clean) AS total_funding
    FROM startup_funding_cleaned
    WHERE amount_clean IS NOT NULL
    GROUP BY YEAR(date_clean)
)
SELECT
    year,
    total_funding,
    LAG(total_funding) OVER (ORDER BY year) AS previous_year_funding,
    ROUND(
        (total_funding - LAG(total_funding) OVER (ORDER BY year))
        / LAG(total_funding) OVER (ORDER BY year) * 100,
        2
    ) AS yoy_growth_percent
FROM yearly_funding
ORDER BY year;

-- City Comparison: --

-- total funding per city --
SELECT
    city_clean,
    SUM(amount_clean) AS total_funding
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY city_clean
ORDER BY total_funding DESC;

-- Number of startups funded per city --
SELECT
    city_clean,
    COUNT(DISTINCT startup_name) AS startups_funded
FROM startup_funding_cleaned
GROUP BY city_clean
ORDER BY startups_funded DESC;

-- Average funding per startup --

SELECT
    city_clean,
    ROUND(AVG(amount_clean), 2) AS average_funding_per_startup
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY city_clean
ORDER BY average_funding_per_startup DESC;

-- Sector Analysis:

-- total funding • Total funding per sector
-- • Number of deals per sector
-- • Average deal size
SELECT
    industry_clean AS sector,
    SUM(amount_clean) AS total_funding,
    COUNT(*) AS number_of_deals,
    ROUND(AVG(amount_clean), 2) AS average_deal_size
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY industry_clean
ORDER BY total_funding DESC;

-- funding volatility --
-- measure yearly volatility --
SELECT
    YEAR(date_clean) AS year,
    ROUND(STDDEV(amount_clean), 2) AS funding_volatility
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY YEAR(date_clean)
ORDER BY year;

-- Identify high-risk vs stable sectors--
SELECT
    industry_clean AS sector,
    ROUND(AVG(amount_clean), 2) AS average_deal_size,
    ROUND(STDDEV(amount_clean), 2) AS funding_volatility,
    CASE
        WHEN STDDEV(amount_clean) > AVG(amount_clean)
            THEN 'High Risk'
        ELSE 'Stable'
    END AS risk_category
FROM startup_funding_cleaned
WHERE amount_clean IS NOT NULL
GROUP BY industry_clean
HAVING COUNT(amount_clean) >= 2
ORDER BY funding_volatility DESC;