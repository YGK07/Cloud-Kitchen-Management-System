import mysql.connector as mycon
from tabulate import tabulate
print("____________________________________________________")
print(" Cloud kitchen Management System")
print("____________________________________________________")
con = mycon.connect(host="localhost", user="root", passwd="YOUR_PASSWORD")
mycursor=con.cursor()
mycursor.execute("create database cbse_project82446450013")
mycursor.execute("use cbse_project82446450013")
mycursor.execute("create table login(username varchar(25) not null,password varchar(25)
not null)")
mycursor.execute("create table purchase(name varchar(25) not null,dcode int not
null,amount int not null,quant int not null)")
mycursor.execute("create table menu(dcode int not null,dname varchar(25) not
null,quantity int not null ,price int not null)")
mycursor.execute("insert into menu values(1,'Chicken 65',10,120)")
mycursor.execute("insert into menu values(2,'Spinach Delight',10,90)")
mycursor.execute("insert into menu values(3,'Gobi Stirfry',10,70)")
mycursor.execute("insert into menu values(4,'Gobi Dryfry',10,130)")
mycursor.execute("insert into menu values(5,'Mutton Chaps',10,150)")
mycursor.execute("insert into menu values(6,'Shrimp Roast',10,100)")
mycursor.execute("insert into menu values(7,'Veg Tempura',10,110)")
mycursor.execute("insert into menu values(8,'Potato Wedges',10,80) ")
mycursor.execute("insert into menu values(9,'Gobi Manchurian',10,190)")
mycursor.execute("insert into menu values(10,'Paneer Butter Masala',10,220)")
mycursor.execute("insert into menu values(11,'Aloo Do Pyaza',10,180)")
mycursor.execute("insert into menu values(12,'Veg Noodles',10,190)")
mycursor.execute("insert into menu values(13,'Gaza Style Curry',10,220)")
mycursor.execute("insert into menu values(14,'Paneer Mothiawala',10,210)")
mycursor.execute("insert into menu values(15,'Chicken Patiala',10,240)")
mycursor.execute("insert into menu values(16,'Mutton Rogan Josh',25,400)")
mycursor.execute("insert into menu values(17,'Sulaimani',10,30)")
mycursor.execute("insert into menu values(18,'Rose Milk',10,70)")
mycursor.execute("insert into menu values(19,'Green Tea',10,70)")
mycursor.execute("insert into menu values(20,'Tea',10,30)")
mycursor.execute("insert into menu values(21,'Coffee',10,45)")
mycursor.execute("insert into menu values(22,'Cold Coffee',10,50)")
mycursor.execute("insert into menu values(23,'Cold Milo',10,100)")
mycursor.execute("insert into menu values(24,'Rose Falooda',10,120)")
mycursor.execute("insert into menu values(25,'Tofee pudding',10,130)")
mycursor.execute("insert into menu values(26,'Banoffee pie',10,140)")
mycursor.execute("insert into menu values(27,'Red Velvet',10,40)")
mycursor.execute("insert into menu values(28,'Caramel Sundae',10,140)")
mycursor.execute("insert into menu values(29,'Chocolate Mudcake',10,40)")
mycursor.execute("insert into menu values(30,'NewYork Cheesecake',10,180)")
mycursor.execute("insert into menu values(31,'Burnt Icecream',10,130)")
con.commit()
def ani():
dcode=int(input("Enter dish code:"))
dname=input("Enter dish name:")
quantity=int(input("Enter product quantity:"))
price=int(input("Enter dish price:"))
mycursor.execute(f"insert into menu values({dcode},'{dname}',{quantity},{price})")
con.commit()
print("Dish added successfully")
def up():
dcode1=int(input("Enter dish code:"))
new_price=int(input("Enter new price:"))
mycursor.execute(f"update menu set price={new_price} where dcode={dcode1}")
con.commit()
print("Dish updated successfully")
def dli():
dcode1=int(input("Enter dish code:"))
mycursor.execute(f"delete from menu where dcode={dcode1}")
con.commit()
print("Dish deleted successfully")
def dai():
mycursor.execute("select* from menu")
data=mycursor.fetchall()
key=['Dcode','Dname','Quantity','Price']
print(tabulate(data,headers=key,tablefmt='fancy_grid'))
def chps():
old_pass=input("Enter old password:")
mycursor.execute("select* from login")
for i in mycursor:
username,password=i
if old_pass==password:
new_pass=input("Enter new password:")
mycursor.execute(f"update login set password='{new_pass}'")
con.commit()
else:
print("Wrong password")
def itc():
while True:
tcode=int(input("Enter dish code:"))
quantity=int(input("Enter product quantity:"))
mycursor.execute(f"select* from menu where dcode={tcode}")
for i in mycursor:
n_code,n_name,n_quantity,n_price=i
amount=n_price*quantity
net_quantity=n_quantity-quantity
mycursor.execute(f"update menu set quantity={net_quantity} where dcode={tcode}")
mycursor.execute(f"insert into purchase values('{n_name}',{tcode},{amount},
{quantity})")
con.commit()
n=input("1.Do you want to add more items (Y/N):")
if n=='N' or n=='n':
break
def vai():
mycursor.execute("select* from menu")
data=mycursor.fetchall()
key=['Dcode','Dname','Quantity','Price']
print(tabulate(data,headers=key,tablefmt='fancy_grid'))
def pay():
mycursor.execute("select* from purchase")
data=mycursor.fetchall()
key=['Dname','Dcode','Total Price','Quantity']
print(" Cloud kitchen Management System")
print(tabulate(data,headers=key,tablefmt='fancy_grid'))
ans=input('Do you want to proceed to payment (Y/N):')
if ans=='N' or ans=='n':
s=input('Do you want to cancel any items from cart (Y/N):')
if s=='y' or s=='Y':
while True:
dcode1=int(input("Enter dish code:"))
mycursor.execute(f"delete from purchase where dcode={dcode1}")
con.commit()
u=input('Do you want to cancel any items from cart (Y/N):')
if u=='n' or u=='N':
break
else:
mycursor.execute("select sum(amount) from purchase")
for i in mycursor:
amount=i
print(" Total Amount to be paid:",amount[0])
break
z=0
mycursor.execute("select* from login")
data=mycursor.fetchall()
for i in data:
z+=1
if z==0:
mycursor.execute("insert into login values('yohan','123hello')")
con.commit()
while True:
print("1.Admin")
print("2.Customer")
print("3.Exit")
opt=int(input("Enter option:"))
if opt==1:
passwd=input("Enter password:")
mycursor.execute("select* from login")
for i in mycursor:
username,password=i
if passwd==password:
print("Password entered is correct")
o=1
while o==1:
print("1.Add new item")
print("2.Updating price")
print("3.Deleting Item")
print("4.Display All items")
print("5.To change the password")
print("6.Log out")
opt=int(input("Enter option:"))
if opt==1:
ch=1
while ch==1:
ani()
ch=int(input("1.If you want to add more dishes,2.If you dont want to add more dishes:"))
o=int(input("1.If you want to continue editing menu,2.if you want to exit:"))
elif opt==2:
ch=1
while ch==1:
up()
ch=int(input("1.If you want to update dishes,2.If you dont want to update more dishes:"))
o=int(input("1.If you want to continue editing menu,2.if you want to exit:"))
elif opt==3:
ch=1
while ch==1:
dli()
ch=int(input("1.If you want to delete more dishes,2.If you dont want to delete more dishes:"))o=int(input("1.If you want to continue editing menu,2.if you want to exit:"))
elif opt==4:
dai()
o=int(input("1.If you want to continue editing menu,2.if you want to exit:"))
elif opt==5:
chps()
elif opt==6:
break
else:
print("Wrong password")
elif opt==2:
while True:
print("1.View Available Items")
print("2.Enter The Items You want To Buy")
print("3.Payment")
print("4.Go back")
ch=int(input("Enter option:"))
if ch==1:
vai()
elif ch==2:
itc()
elif ch==3:
pay()
elif ch==4:
mycursor.execute('delete from purchase;')
con.commit()
break #Breaks from the inner loop and goes to the main loop
elif opt==3:
print('Thank You for visiting')
break
