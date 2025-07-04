-- Table creation 

--USERS TABLE
create table users(
 User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
 Username TEXT,
 Signup_Date DATE,
 Last_Login DATE,
 Email TEXT);

--PRODUCTS TABLE
create table Products(
 Product_ID INTEGER PRIMARY KEY,
 Product_Name TEXT,
 Category TEXT,
 Price INTEGER,                                                                                                                                                                                                                     
 Rating INTEGER);

--ORDERS TABLE
create table Orders(
 Order_ID INTEGER PRIMARY KEY,
 User_ID INTEGER,
 Product_ID INTEGER,
 Order_Date DATE,
 Status TEXT,
 Quantity INTEGER);

-- EMPLOYEES TABLE
create table employees(
 emp_ID INTEGER,                                                                                              
 emp_name TEXT,                                                                                               
 Manager_ID INTEGER,                                                                                          
 Department TEXT);


-- DATA ENTRY FOR TABLES

--USERS
insert into users(User_ID,Username,Signup_Date,Last_Login,Email) values
 (1,'john','2024-05-01','2024-06-28','john@mail.com'),
 (2,'emma','2024-06-15','2024-06-30','emma@mail.com');
 insert into users(User_ID,Username,Signup_Date,Email) values
 (3,'alex','2023-12-10','alex@mail.com');

--PRODUCTS
insert into products(Product_ID,Product_Name,Category,Price,Rating) values
(101,'Wireless Mouse','Electronics',25.99,4.5),
(102,'Yoga Mat','Fitness',19.99,4.2),
(103,'Smartwatch','Electronics',89.99,3.8);

--ORDERS
insert into Orders (Order_ID,User_ID,Product_ID,Order_Date,Status,Quantity) values
(1001,1,101,'2024-06-10','Delivered',2),
(1002,1,102,'2024-06-15','Pending',1),
(1003,2,103,'2024-06-20','Delivered',1);

--EMPLOYEES
insert into employees(emp_ID,emp_name,Manager_ID,Department) values
 (501,'Alics',NULL,'CEO'),
 (502,'Bob',501,'Engineering'),
 (503,'Carol',502,'Engineering');

