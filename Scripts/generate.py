"""Optimized Synthetic Data Generator"""


import pandas as pd;
import numpy as np;
from datetime import datetime, timedelta 
import random
import warnings
warnings.filterwarnings('ignore')

# Make all random operations generate the same sequence every time the program runs, so results are reproducible and easier to debug.
np.random.seed(42)
random.seed(42)

NUM_USERS = 10000
NUM_RESTAURANTS = 1000
NUM_ORDERS = 600000
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2025, 12, 31)


print("=" * 80)
print("SWIGGY SALES ANALYSIS - OPTIMIZED DATA GENERATOR")
print("=" * 80)
print(f"\nConfiguration:")
print(f"  Users: {NUM_USERS:,}")
print(f"  Restaurants: {NUM_RESTAURANTS:,}")
print(f"  Orders: {NUM_ORDERS:,}")
print(f"  Date Range: {START_DATE.date()} to {END_DATE.date()}")
print("=" * 80)



print("\n[1/5] Generating Users data...")


def generate_user(num_users): 
    
    firstNames = [
        'Rahul', 'Priya', 'Amit', 'Sneha', 'Raj', 'Anjali', 'Vikram', 'Pooja',
        'Arjun', 'Neha', 'Karan', 'Divya', 'Rohan', 'Shreya', 'Aditya', 'Kavya',
        'Sanjay', 'Riya', 'Nikhil', 'Ananya', 'Manish', 'Sakshi', 'Varun', 'Nisha',
        'Akash', 'Megha', 'Siddharth', 'Isha', 'Vishal', 'Ritika', 'Gaurav', 'Simran',
        'Abhishek', 'Tanya', 'Harsh', 'Kriti', 'Deepak', 'Swati', 'Mohit', 'Pallavi'
    ]
    
    lastNames = [
        'Sharma', 'Gupta', 'Kumar', 'Singh', 'Patel', 'Reddy', 'Verma', 'Iyer',
        'Nair', 'Mehta', 'Agarwal', 'Joshi', 'Rao', 'Desai', 'Shahi', 'Malhotra',
        'Banerjee', 'Chatterjee', 'Das', 'Kulkarni', 'Pandey', 'Mishra', 'Chopra',
        'Kapoor', 'Bhat', 'Menon', 'Shetty', 'Pillai', 'Naidu', 'Ghosh'
    ]
    
    occupations = [
        'Software Engineer', 'Teacher', 'Doctor', 'Business Owner', 
        'Marketing Manager', 'Sales Executive', 'Student', 'Consultant',
        'Data Analyst', 'Graphic Designer', 'Accountant', 'HR Manager',
        'Civil Engineer', 'Architect', 'Lawyer', 'Freelancer',
        'Product Manager', 'Content Writer', 'Chef', 'Nurse'
    ]
    
    
    user_ids = [f'U{i:05d}' for i in range(1, num_users + 1)]
    user_names = [f"{random.choice(firstNames)} {random.choice(lastNames)}" for _ in range(num_users)]
    ages = np.random.randint(18, 65, num_users);
    genders = np.random.choice(['Male', 'Female'], num_users, p=[0.55, 0.45])
    marital_statuses = ['Married' if age > 28 and random.random() < 0.6 else 'Single' for age in ages]
    occupations_list = [random.choice(occupations) for _ in range (num_users)]
    
    
    return pd.DataFrame({
        "user_id" : user_ids,
        "user_name" : user_names,
        "age" : ages,
        "gender" : genders,
        "marital_status" : marital_statuses,
        "occupation" : occupations_list
    })
    
users_def = generate_user(NUM_USERS);
print(f"\nGenerated {len(users_def): } \n {users_def}")

print("\n[2/5] Generating Restaurants data...")

