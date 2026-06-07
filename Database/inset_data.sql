COPY users (user_id,user_name,age,gender,marital_status,occupation) 
FROM 'C:\Users\karan\OneDrive\Desktop\powerBI Data\SWIGGY SALES ANALYSIS\Data\users.csv'
DELIMITER ','
CSV
HEADER;



COPY restaurants (restaurant_id,restaurant_name,city,cuisine,rating,is_cloud_kitchen)
FROM 'C:\Users\karan\OneDrive\Desktop\powerBI Data\SWIGGY SALES ANALYSIS\Data\restaurants.csv'
DELIMITER ','
CSV
HEADER;


COPY menu (menu_id,restaurant_id,item_name,category,price,is_veg)
FROM 'C:\Users\karan\OneDrive\Desktop\powerBI Data\SWIGGY SALES ANALYSIS\Data\menu.csv'
DELIMITER ','
CSV
HEADER;

COPY orders (order_id,user_id,restaurant_id,order_date,delivery_time,
                    order_status,payment_method,total_amount)
FROM 'C:\Users\karan\OneDrive\Desktop\powerBI Data\SWIGGY SALES ANALYSIS\Data\orders.csv'
DELIMITER ','
CSV
HEADER;

COPY order_items (order_item_id,order_id,menu_id,quantity,price)
FROM  'C:\Users\karan\OneDrive\Desktop\powerBI Data\SWIGGY SALES ANALYSIS\Data\order_items.csv'
DELIMITER ','
CSV
HEADER;
