DROP TABLE IF EXISTS orders_master;
CREATE TABLE orders_master AS 
WITH repeat_users AS (
     SELECT 
	       user_id,
		   COUNT(*) as total_orders
	 FROM orders
	 GROUP BY user_id
)
SELECT 
      o.order_id,
	  o.order_date,
	  o.delivery_time,
	  o.order_status,
	  o.payment_method,
	  o.total_amount,

	  o.user_id,
	  u.user_name,
	  u.age,
	  u.gender,
	  u.marital_status,
	  u.occupation,



	  CASE 
	       WHEN u.age < 18 THEN 'Under 18'
           WHEN u.age BETWEEN 18 AND 25 THEN '18-25'
           WHEN u.age BETWEEN 26 AND 35 THEN '26-35'
           WHEN u.age BETWEEN 36 AND 45 THEN '36-45'
           WHEN u.age BETWEEN 46 AND 55 THEN '46-55'
           WHEN u.age >= 56 THEN '56+'
		   ELSE 'Unknown'
	  END as age_group,

	  CASE 
	      WHEN ru.total_orders > 1 THEN TRUE
		  ELSE FALSE 
	  END AS is_repeat_customer,

	  o.restaurant_id,
	  r.restaurant_name,
	  r.city,
	  r.cuisine,
	  r.rating as restaurant_rating,


	  CASE 
	       WHEN r.is_cloud_kitchen = 1 THEN 'Cloud Kitchen'
		   ELSE 'Traditional'
	  END as restaurant_type,

	  EXTRACT (YEAR FROM o.order_date) as order_year,
	  EXTRACT (MONTH FROM o.order_date) as order_month,
	  EXTRACT (QUARTER FROM o.order_date) as order_quarter,
	  EXTRACT (DOW FROM o.order_date) as day_of_week,
	  CASE 
	      WHEN EXTRACT(DOW FROM o.order_date) IN (0,6) THEN 'Weekend'
		  ELSE 'Weekday'
	  END as day_type,

	  CASE 
	      WHEN EXTRACT(HOUR FROM o.delivery_time) BETWEEN 8 AND 11 THEN 'Breakfast'
		  WHEN EXTRACT(HOUR FROM o.delivery_time) BETWEEN 12 AND 14 THEN 'Lunch'
		  WHEN EXTRACT(HOUR FROM o.delivery_time) BETWEEN 15 AND 17 THEN 'Snack'
		  WHEN EXTRACT(HOUR FROM o.delivery_time) BETWEEN 18 AND 22 THEN 'Dinner'
		  ELSE 'Late Night'
	  END as time_slot
FROM orders o
INNER JOIN users U ON u.user_id = o.user_id
LEFT JOIN repeat_users ru ON o.user_id = ru.user_id
INNER JOIN restaurants r ON o.restaurant_id = r.restaurant_id;






DROP TABLE IF EXISTS order_items_master;
CREATE TABLE order_items_master AS 
SELECT 

	  oi.order_item_id,
	  oi.order_id,
	  oi.quantity,
	  m.price as menu_price,
	  (oi.quantity * m.price) as line_total,

	  oi.menu_id,
	  m.restaurant_id,
	  m.item_name,
	  m.category,


	  CASE 
	       WHEN m.is_veg = 1 THEN 'Veg'
		   ELSE 'Non-Veg'
	  END as item_type,


	  CASE 
	      WHEN m.price < 100 THEN 'Budget (<100)'
		  WHEN m.price < 200 THEN 'Economic(100-199)'
		  WHEN m.price < 200 THEN 'Mid-Range (200-299)'
		  WHEN m.price < 200 THEN 'Premium (300-399)'
		  ELSE 'Luxury (400+)'
	  END as price_category
FROM order_items oi
INNER JOIN menu m 
ON oi.menu_id = m.menu_id



	       
	  