def generate_restro(num_restro):
    cities = ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 
                'Kolkata', 'Pune', 'Ahmedabad', 'Jaipur', 'Lucknow']
    
    cuisines = [
        'North Indian', 'South Indian', 'Chinese', 'Italian', 'Continental',
        'Fast Food', 'Biryani', 'Street Food', 'Desserts', 'Beverages',
        'Mexican', 'Thai', 'Japanese', 'Bakery', 'Cafe', 'Healthy Food',
        'Pizza', 'Burger', 'Seafood', 'Mughlai'
    ]
    
    restaurant_type = [
        'Spice', 'Kitchen', 'Cafe', 'Restaurant', 'Corner', 'Express',
        'Hub', 'Junction', 'Palace', 'Paradise', 'Delight', 'Station',
        'House', 'Point', 'Zone', 'Dhaba', 'Grill', 'Bistro'
    ]
    
    name_prefixes = [
        'Anand', 'Ravi', 'Priya', 'Mumbai', 'Delhi', 'Bangalore', 
        'Chennai', 'Royal', 'Golden', 'Urban', 'Fresh', 'Tasty',
        'Spicy', 'Classic', 'Modern', 'Grand', 'Elite', 'Premium'
    ]
    
    
    restaurant_ids = [f'R{i:04d}' for i in range(1, num_restro+1)]
    
    restaurant_names = [];
    
    for _ in range(num_restro) :
        if random.random() < 0.3:
            name =  random.choice(name_prefixes) + "'s " + random.choice(restaurant_type)
        else: 
            prefix =  random.choice(['The', 'Royal', 'Golden', 'Urban', 'Fresh', 
                                    'Tasty', 'Spicy', 'Classic', 'Modern', ''])
            suffix = random.choice(restaurant_type)
            name = f"{prefix} {suffix}".strip()
        restaurant_names.append(name)
        
    
    
    city_list = np.random.choice(cities, num_restro, 
                                p=[0.20, 0.18, 0.16, 0.12, 0.10, 
                                    0.08, 0.06, 0.04, 0.03, 0.03])
    
    cuisine_list = [random.choice(cuisines) for _ in range(num_restro)]
    
    ratings = np.random.choice([3.0, 3.5, 4.0, 4.5, 5.0, 2.5, 3.2, 3.8, 4.2, 4.7],
        num_restro,
        p=[0.05, 0.15, 0.25, 0.30, 0.10, 0.03, 0.04, 0.03, 0.03, 0.02])
    
    is_cloud_kitchen = np.random.choice([0,1] , num_restro, p=[0.7, 0.3])
    
    return pd.DataFrame({
        "restaurant_id" : restaurant_ids,
        "restaurant_names" : restaurant_names,
        "city": city_list,
        "cuisine": cuisine_list,
        "rating" : np.round(ratings, 1),
        "is_cloud_kitchen" : is_cloud_kitchen
        }
        
        
    )
    
restaurants_df = generate_restro(NUM_RESTAURANTS);
print(f"\nGenerated {len(restaurants_df): } \n{restaurants_df}")



print("\n[3/5] Generating Menu data...")


