CREATE TABLE student(roll int primary key,names char(20),marks int, address char(50), age int);
INSERT INTO student values(1,"Eshika",100,"Mumbai",18);
INSERT INTO student values(2,"Kashish",100,"Delhi",18);
INSERT INTO student values(3,"Taniksha",100,"Delhi",17);
INSERT INTO student values(4,"Sneha",null,"Mumbai",19);
SELECT * FROM student;


CREATE TABLE Employee(emp_id int primary key, names char(20),salary int);
INSERT INTO Employee values(1001, "Eshika", 2000);
INSERT INTO Employee values(1002, "Kashish", 2400);
INSERT INTO Employee values(1003, "Taniksha", 3000);
SELECT * FROM Employee;


SELECT * FROM student INNER JOIN Employee where Employee.names=student.names;


SELECT COUNT(names) FROM student;
SELECT AVG(salary) FROM Employee;
SELECT MIN(salary) FROM Employee;
SELECT MAX(salary) FROM Employee;


SELECT * FROM Employee WHERE salary BETWEEN 2000 AND 2400 AND emp_id BETWEEN 1001 AND 1002;


SELECT emp_id,names FROM Employee WHERE names LIKE "_sh%";


SELECT names FROM student WHERE address="Mumbai";


SELECT names,salary FROM Employee ORDER BY salary;


SELECT * FROM student WHERE names IN("Kashish","Taniksha");


SELECT * FROM student WHERE address="Mumbai" OR age=17;


SELECT * FROM student WHERE NOT marks="null";


SELECT names,salary FROM Employee ORDER BY names DESC;


SELECT count(address),address FROM student GROUP BY address; 


SELECT age,count(names) FROM student GROUP BY age HAVING age=18;


CREATE TABLE bank(ID int primary key, Amount int, Mode char(20));
INSERT INTO bank values(1,60,"Cash");
INSERT INTO bank values(2,30,"Credit card");
INSERT INTO bank values(3,90,"Credit card");
INSERT INTO bank values(4,40,"Debit card");
INSERT INTO bank values(5,70,"Mobile payment");
INSERT INTO bank values(6,20,"Cash");
SELECT * FROM bank;


SELECT Mode, sum(Amount) as Total FROM bank GROUP BY Mode;


SELECT Mode, sum(Amount) as Total FROM bank GROUP BY Mode HAVING sum(Amount)>=80;


CREATE TABLE Employees(Employee_ID int primary key,Name char(50),Gender char,Department char(50),Education char(50),Month_of_Joining char(50),Salary int);
INSERT INTO Employees values(1001,"Ajay","M","Engineering","Doctoral","January",25);
INSERT INTO Employees values(1002,"Babloo","M","Engineering","UG","February",23);
INSERT INTO Employees values(1003,"Chhavi","F","HR","PG","March",15);
INSERT INTO Employees values(1004,"Dheeraj","M","HR","UG","January",12);
INSERT INTO Employees values(1005,"Evina","F","Marketing","UG","March",16);
INSERT INTO Employees values(1006,"Fredy","M","Sales","UG","December",10);
INSERT INTO Employees values(1007,"Garima","F","Sales","PG","March",10);
INSERT INTO Employees values(1008,"Hans","M","Admin","PG","November",8);
INSERT INTO Employees values(1009,"Ivanka","F","Admin","Intermediate","April",7);
INSERT INTO Employees values(1010,"Jai","M","Peon","High School","December",4);




SELECT Department,SUM(salary) FROM Employees WHERE NOT Education="UG" GROUP BY Department HAVING SUM(salary)>=20;


SELECT Department,SUM(salary) AS Total FROM Employees GROUP BY Department HAVING Total>=15 ORDER BY Total DESC;


SELECT Department,AVG(salary) FROM Employees GROUP BY Department HAVING AVG(salary)>35;


SELECT Name FROM Employees WHERE Salary BETWEEN 14 AND 24;


UPDATE Employees set Salary = Salary + 5 ;
SELECT Salary FROM Employees;