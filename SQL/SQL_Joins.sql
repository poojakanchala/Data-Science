-- Table t1: Customers
CREATE TABLE Customers (
    CustomerID NUMBER PRIMARY KEY,
    CustomerName VARCHAR2(50),
    Email VARCHAR2(50),
    City VARCHAR2(50),
    Country VARCHAR2(50)
);

-- Table t2: Products
CREATE TABLE Products (
    ProductID NUMBER PRIMARY KEY,
    ProductName VARCHAR2(50),
    Category VARCHAR2(30),
    Price NUMBER,
    CustomerID NUMBER
);



-- t1 
INSERT INTO Customers VALUES (1, 'John Smith', 'john.smith@gmail.com', 'New York', 'USA');
INSERT INTO Customers VALUES (2, 'Priya Sharma', 'priya.sharma@gmail.com', 'Delhi', 'India');
INSERT INTO Customers VALUES (3, 'Carlos Mendez', NULL, 'Madrid', 'Spain');
INSERT INTO Customers VALUES (4, 'Aisha Khan', 'aisha.khan@gmail.com', NULL, 'UAE');
INSERT INTO Customers VALUES (5, 'Liam Brown', 'liam.brown@gmail.com', 'London', NULL);

-- t2 
INSERT INTO Products VALUES (101, 'Laptop', 'Electronics', 850, 1);
INSERT INTO Products VALUES (102, 'Smartphone', 'Electronics', 500, 1);
INSERT INTO Products VALUES (103, 'Tablet', 'Electronics', 300, 2);
INSERT INTO Products VALUES (104, 'Headphones', 'Accessories', 100, NULL);
INSERT INTO Products VALUES (105, 'Watch', 'Accessories', 150, 3);
INSERT INTO Products VALUES (106, 'Camera', 'Electronics', 700, 2);
INSERT INTO Products VALUES (107, 'Shoes', 'Fashion', 80, 4);
INSERT INTO Products VALUES (108, 'Backpack', 'Fashion', NULL, 4);



---------------------------------------------------------
--1.INNER JOIN
---------------------------------------------------------
SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
INNER JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID;

---------------------------------------------------------
--2. LEFT JOIN (LEFT OUTER JOIN)
---------------------------------------------------------
SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
LEFT JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID;

---------------------------------------------------------
-- 3. RIGHT JOIN (RIGHT OUTER JOIN)
---------------------------------------------------------
SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
RIGHT JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID;

---------------------------------------------------------
-- 4.FULL OUTER JOIN
---------------------------------------------------------
SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
FULL OUTER JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID;

---------------------------------------------------------
-- 5️.SYMMETRIC DIFFERENCE (records not matching)
---------------------------------------------------------
SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
LEFT JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID
WHERE 
    t2.CustomerID IS NULL

UNION

SELECT 
    t1.CustomerID, 
    t1.CustomerName, 
    t2.ProductName, 
    t2.Price
FROM 
    Customers t1
RIGHT JOIN 
    Products t2
ON 
    t1.CustomerID = t2.CustomerID
WHERE 
    t1.CustomerID IS NULL;