def generate_menu(restaurants_df):
        menuItems = {
        'Appetizer': ['Spring Rolls', 'Paneer Tikka', 'Chicken Wings', 'French Fries', 
                        'Garlic Bread', 'Veg Manchurian', 'Samosa', 'Pakora', 'Momos'],
        'Main Course': ['Butter Chicken', 'Dal Makhani', 'Paneer Butter Masala', 
                        'Chicken Biryani', 'Veg Biryani', 'Pasta', 'Fried Rice',
                        'Chicken Curry', 'Fish Curry', 'Egg Curry', 'Kadhai Paneer',
                        'Chole Bhature', 'Rajma Rice', 'Palak Paneer'],
        'Rice & Bread': ['Roti', 'Naan', 'Paratha', 'Jeera Rice', 'Steamed Rice',
                        'Garlic Naan', 'Butter Naan', 'Kulcha'],
        'Pizza': ['Margherita Pizza', 'Pepperoni Pizza', 'Veggie Pizza', 
                    'Chicken Pizza', 'Cheese Pizza', 'BBQ Chicken Pizza'],
        'Burger': ['Veg Burger', 'Chicken Burger', 'Cheese Burger', 
                    'Aloo Tikki Burger', 'Paneer Burger'],
        'Dessert': ['Ice Cream', 'Gulab Jamun', 'Brownie', 'Cake', 
                    'Rasmalai', 'Kulfi', 'Pastry'],
        'Beverage': ['Soft Drink', 'Fresh Juice', 'Lassi', 'Milkshake', 
                    'Coffee', 'Tea', 'Mojito', 'Smoothie']
    }
        
        
        vegItems = {
        'Paneer Tikka', 'French Fries', 'Garlic Bread', 'Veg Manchurian', 
        'Samosa', 'Pakora', 'Dal Makhani', 'Paneer Butter Masala', 
        'Veg Biryani', 'Pasta', 'Fried Rice', 'Kadhai Paneer', 'Chole Bhature', 
        'Rajma Rice', 'Palak Paneer', 'Roti', 'Naan', 'Paratha', 'Jeera Rice', 
        'Steamed Rice', 'Garlic Naan', 'Butter Naan', 'Kulcha', 
        'Margherita Pizza', 'Veggie Pizza', 'Cheese Pizza', 'Veg Burger', 
        'Cheese Burger', 'Aloo Tikki Burger', 'Paneer Burger', 'Ice Cream', 
        'Gulab Jamun', 'Brownie', 'Cake', 'Rasmalai', 'Kulfi', 'Pastry',
        'Soft Drink', 'Fresh Juice', 'Lassi', 'Milkshake', 'Coffee', 'Tea', 
        'Mojito', 'Smoothie'
    }
        
        all_items = [];
        menu_id = 1;
        
        for _, restaurant in restaurants_df.iterrows():
            
            num_items = random.randint(12, 25);
            selected = set();
            
            
            for _ in range(num_items):
                category = random.choice(list(menuItems.keys()))
                item = random.choice(menuItems[category])
                
                if(category, item) in selected: 
                    continue
                selected.add((category, item))
                
                
                
                if category in ['Appetizer', 'Rice & Bread']: 
                    price = random.uniform(50, 200)
                elif category == 'Main Course':
                    price = random.uniform(150, 450)
                elif category in ['Pizza', 'Burger']:
                    price = random.uniform(100, 350)
                elif category == 'Dessert':
                    price = random.uniform(50, 180)
                else:
                    price = random.uniform(30, 150)
                    
                if restaurant['rating'] >= 4.5 :
                    price *= 1.2
                    
                if item in ['Spring Rolls', 'Momos']:
                    isVeg = random.choice([0,1]);
                elif item in vegItems:
                    isVeg = 1;
                else:
                    isVeg = 0;
                    
                
                
                all_items.append({
                    "menu_id" : f'M{menu_id:06d}',
                    'restaurant_id': restaurant['restaurant_id'],
                    'item_name': item,
                    'category' : category,
                    'price' : round(price, 2),
                    'is_veg' : isVeg
                })
                
                menu_id += 1;
                
        return pd.DataFrame(all_items);
    
menu_df = generate_menu(restaurants_df)
print(f"Generated {len(menu_df)} \n{menu_df}" )
                    
            
print("\n[4/5] Generating Orders data")

