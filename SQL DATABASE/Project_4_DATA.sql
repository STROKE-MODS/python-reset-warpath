-- CREATION OF USERS TABLE
create table users(
 user_ID INTEGER PRIMARY KEY,
 username TEXT,
 Email TEXT,
 Phone INTEGER,
 Signup_Date DATE);

-- CREATION OF ORDERS TABLE
create table orders(
 Order_ID INTEGER PRIMARY KEY,
 User_ID INTEGER,
 Product TEXT,
 Order_Date DATE);


-- DATA IN USERS
insert into users(user_ID,username,Email,Phone,Signup_Date) values
 (1,'John','john@mail.com',1111111111,'2023-01-01'),
 (2,'Emma','emma@mail.com',222222222222,'2023-02-15'),
 (3,'John_D','john@mail.com',NULL,'2024-01-10'),
 (4,'JohnX','johnx@mail.com',1111111111,'2024-02-20');

-- DATA IN ORDERS
insert into orders(Order_ID,User_ID,Product,Order_Date) values
 (101,1,'Laptop','2023-05-10'),
 (102,3,'Mouse','2024-01-15'),
 (103,4,'Keyboard','2024-03-01');
