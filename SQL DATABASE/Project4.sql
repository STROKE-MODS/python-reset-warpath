PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users(
 user_ID INTEGER PRIMARY KEY,
 username TEXT,
 Email TEXT,
 Phone INTEGER,
 Signup_Date DATE);
INSERT INTO users VALUES(1,'John','john@mail.com',1111111111,'2023-01-01');
INSERT INTO users VALUES(2,'Emma','emma@mail.com',222222222222,'2023-02-15');
CREATE TABLE orders(
 Order_ID INTEGER PRIMARY KEY,
 User_ID INTEGER,
 Product TEXT,
 Order_Date DATE);
INSERT INTO orders VALUES(101,1,'Laptop','2023-05-10');
INSERT INTO orders VALUES(102,1,'Mouse','2024-01-15');
INSERT INTO orders VALUES(103,1,'Keyboard','2024-03-01');
COMMIT;
