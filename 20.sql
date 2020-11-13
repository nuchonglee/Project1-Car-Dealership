--1. 
INSERT INTO customer(ct_name,ct_address,ct_email,ct_password) VALUES(Jim, 124 2nd Street, kennen35@hotmail.com, 5D4R3);
--2. Input
INSERT INTO car(c_custkey,c_price,c_brand,c_year,c_titlestatue,c_milage,c_color) VALUES(35, 39000, 'Subaru', 2000, 'clean', 99534, 'silver');
--3. Input
INSERT INTO services(s_price,s_date,s_term,s_type,s_repair,s_workorder) VALUES(535,'2000-04-04','confirm','oil change','no','no ordering of new parts');
--4. 
INSERT INTO rental(r_price,r_pdate,r_ddate) VALUES(300,'2000-01-02','2000-01-03');
--5. 
INSERT INTO sales(sp_name) VALUES('Jack');
--6. 
INSERT INTO branch(b_custkey,b_carkey,b_serkey,b_salekey,b_rentkey,b_location) VALUES(35,68,0,0,0,'Fresno');

--7.
update customer
set ct_email = 'reprouced123@yahoo.com', ct_password = '12345'
where ct_name = 'Jim'

--8. 
update car
set c_milage = 2000, c_titlestatue = junk
where c_custkey = 34 

select *
from car
where c_custkey = 34

--9. 
update services
set s_term = 'confirm', s_date = '2000-01-19'
where s_serkey = 50

select * from services where s_serkey = 50 

--10. 
update sales
set sp_name = 'Jack' 
where sp_salekey = 34

select * from sales where sp_name = 'Jack'

--11. 
select * from rental where r_price < 3000

update rental
set r_price = 3000 
where r_price > 2000

--12. 
update branch
set b_location = 'Merced' 
where b_carkey = 95  AND b_custkey = 46
--13. 
delete from customer where ct_name = 'Jim' and ct_custkey = 3
--14. 
delete from car where c_carkey = 34 and c_custkey = 38
--15. 
select ct_custkey, s_serkey, s_price,s_date,s_term,s_type,s_repair,s_workorder
                from customer, branch, services
                where ct_custkey = 34
                    AND ct_custkey = b_custkey
                    AND b_serkey = s_serkey
--16. 
select ct_custkey, b_location, b_salekey, sp_name
                from customer, branch, sales
                where ct_custkey = 35
                    AND ct_custkey = b_custkey
                    AND b_serkey = sp_salekey
--17. 
delete from rental where r_pdate LIKE '%2000-1%'
--18. 
delete from branch where b_location = 'Scaramento'
--19. 
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

--20. 
select b_custkey, b_carkey, c_brand, c_year, s_price, s_type, s_date, s_term
from customer, branch, services, car
where ct_custkey = b_custkey
    AND b_serkey = s_serkey
    AND b_carkey = c_carkey
    AND c_year < 1910
group by s_price
order by s_price desc