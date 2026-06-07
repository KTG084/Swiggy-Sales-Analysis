DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS menu;
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS users;


CREATE TABLE users(
    user_id VARCHAR(50)    PRIMARY KEY,
	user_name VARCHAR(100),
	age INT,
	gender VARCHAR(20),
	marital_status  VARCHAR(50),
	occupation  VARCHAR(100)
);


CREATE INDEX IF NOT EXISTS idx_users_age ON users(age);
CREATE INDEX IF NOT EXISTS idx_users_gender ON users(gender);
CREATE INDEX IF NOT EXISTS idx_users_occupation ON users(occupation);
CREATE INDEX IF NOT EXISTS idx_users_marital_status ON users(marital_status);



CREATE TABLE restaurants(
     restaurant_id       VARCHAR(50) PRIMARY KEY,
	 restaurant_name VARCHAR(100),
	 city      VARCHAR(80),
	 cuisine    VARCHAR(80),
	 rating        DECIMAL(2,1),
	 is_cloud_kitchen INT
);


CREATE INDEX IF NOT EXISTS idx_restaurants_city ON restaurants(city);
CREATE INDEX IF NOT EXISTS idx_restaurants_cuisine ON restaurants(cuisine);
CREATE INDEX IF NOT EXISTS idx_restaurants_rating ON restaurants(rating);
CREATE INDEX IF NOT EXISTS idx_restaurants_cloud_kitchen ON restaurants(is_cloud_kitchen);


CREATE TABLE menu(
     menu_id       VARCHAR(50) PRIMARY KEY,
	 restaurant_id VARCHAR(50),
	 item_name VARCHAR(100),
	 category VARCHAR(50),
	 price DECIMAL(10, 2),
	 is_veg  INT,

	 FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) on DELETE CASCADE
);


CREATE INDEX IF NOT EXISTS idx_menu_restaurant ON menu(restaurant_id);
CREATE INDEX IF NOT EXISTS idx_menu_category ON menu(category);
CREATE INDEX IF NOT EXISTS idx_menu_price ON menu(price);
CREATE INDEX IF NOT EXISTS idx_menu_is_veg ON menu(is_veg);



CREATE TABLE orders(
      order_id       VARCHAR(15)      PRIMARY KEY,
	  user_id          VARCHAR(50),
	  restaurant_id      VARCHAR(50),
	  order_date          DATE,
	  delivery_time        TIME,
	  order_status        VARCHAR(20),
	  payment_method      VARCHAR(30),
	  total_amount        DECIMAL(10, 2),


	  FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id) on DELETE CASCADE,
	  FOREIGN KEY (user_id) REFERENCES users(user_id) on DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_orders_user ON orders(user_id);
CREATE INDEX IF NOT EXISTS idx_orders_restaurant ON orders(restaurant_id);
CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date);
CREATE INDEX IF NOT EXISTS idx_orders_status ON orders(order_status);
CREATE INDEX IF NOT EXISTS idx_orders_payment ON orders(payment_method);
CREATE INDEX IF NOT EXISTS idx_orders_date_status ON orders(order_date, order_status);



CREATE TABLE IF NOT EXISTS order_items(
     order_item_id        VARCHAR(15) PRIMARY KEY,
	 order_id         VARCHAR(15),
	 menu_id             VARCHAR(15),
	 quantity            INT,
	 price                 DECIMAL(10, 2),


	 FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
	 FOREIGN KEY (menu_id) REFERENCES menu(menu_id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_order_items_order ON order_items(order_id);
CREATE INDEX IF NOT EXISTS idx_order_items_menu ON order_items(menu_id);
CREATE INDEX IF NOT EXISTS idx_order_items_order_menu ON order_items(order_id, menu_id)

















