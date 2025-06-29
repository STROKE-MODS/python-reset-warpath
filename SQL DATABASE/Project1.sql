PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE students(
Roll_No INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,
Class TEXT);
INSERT INTO students VALUES(1,'Himanshu','12th');
INSERT INTO students VALUES(2,'Sambhav','12th');
INSERT INTO students VALUES(3,'Chinu','12th');
INSERT INTO students VALUES(4,'Amit','12th');
INSERT INTO students VALUES(5,'Rohit','12th');
INSERT INTO students VALUES(6,'Hello','12th');
CREATE TABLE Courses(
Course_ID INTEGER PRIMARY KEY,
Course_Name TEXT);
INSERT INTO Courses VALUES(1,'B.Tech');
INSERT INTO Courses VALUES(2,'Computer Science');
INSERT INTO Courses VALUES(3,'LLB');
INSERT INTO Courses VALUES(4,'CA');
INSERT INTO Courses VALUES(5,'Gaming');
INSERT INTO Courses VALUES(6,'Data Science');
CREATE TABLE Marks(
Roll_No INTEGER,
Course_ID INTEGER,
Marks INTEGER,
foreign key(Roll_No) references students(Roll_No),
foreign key(Course_ID) references Courses(Course_ID));
INSERT INTO Marks VALUES(1,1,92);
INSERT INTO Marks VALUES(2,2,95);
INSERT INTO Marks VALUES(3,3,89);
INSERT INTO Marks VALUES(4,4,85);
INSERT INTO Marks VALUES(5,5,86);
INSERT INTO Marks VALUES(6,NULL,92);
CREATE TABLE enrollments(
Roll_No INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT,
Course_ID INTEGER,
Course_Name TEXT,
foreign key (Roll_No) references students(Roll_No),
foreign key (Course_ID) references Courses(Course_ID),
foreign key (Course_Name) references Courses(Course_Name));
INSERT INTO enrollments VALUES(1,'Himanshu',1,'B.Tech');
INSERT INTO enrollments VALUES(2,'Sambhav',1,'B.Tech');
INSERT INTO enrollments VALUES(3,'Chinu',1,'B.Tech');
INSERT INTO enrollments VALUES(4,'Amit',6,'Data Science');
INSERT INTO enrollments VALUES(7,'Himanshu',6,'Data Science');
CREATE TABLE Teachers(
Name TEXT not null,
Course_ID INTEGER,
Course_Name TEXT,
foreign key (Course_ID) references Courses(Course_ID),
foreign key (Course_Name) references Courses(Course_Name));
INSERT INTO Teachers VALUES('Ms.Rekha',1,'B.Tech');
INSERT INTO Teachers VALUES('Mr.Rajeev',2,'Computer Scince');
INSERT INTO Teachers VALUES('Mr.Sandeep',3,'LLB');
INSERT INTO Teachers VALUES('Mr.Bansal',4,'CA');
INSERT INTO Teachers VALUES('Ms.Swati',5,'Gaming');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('students',6);
INSERT INTO sqlite_sequence VALUES('enrollments',7);
COMMIT;
