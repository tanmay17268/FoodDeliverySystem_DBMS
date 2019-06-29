import mysql.connector
import random



db = mysql.connector.connect(
     host = "localhost",
     user = "root",
     password = "tanmay28",
     database = "swaggy"
     )


cursor = db.cursor()

cursor.execute('''
    INSERT INTO `CART` (`Total_Amount`)
    VALUES (100)
    ''')

cursor.execute('''
    INSERT INTO `CART` (`Total_Amount`)
    VALUES (200)
    ''')

cursor.execute('''
    INSERT INTO `CART` (`Total_Amount`)
    VALUES (400)
    ''')

cursor.execute('''
    INSERT INTO `CART` (`Total_Amount`)
    VALUES (500)
    ''')

cursor.execute('''
    INSERT INTO `CART` (`Total_Amount`)
    VALUES (300)
    ''')

db.commit()

cursor.execute('''
	INSERT INTO `CUSTOMER` (`Name`, `Address`, `Cart_id`)
	VALUES ('Madhav', 'Colony A', 1)
	''')

cursor.execute('''
	INSERT INTO `CUSTOMER` (`Name`, `Address`, `Cart_id`)
	VALUES ('Tanmay', 'Colony B', 2)
	''')

cursor.execute('''
	INSERT INTO `CUSTOMER` (`Name`, `Address`, `Cart_id`)
	VALUES ('Raj', 'Colony C', 3)
	''')

cursor.execute('''
	INSERT INTO `CUSTOMER` (`Name`, `Address`, `Cart_id`)
	VALUES ('Sanjay', 'Colony D', 4)
	''')

cursor.execute('''
	INSERT INTO `CUSTOMER` (`Name`, `Address`, `Cart_id`)
	VALUES ('Dhruv', 'Colony B', 5)
	''')

db.commit()

cursor.execute('''
	INSERT INTO `CUSTOMER_PHONE` (`Customer_id`, `Phone_Number`)
	VALUES (1, '1234567890')
	''')
cursor.execute('''
	INSERT INTO `CUSTOMER_PHONE` (`Customer_id`, `Phone_Number`)
	VALUES (2, '2134567890')
	''')
cursor.execute('''
	INSERT INTO `CUSTOMER_PHONE` (`Customer_id`, `Phone_Number`)
	VALUES (3, '3214567890')
	''')
cursor.execute('''
	INSERT INTO `CUSTOMER_PHONE` (`Customer_id`, `Phone_Number`)
	VALUES (4, '4231567890')
	''')
cursor.execute('''
	INSERT INTO `CUSTOMER_PHONE` (`Customer_id`, `Phone_Number`)
	VALUES (5, '5234167890')
	''')


db.commit()

cursor.execute('''
	INSERT INTO `FOOD_ITEM` (`Item_name`, `Description`, `Price`)
	VALUES ('Dal Makhni', 'Tasty', 250)
	''')
cursor.execute('''
	INSERT INTO `FOOD_ITEM` (`Item_name`, `Description`, `Price`)
	VALUES ('Shahi Paneer', 'Delicious', 350)
	''')
cursor.execute('''
	INSERT INTO `FOOD_ITEM` (`Item_name`, `Description`, `Price`)
	VALUES ('Soya Chaap', 'Savoury', 300)
	''')
cursor.execute('''
	INSERT INTO `FOOD_ITEM` (`Item_name`, `Description`, `Price`)
	VALUES ('Aloo Pakora', 'Popular', 120)
	''')
cursor.execute('''
	INSERT INTO `FOOD_ITEM` (`Item_name`, `Description`, `Price`)
	VALUES ('Gobi Parantha', 'Must-have', 70)
	''')

db.commit()

cursor.execute('''
	INSERT INTO `CHEF` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('CHEFA', 'MIDA', 'SURA', '1234567891', 'male', 'ADDA', 1000, '1999-04-09')
	''')

cursor.execute('''
	INSERT INTO `CHEF` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('CHEFB', 'MIDB', 'SURB', '1234567892', 'female', 'ADDB', 2000, '1999-04-10')
	''')
cursor.execute('''
	INSERT INTO `CHEF` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('CHEFC', 'MIDC', 'SURC', '1234567893', 'male', 'ADDC', 1000, '1999-04-11')
	''')
cursor.execute('''
	INSERT INTO `CHEF` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('CHEFD', 'MIDD', 'SURD', '1234567894', 'female', 'ADDD', 4000, '1999-04-12')
	''')
cursor.execute('''
	INSERT INTO `CHEF` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('CHEFE', 'MIDE', 'SURE', '1234567895', 'male', 'ADDE', 3000, '1999-04-13')
	''')

db.commit()

cursor.execute('''
	INSERT INTO `DELIVERY_BOY` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('DBA', 'DMIDA', 'DSURA', '9876543211', 'male', 'DADDA', 500, '1999-04-09')
	''')
