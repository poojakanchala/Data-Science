-- QUESTION- To find top-2 cust_credit_limit by city


-- Sub-query

select * from (
    select cust_city, 
    cust_credit_limit, 
    row_number () 
    over(PARTITION BY CUST_CITY ORDER BY CUST_CREDIT_LIMIT DESC) AS RN 
    FROM SH.CUSTOMERS
) WHERE RN <=2


-- CTE (Common Table Expression)

with cust_info AS
(
    select cust_city,
    cust_credit_limit, 
    row_number () 
    over(PARTITION BY CUST_CITY ORDER BY CUST_CREDIT_LIMIT DESC) AS RN 
    FROM SH.CUSTOMERS
)
select * from cust_info WHERE RN <=2 

-- QUESTION- creste a new column to give the credits(premium,standard) for cust_credit_limit using cust_id 

with cust_info as (
    select 
      cust_id, 
      cust_credit_limit,
      row_number() over (order by cust_credit_limit) as rn
    from
     sh.customers

)

select 
  cust_id, 
  cust_credit_limit,
  case
    WHERE rn <= 5 Then 'Premium'
    else 'Standard'
  END AS cust_tier
from cust_info
order by cust_credit_limit desc;


-- 🧱 A. Aggregation & Grouping (20 Questions)
-- 1.Find the total, average, minimum, and maximum credit limit of all customers.
select sum(cust_credit_limit) as total,avg(cust_credit_limit) as avge, max(cust_credit_limit) mini,min(cust_credit_limit) maxy
from sh.customers

-- 2.Count the number of customers in each income level.

select cust_income_level, count(*)
from sh.CUSTOMERS
group by cust_income_level 

-- 3.Show total credit limit by state and country.

select cust_state_province_id, country_id, sum(cust_credit_limit) as total_credit_limit
from sh.customers
group by cust_state_province_id, country_id


-- 4.Display average credit limit for each marital status and gender combination.
select cust_marital_status, cust_gender, avg(cust_credit_limit) as avg_credit_limit
from sh.customers
group by cust_marital_status, cust_gender

-- 5.Find the top 3 states with the highest average credit limit.

select cust_state_province_id, avg(cust_credit_limit) as avg_credit_limit 
from sh.CUSTOMERS
group by cust_state_province_id
order by avg_credit_limit desc
fetch first 3 rows only 


-- 6.Find the country with the maximum total customer credit limit.
select country_id, max(cust_credit_limit) as max_credit_limit 
from sh.CUSTOMERS
group by country_id

-- 7.Show the number of customers whose credit limit exceeds their state average.
SELECT COUNT(*)
FROM sh.customers c
WHERE cust_credit_limit > (
    SELECT AVG(cust_credit_limit)
    FROM sh.customers
    WHERE cust_state_province = c.cust_state_province
)

-- 8.Calculate total and average credit limit for customers born after 1980.
select cust_year_of_birth, 
       sum(cust_credit_limit) total, 
       avg(cust_credit_limit) avg_credit 
from sh.customers 
group by cust_credit_limit, cust_year_of_birth 
having cust_year_of_birth > 1980

-- 9.Find states having more than 50 customers.

select cust_state_province_id, count(*) 
from sh.CUSTOMERS
group by cust_state_province_id
having count(*) > 50

-- 10.List countries where the average credit limit is higher than the global average.

SELECT country_id, AVG(cust_credit_limit) 
FROM sh.customers
GROUP BY country_id
HAVING AVG(cust_credit_limit) > (
    SELECT AVG(cust_credit_limit) 
    FROM sh.customers
)

-- 11.Calculate the variance and standard deviation of customer credit limits by country.

select country_id, var_samp(cust_credit_limit) variance_s, STDDEV(cust_credit_limit) standard_deviation 
from sh.customers 
group by country_id

-- 12.Find the state with the smallest range (max–min) in credit limits.

SELECT cust_state_province_id, 
       MAX(cust_credit_limit) - MIN(cust_credit_limit) credit_range
FROM sh.customers
GROUP BY cust_state_province_id
ORDER BY credit_range ASC 
FETCH FIRST ROW ONLY

-- 13.Show the total number of customers per income level and the percentage contribution of each.

SELECT 
    cust_income_level,
    COUNT(*) AS total_customers,
    ROUND( (COUNT(*) * 100.0 / SUM(COUNT(*)) OVER()),2) AS percentage_contribution
FROM sh.customers
GROUP BY cust_income_level
ORDER BY total_customers DESC;

-- 14.For each income level, find how many customers have NULL credit limits.

SELECT CUST_INCOME_LEVEL, COUNT(*) AS NULL_CREDITS
FROM SH.CUSTOMERS
WHERE CUST_CREDIT_LIMIT IS NULL
GROUP BY CUST_INCOME_LEVEL
ORDER BY CUST_INCOME_LEVEL ASC

15.Display countries where the sum of credit limits exceeds 10 million.

SELECT country_id,
       SUM(cust_credit_limit) AS total_credit_limit
FROM sh.customers
GROUP BY country_id
HAVING SUM(cust_credit_limit) > 10000000
ORDER BY total_credit_limit DESC;

-- 16.Find the state that contributes the highest total credit limit to its country.

SELECT country_id, cust_state_province_id, SUM(cust_credit_limit) AS total_credit
FROM sh.customers
GROUP BY country_id, cust_state_province_id
HAVING SUM(cust_credit_limit) = (
    SELECT MAX(SUM(cust_credit_limit))
    FROM sh.customers
    WHERE country_id = sh.customers.country_id
    GROUP BY cust_state_province_id
)

-- 17.Show total credit limit per year of birth, sorted by total descending.

SELECT EXTRACT(YEAR FROM birth_date) AS birth_year,
       SUM(cust_credit_limit) AS total_credit
FROM sh.customers
GROUP BY EXTRACT(YEAR FROM birth_date)
ORDER BY total_credit DESC;

-- 18.Identify customers who hold the maximum credit limit in their respective country.

SELECT cust_id, country_id, cust_credit_limit
FROM sh.customers c
WHERE cust_credit_limit = (
    SELECT MAX(cust_credit_limit)
    FROM sh.customers
    WHERE country_id = c.country_id
);

-- 19.Show the difference between maximum and average credit limit per country.

SELECT country_id,
       MAX(cust_credit_limit) - AVG(cust_credit_limit) AS max_avg_difference
FROM sh.customers
GROUP BY country_id;

-- 20.Display the overall rank of each state based on its total credit limit (using GROUP BY + analytic rank).

SELECT cust_state_province_id,
       SUM(cust_credit_limit) AS total_credit,
       RANK() OVER (ORDER BY SUM(cust_credit_limit) DESC) AS state_rank
FROM sh.customers
GROUP BY cust_state_province_id
ORDER BY state_rank;
