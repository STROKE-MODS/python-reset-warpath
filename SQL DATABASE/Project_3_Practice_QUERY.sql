-- To find users who signed up before or between the date
select u.Username from users as u
  where Signup_Date between '2024-05-30' and '2024-06-30';

-- List products prices between $10 and $50,sorted by price (low to high).
select p.Product_Name,p.Category from products as p
 where p.Price between 10 and 50
 order by p.Price asc;

-- Get orders that are not delivered(Status = Pending)
select u.Username,p.Product_Name,p.Category from Orders as o
 join users as u
 on o.User_ID=u.User_ID
 join Products as p
 on o.Product_ID=p.Product_ID
 where o.Status = 'Pending';

-- Count how many orders each customer made(show only customers with 5+ orders)
select u.Username,count(o.Order_ID) as Total_Orders
    from Users as u
    join Orders as o
    on u.User_ID=o.User_ID
    group by u.Username,u.User_ID
    having count(o.Order_ID)>=5;

-- Calculate the total revenue per product category.
select p.Category,(p.Product_ID*o.Quantity) as 'Revenue'
 from products as p
 join Orders as o
 on p.Product_ID=o.Product_ID
 group by p.Category;

-- Orders which had not been purchased even a single time
SELECT p.Product_ID, p.Product_Name 
FROM Products p
LEFT JOIN Orders o ON p.Product_ID = o.Product_ID
WHERE o.Product_ID IS NULL;

-- People who had orders more than the avg persons.
select u.Username from Orders as o
 join users as u
 on u.User_ID=o.User_ID
 join Products as p
 on p.Product_ID=o.Product_ID
 group by u.Username
 having sum(p.Price)>avg(p.Price);

-- Items having rating more than Average
select p.Product_Name,p.Category,p.Price,p.Rating 
   from Products as p
   where p.Rating>(select avg(Rating) from Products);

--Users deletion according to last date
delete from users 
    where Last_Login>'2024-06-28'
    or
    Last_Login is NULL;
  