cursor.execute('''
	INSERT INTO `DELIVERY_BOY` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('DBB', 'DMIDB', 'DSURB', '9876543212', 'male', 'DADDB', 1500, '1999-04-10')
	''')
cursor.execute('''
	INSERT INTO `DELIVERY_BOY` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('DBC', 'DMIDC', 'DSURC', '9876543213', 'female', 'DADDC', 1200, '1999-04-11')
	''')
cursor.execute('''
	INSERT INTO `DELIVERY_BOY` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('DBD', 'DMIDD', 'DSURD', '9876543214', 'female', 'DADDD', 1700, '1999-04-12')
	''')
cursor.execute('''
	INSERT INTO `DELIVERY_BOY` (`First_Name`, `Middle_Name`, `Last_Name`, `Phone_Number`, `Sex`, `Address`, `Salary`, `DOB`)
	VALUES ('DBE', 'DMIDE', 'DSURE', '9876543215', 'female', 'DADDE', 800, '1999-04-13')
	''')

db.commit()

cursor.execute('''
	INSERT INTO `ORDERS` (`Order_Date`, `Order_Time`, `Total_Price`, `Status`, `Customer_id`, `Chef_id`, `DeliveryBoy_id`)
	VALUES ('2019-04-13', '10:00:00', 2000, 'getting prepared', 1, 2, 3)
	''')
cursor.execute('''
	INSERT INTO `ORDERS` (`Order_Date`, `Order_Time`, `Total_Price`, `Status`, `Customer_id`, `Chef_id`, `DeliveryBoy_id`)
	VALUES ('2019-04-14', '11:00:00', 1000, 'out for delivery', 3, 4, 1)
	''')
cursor.execute('''
	INSERT INTO `ORDERS` (`Order_Date`, `Order_Time`, `Total_Price`, `Status`, `Customer_id`, `Chef_id`, `DeliveryBoy_id`)
	VALUES ('2019-04-15', '12:00:00', 500, 'cancelled', 5, 3, 4)
	''')
cursor.execute('''
	INSERT INTO `ORDERS` (`Order_Date`, `Order_Time`, `Total_Price`, `Status`, `Customer_id`, `Chef_id`, `DeliveryBoy_id`)
	VALUES ('2018-04-16', '13:00:00', 1000, 'delivered', 4, 5, 2)
	''')
cursor.execute('''
	INSERT INTO `ORDERS` (`Order_Date`, `Order_Time`, `Total_Price`, `Status`, `Customer_id`, `Chef_id`, `DeliveryBoy_id`)
	VALUES ('2018-04-17', '14:00:00', 3000, 'delivered', 2, 2, 5)
	''')

db.commit()

cursor.execute('''
	INSERT INTO `DELIVERS_TO` (`Customer_id`, `DeliveryBoy_id`)
	VALUES (1, 5)
	''')

cursor.execute('''
	INSERT INTO `DELIVERS_TO` (`Customer_id`, `DeliveryBoy_id`)
	VALUES (4, 3)
	''')
cursor.execute('''
	INSERT INTO `DELIVERS_TO` (`Customer_id`, `DeliveryBoy_id`)
	VALUES (5, 4)
	''')
cursor.execute('''
	INSERT INTO `DELIVERS_TO` (`Customer_id`, `DeliveryBoy_id`)
	VALUES (2, 2)
	''')
cursor.execute('''
	INSERT INTO `DELIVERS_TO` (`Customer_id`, `DeliveryBoy_id`)
	VALUES (3, 1)
	''')

db.commit()

cursor.execute('''
	INSERT INTO `CART_CONTENTS` (`Cart_id`, `Item_id`, `Quantity`)
	VALUES (1, 5, 1)
	''')
cursor.execute('''
	INSERT INTO `CART_CONTENTS` (`Cart_id`, `Item_id`, `Quantity`)
	VALUES (2, 3, 10)
	''')
cursor.execute('''
	INSERT INTO `CART_CONTENTS` (`Cart_id`, `Item_id`, `Quantity`)
	VALUES (4, 4, 7)
	''')
cursor.execute('''
	INSERT INTO `CART_CONTENTS` (`Cart_id`, `Item_id`, `Quantity`)
	VALUES (5, 1, 7)
	''')
cursor.execute('''
	INSERT INTO `CART_CONTENTS` (`Cart_id`, `Item_id`, `Quantity`)
	VALUES (3, 2, 8)
	''')

db.commit()


cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (1, 4, 2)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (1, 3, 2)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (2, 5, 11)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (2, 3, 11)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (3, 2, 3)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (3, 3, 3)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (4, 1, 4)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (4, 3, 4)
	''')
cursor.execute('''
	INSERT INTO `ORDER_CONTENTS` (`Order_id`, `Item_id`, `Quantity`)
	VALUES (5, 3, 3)
	''')

db.commit()

print("Added data successfully")