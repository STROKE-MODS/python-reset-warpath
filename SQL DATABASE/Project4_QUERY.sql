-- TO CHECK IF EMAIL IS COPIED
select Email,group_concat(Username,',') , count(*) 
from users group by Email;

-- TO CHECK IF PHONE NUMBER IS COPIED
select Phone,group_concat(Username,',')  
from users 
group by Phone;

-- TO CHECK WHICH USER ID IS ASIGN TO WHICH
select user_ID,Username 
from users;

-- TO UPDATE THE USER ID
update users set user_ID=1 
where user_ID IN (3,4);

-- TO DELETE COPIED ONES
delete from users where user_ID in (3,4);


-- TO UPDATE THE ORDERS
update orders set User_ID=1 
where User_ID in (3,4);


-- PROJECT TO CHECK IF ONE PERSON HAVE MADE MULTIPLE ACCOUNTS.