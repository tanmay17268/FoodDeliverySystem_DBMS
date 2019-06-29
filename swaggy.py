import mysql.connector

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "tanmay28",
	database = "swaggy"
	)

cursor = db.cursor()

cursor.execute('''
	CREATE TABLE CART (
	Cart_id INT AUTO_INCREMENT PRIMARY KEY,
	Total_Amount INT NOT NULL )
	''')

cursor.execute('''
	CREATE TABLE CUSTOMER(
	Customer_id INT AUTO_INCREMENT PRIMARY KEY,
	Name VARCHAR(50) NOT NULL,
	Address VARCHAR(255) NOT NULL,
	Cart_id INT NOT NULL UNIQUE,
	FOREIGN KEY(Cart_id) references CART(Cart_id) )
	''')

cursor.execute('''
	CREATE TABLE CUSTOMER_PHONE (
	Customer_id INT,
	FOREIGN KEY(Customer_id) references CUSTOMER(Customer_id),
	Phone_Number CHAR(10),
	PRIMARY KEY (Customer_id, Phone_Number) )
	''')

cursor.execute('''
	CREATE TABLE FOOD_ITEM (
	Item_id INT AUTO_INCREMENT PRIMARY KEY,
	Item_name VARCHAR(50) NOT NULL,
	Description VARCHAR(250),
	Price INT NOT NULL )
	''')

cursor.execute('''
	CREATE TABLE CHEF (
	Chef_id INT AUTO_INCREMENT PRIMARY KEY,
	First_Name VARCHAR(50) NOT NULL,
	Middle_Name VARCHAR(50),
	Last_Name VARCHAR(50),
	Phone_Number CHAR(10) NOT NULL,
	Sex ENUM('male', 'female') NOT NULL,
	Address VARCHAR(50) NOT NULL,
	Salary INT NOT NULL,
	DOB DATE NOT NULL )
	''')

cursor.execute('''
	CREATE TABLE DELIVERY_BOY (
	DeliveryBoy_id INT AUTO_INCREMENT PRIMARY KEY,
	First_Name VARCHAR(50) NOT NULL,
	Middle_Name VARCHAR(50),
	Last_Name VARCHAR(50),
	Phone_Number CHAR(10) NOT NULL,
	Sex ENUM('male', 'female') NOT NULL,
	Address VARCHAR(50) NOT NULL,
	Salary INT NOT NULL,
	DOB DATE NOT NULL )
	''')

cursor.execute('''
	CREATE TABLE ORDERS (
	Order_id INT AUTO_INCREMENT PRIMARY KEY,
	Order_Date DATE NOT NULL,
	Order_Time TIME NOT NULL,
	Total_Price INT NOT NULL,
	Status ENUM('getting prepared', 'cancelled', 'out for delivery', 'delivered'),
	Customer_id INT NOT NULL,
	Chef_id INT NOT NULL,
	DeliveryBoy_id INT NOT NULL,
	FOREIGN KEY(Customer_id) references CUSTOMER(Customer_id),
	FOREIGN KEY(Chef_id) references CHEF(Chef_id),
	FOREIGN KEY(DeliveryBoy_id) references DELIVERY_BOY(DeliveryBoy_id) )
	''')

cursor.execute('''
	CREATE TABLE DELIVERS_TO (
	Customer_id INT NOT NULL,
	FOREIGN KEY(Customer_id) references CUSTOMER(Customer_id),
	DeliveryBoy_id INT NOT NULL,
	FOREIGN KEY(DeliveryBoy_id) references DELIVERY_BOY(DeliveryBoy_id),
	Delivery_id INT AUTO_INCREMENT PRIMARY KEY )
	''')

cursor.execute('''
	CREATE TABLE CART_CONTENTS (
	Cart_id INT,
	FOREIGN KEY(Cart_id) references CART(Cart_id),
	Item_id INT,
	FOREIGN KEY(Item_id) references FOOD_ITEM(Item_id),
	Quantity INT NOT NULL,
	PRIMARY KEY(Cart_id, Item_id) )
	''')

cursor.execute('''
	CREATE TABLE ORDER_CONTENTS (
	Order_id INT,
	FOREIGN KEY(Order_id) references ORDERS(Order_id),
	Item_id INT,
	FOREIGN KEY(Item_id) references FOOD_ITEM(Item_id),
	Quantity INT NOT NULL,
	PRIMARY KEY(Order_id, Item_id) )
	''')

print("All tables created successfully")