def generate_orders(num_orders, users_df, restaurants_df, start_date, end_date):
    user_ids = users_df['user_id'].values
    heavy_users = np.random.choice(user_ids, int(len(user_ids)*0.2), replace = False)
    restaurants_ids = restaurants_df['restaurant_id'].values
    
    days_diff = (end_date-start_date).days
    
    
    order_ids = [f'O{i:07d}' for i in range(1, num_orders+1)]
    
    user_selection = np.random.rand(num_orders)
    selected_users = np.where(user_selection<0.8, np.random.choice(heavy_users, num_orders),
                                                  np.random.choice(user_ids, num_orders))
    
    selected_restaurants = np.random.choice(restaurants_ids, num_orders)
    
    random_days = np.random.randint(0, days_diff+1, num_orders)
    order_dates = [start_date + timedelta(days=int(d)) for d in random_days]
    
    hour_probs = np.random.rand(num_orders)
    hours = np.where(hour_probs < 0.4,
                     np.random.randint(12, 15, num_orders),
                     np.where(hour_probs < 0.75,
                              np.random.randint(19, 23, num_orders),
                              np.random.randint(8, 24, num_orders)))
    
    minutes = np.random.randint(0, 60, num_orders)
    delivery_times = [f"{h:02d}:{m:02d}:00" for h, m in zip(hours, minutes)]
    
    order_statuses = np.random.choice(['Delivered', 'Cancelled'], num_orders, p=[0.95, 0.05])
    
    payment_methods = np.random.choice(
        ['Credit Card', 'Debit Card', 'UPI', 'Cash on Delivery', 'Wallet'],
        num_orders,
        p=[0.25, 0.15, 0.40, 0.10, 0.10]
    )
    
    
    return pd.DataFrame({
        'order_id' : order_ids,
        'user_id': selected_users,
        'restaurant_id': selected_restaurants,
        'order_date': [d.strftime('%Y-%m-%d') for d in order_dates],
        'delivery_time': delivery_times,
        'order_status': order_statuses,
        'payment_method': payment_methods,
        'total_amount': 0
    })
    
orders_df = generate_orders(NUM_ORDERS, users_def, restaurants_df, START_DATE, END_DATE )
print(f"Generated {len(orders_df)} \n{orders_df}")


print("\n[5/5] Generating Order Items and calculating totals...")

def generate_order_items(orders_df, menu_df):
    all_items = []
    order_totals = {}
    item_id = 1;
    
    menu_by_restaurants = {k: v for k, v in menu_df.groupby('restaurant_id')}
    
    batch_size = 50000
    total_batches = (len(orders_df) + batch_size -1) // batch_size
    
    for batch_num in range(total_batches):
        start_idx = batch_num * batch_size
        end_idx = min((batch_num + 1)* batch_size, len(orders_df))
        
        if batch_num % 5 == 0:
            print(f"Processing batch {batch_num + 1}/{total_batches}...", end ='\r')
            
        for idx in range(start_idx, end_idx):
            order = orders_df.iloc[idx]
            order_id = order['order_id']
            restaurant_id = order['restaurant_id']
            
            
            if restaurant_id not in menu_by_restaurants:
                continue
            
            
            restaurant_menu = menu_by_restaurants[restaurant_id]
            num_items = np.random.choice([1, 2, 3, 4, 5, 6], 
                                        p=[0.15, 0.30, 0.30, 0.15, 0.07, 0.03])
            
            selected = restaurant_menu.sample(min(num_items, len(restaurant_menu)))
            order_total = 0
            
            for _, menu_item in selected.iterrows():
                quantity = np.random.choice([1, 2, 3], p=[0.70, 0.25, 0.05])
                price = menu_item['price']
                order_total += price*quantity
                
                all_items.append({
                    'order_item_id': f'OI{item_id:08d}',
                    'order_id': order_id,
                    'menu_id' : menu_item['menu_id'],
                    'quantity': quantity,
                    'price' : price
                })
                
                item_id += 1
                
            order_totals[order_id] = round(order_total, 2)
    print()
    
    orders_df['total_amount'] = orders_df['order_id'].map(order_totals).fillna(0)
    
    return pd.DataFrame(all_items), orders_df

order_items_df, orders_df = generate_order_items(orders_df, menu_df)
print(f"Generated {len(order_items_df)} \n {order_items_df}")
            

print("\n" + "=" * 80)
print("SAVING DATA TO CSV FILES")
print("=" * 80)


users_def.to_csv('./Data/users.csv', index=False)
print("users.csv")

restaurants_df.to_csv('./Data/restaurants.csv', index=False)
print("restaurants.csv")

menu_df.to_csv('./Data/menu.csv', index=False)
print("menu.csv")

orders_df.to_csv('./Data/orders.csv', index=False)
print("orders.csv")

order_items_df.to_csv('./Data/order_items.csv', index=False)
print("order_items.csv")

print("\n" + "=" * 80)
print("ALL FILES SAVED SUCCESSFULLY!")
print("=" * 80)
