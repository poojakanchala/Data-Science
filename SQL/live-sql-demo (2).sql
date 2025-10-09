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



-- B. Analytical / Window Functions (30 Questions)

1-- Assign row numbers to customers ordered by credit limit descending.
SELECT cust_id, cust_credit_limit,
 row_number() over (Order by cust_credit_limit desc) as row_number
from sh.customers

2-- Rank customers within each state by credit limit.
select cust_id, cust_state_province_id,
 rank() over (Partition by cust_credit_limit Order by cust_credit_limit desc) as rank_number
from sh.customers 

3-- Use DENSE_RANK() to find the top 5 credit holders per country.
select cust_id, country_id, cust_credit_limit,
  dense_rank() over (Partition by country_id order by cust_credit_limit) as dense_ranks
from sh.customers

4-- Divide customers into 4 quartiles based on their credit limit using NTILE(4).

select cust_id, cust_credit_limit,
  NTILE(4) over (Order by cust_credit_limit desc) as quartiles
from sh.customers;

5-- Calculate a running total of credit limits ordered by customer_id.

select cust_id, cust_credit_limit,
 sum(cust_credit_limit) over (Order by cust_id desc) as running_total
from sh.customers

6-- Show cumulative average credit limit by country.

select cust_id,country_id, cust_credit_limit,
 avg(cust_credit_limit) over (Partition by country_id Order by cust_id desc) as avg_credit_limit
from sh.customers

7-- Compare each customer’s credit limit to the previous one using LAG().

SELECT
    cust_id,
    cust_credit_limit,
    LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS previous_credit_limit,
    cust_credit_limit - LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS difference_from_previous
FROM sh.customers;

8-- Show next customer’s credit limit using LEAD().
SELECT
    cust_id,
    cust_credit_limit,
    LEAD(cust_credit_limit) OVER (ORDER BY cust_id) AS next_credit_limit
FROM sh.customers

9-- Display the difference between each customer’s credit limit and the previous one.

SELECT
    cust_id,
    cust_credit_limit,
    LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS previous_credit_limit,
    cust_credit_limit - LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS difference_from_previous
FROM sh.customers;

10-- For each country, display the first and last credit limit using FIRST_VALUE() and LAST_VALUE().

SELECT DISTINCT
    country_id,
    FIRST_VALUE(cust_credit_limit) OVER (PARTITION BY country_id ORDER BY cust_id) AS first_credit_limit,
    LAST_VALUE(cust_credit_limit) OVER (
        PARTITION BY country_id 
        ORDER BY cust_id 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS last_credit_limit
FROM sh.customers;


11-- Compute percentage rank (PERCENT_RANK()) of customers based on credit limit.

SELECT
    cust_id,
    cust_credit_limit,
    PERCENT_RANK() OVER (ORDER BY cust_credit_limit) AS percent_rank
FROM sh.customers;

12-- Show each customer’s position in percentile (CUME_DIST() function).

SELECT
    cust_id,
    cust_credit_limit,
    CUME_DIST() OVER (ORDER BY cust_credit_limit) AS percentile_position
FROM sh.customers;

13-- Display the difference between the maximum and current credit limit for each customer.

SELECT
    cust_id,
    cust_credit_limit,
    MAX(cust_credit_limit) OVER () - cust_credit_limit AS difference_from_max
FROM sh.customers;

14-- Rank income levels by their average credit limit.

SELECT
    cust_income_level,
    AVG(cust_credit_limit) AS avg_credit_limit,
    RANK() OVER (ORDER BY AVG(cust_credit_limit) DESC) AS rank_by_avg_credit
FROM sh.customers
GROUP BY cust_income_level;

15-- Calculate the average credit limit over the last 10 customers (sliding window).

SELECT
    cust_id,
    cust_credit_limit,
    AVG(cust_credit_limit) OVER (
        ORDER BY cust_id
        ROWS BETWEEN 9 PRECEDING AND CURRENT ROW
    ) AS avg_last_10_customers
FROM sh.customers;

16-- For each state, calculate the cumulative total of credit limits ordered by city.
SELECT
    cust_id,
    cust_state_province_id,
    cust_city,
    cust_credit_limit,
    SUM(cust_credit_limit) OVER (PARTITION BY cust_state_province_id ORDER BY cust_city) AS cumulative_credit
FROM sh.customers;

17-- Find customers whose credit limit equals the median credit limit (use PERCENTILE_CONT(0.5)).

SELECT *
FROM sh.customers
WHERE cust_credit_limit = (
    SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY cust_credit_limit) 
    FROM sh.customers
);

18-- Display the highest 3 credit holders per state using ROW_NUMBER() and PARTITION BY.

