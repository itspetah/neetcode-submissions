-- Write your query below
select c.customer_id, c.customer_name
from customers c join orders o
on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name
having count(case when product_name = 'A' then 1 else null end) >0
and count(case when product_name = 'B' then 1 else null end) > 0
and count(case when product_name = 'C' then 1 else null end) = 0
order by c.customer_name