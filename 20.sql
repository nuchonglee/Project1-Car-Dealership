--1. insert to customer
INSERT INTO customer(ct_name,ct_address,ct_email,ct_password) VALUES(Jim, 124 2nd Street, kennen35@hotmail.com, 5D4R3);
--2. insert to car
INSERT INTO car(c_custkey,c_price,c_brand,c_year,c_titlestatue,c_milage,c_color) VALUES(35, 39000, 'Subaru', 2000, 'clean', 99534, 'silver');
--3. insert to services
INSERT INTO services(s_price,s_date,s_term,s_type,s_repair,s_workorder) VALUES(535,'2000-04-04','confirm','oil change','no','no ordering of new parts');
--4. insert to rental
INSERT INTO rental(r_price,r_pdate,r_ddate) VALUES(300,'2000-01-02','2000-01-03');
--5. insert to sales
INSERT INTO sales(sp_name) VALUES('Jack');
--6. insert to branch
INSERT INTO branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) VALUES(35,68,0,0,0,'Fresno');

--7. update customer
update customer
set ct_email = 'reprouced123@yahoo.com', ct_password = '12345'
where ct_name = 'Jim'

--8. update car & select all customer key 34
update car
set c_milage = 2000, c_titlestatue = junk
where c_custkey = 34 

select *
from car
where c_custkey = 34

--9. update service and select all service key 50
update services
set s_term = 'confirm', s_date = '2000-01-19'
where s_serkey = 50

select * from services where s_serkey = 50 

--10. update sales and select all sale's name Jack
update sales
set sp_name = 'Jack' 
where sp_salekey = 34

select * from sales where sp_name = 'Jack'

--11. select all rental where price is less than 3000 and update price to 3000 where price is greater than 2 thousand
select * from rental where r_price < 3000

update rental
set r_price = 3000 
where r_price > 2000

--12. update branch 
update branch
set b_location = 'Merced' 
where b_carkey = 95  AND b_custkey = 46
--13. delete customer
delete from customer where ct_name = 'Jim' and ct_custkey = 3
--14. delete car
delete from car where c_carkey = 34 and c_custkey = 38
--15. select all serivce of customer key 34
select ct_custkey, s_serkey, s_price,s_date,s_term,s_type,s_repair,s_workorder
                from customer, branch, services
                where ct_custkey = 34
                    AND ct_custkey = b_custkey
                    AND b_serkey = s_serkey
--16. select locationt and sale name where customer key equal 35
select ct_custkey, b_location, b_salekey, sp_name
                from customer, branch, sales
                where ct_custkey = 35
                    AND ct_custkey = b_custkey
                    AND b_serkey = sp_salekey
--17. delete rental where year 2000 and month 1
delete from rental where r_pdate LIKE '%2000-1%'
--18. delete branch at location
delete from branch where b_location = 'Scaramento'
--19. Compare Honda bonded cars with all toytoa car
select Q1.c_price, Q1.c_brand, Q1.c_year, Q2.c_price, Q2.c_brand, Q2.c_year
from (select c_custkey, c_price,c_brand,c_year,c_titlestatue,c_milage,c_color,b_location
from car, branch
where c_brand = 'Honda'
    AND c_titlestatue = 'bonded'
group by c_year)Q1,
    (select c_custkey, c_price,c_brand,c_year,c_titlestatue,c_milage,c_color,b_location
from car, branch
where c_brand = 'Toyota'
group by c_year)Q2
group by Q1.c_year,Q2.c_year

--20. Select the top three cars that has a year less than 1910
select b_custkey, b_carkey, c_brand, c_year, s_price, s_type, s_date, s_term
from customer, branch, services, car
where ct_custkey = b_custkey
    AND b_serkey = s_serkey
    AND b_carkey = c_carkey
    AND c_year < 1910
group by s_price
order by s_price desc
limit 3