SELECT *
FROM (
    SELECT
        cust_id,
        cust_state_province_id,
        cust_credit_limit,
        ROW_NUMBER() OVER (PARTITION BY cust_state_province_id ORDER BY cust_credit_limit DESC) AS rn
    FROM sh.customers
) 
WHERE rn <= 3;

19-- Identify customers whose credit limit increased compared to previous row (using LAG).

SELECT *
FROM (
    SELECT
        cust_id,
        cust_credit_limit,
        LAG(cust_credit_limit) OVER (ORDER BY cust_id) AS prev_credit
    FROM sh.customers
) 
WHERE cust_credit_limit > prev_credit;

20-- Calculate moving average of credit limits with a window of 3.

SELECT
    cust_id,
    cust_credit_limit,
    AVG(cust_credit_limit) OVER (
        ORDER BY cust_id
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3
FROM sh.customers;

21-- Show cumulative percentage of total credit limit per country.

SELECT
    cust_id,
    country_id,
    cust_credit_limit,
    SUM(cust_credit_limit) OVER (PARTITION BY country_id ORDER BY cust_id) /
    SUM(cust_credit_limit) OVER (PARTITION BY country_id) * 100 AS cumulative_pct
FROM sh.customers;

22-- Rank customers by age (derived from CUST_YEAR_OF_BIRTH).

SELECT
    cust_id,
    cust_year_of_birth,
    (EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) AS age,
    RANK() OVER (ORDER BY (EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) DESC) AS age_rank
FROM sh.customers;

23-- Calculate difference in age between current and previous customer in the same state.

SELECT
    cust_id,
    cust_state_province_id,
    cust_year_of_birth,
    (EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) AS age,
    (EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) - 
        LAG(EXTRACT(YEAR FROM SYSDATE) - cust_year_of_birth) OVER (PARTITION BY cust_state_province_id ORDER BY cust_id) AS age_diff
FROM sh.customers;

24-- Use RANK() and DENSE_RANK() to show how ties are treated differently.

SELECT
    cust_id,
    cust_credit_limit,
    RANK() OVER (ORDER BY cust_credit_limit DESC) AS rank_with_gaps,
    DENSE_RANK() OVER (ORDER BY cust_credit_limit DESC) AS dense_rank_no_gaps
FROM sh.customers;

25-- Compare each state’s average credit limit with country average using window partition.

SELECT
    cust_id,
    cust_state_province_id,
    country_id,
    cust_credit_limit,
    AVG(cust_credit_limit) OVER (PARTITION BY cust_state_province_id) AS state_avg,
    AVG(cust_credit_limit) OVER (PARTITION BY country_id) AS country_avg
FROM sh.customers;

26-- Show total credit per state and also its rank within each country.

SELECT
    country_id,
    cust_state_province_id,
    SUM(cust_credit_limit) AS total_credit,
    RANK() OVER (PARTITION BY country_id ORDER BY SUM(cust_credit_limit) DESC) AS state_rank_in_country
FROM sh.customers
GROUP BY country_id, cust_state_province_id;

27-- Find customers whose credit limit is above the 90th percentile of their income level.

SELECT *
FROM (
    SELECT
        cust_id,
        income_level,
        cust_credit_limit,
        PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY cust_credit_limit) OVER (PARTITION BY income_level) AS percentile_90
    FROM sh.customers
)
WHERE cust_credit_limit > percentile_90;

28-- Display top 3 and bottom 3 customers per country by credit limit.

SELECT *
FROM (
    SELECT
        cust_id,
        country_id,
        cust_credit_limit,
        ROW_NUMBER() OVER (PARTITION BY country_id ORDER BY cust_credit_limit DESC) AS rn_top,
        ROW_NUMBER() OVER (PARTITION BY country_id ORDER BY cust_credit_limit ASC) AS rn_bottom
    FROM sh.customers
)
WHERE rn_top <= 3 OR rn_bottom <= 3;

29-- Calculate rolling sum of 5 customers’ credit limit within each country.
SELECT
    cust_id,
    country_id,
    cust_credit_limit,
    SUM(cust_credit_limit) OVER (
        PARTITION BY country_id
        ORDER BY cust_id
        ROWS BETWEEN 4 PRECEDING AND CURRENT ROW
    ) AS rolling_sum_5
FROM sh.customers;

30-- For each marital status, display the most and least wealthy customers using analytical functions.

SELECT *
FROM (
    SELECT
        cust_id,
        cust_marital_status,
        cust_credit_limit,
        RANK() OVER (PARTITION BY cust_marital_status ORDER BY cust_credit_limit DESC) AS rank_most_wealthy,
        RANK() OVER (PARTITION BY cust_marital_status ORDER BY cust_credit_limit ASC) AS rank_least_wealthy
    FROM sh.customers
)
WHERE rank_most_wealthy = 1 OR rank_least_wealthy = 1;