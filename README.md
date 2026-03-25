# Cloud Kitchen Management System

A command-line based restaurant management system built with Python and MySQL.

## About

This project was built as a CBSE Class 12 Computer Science project. It simulates a cloud kitchen ordering system with separate portals for admins and customers. A cloud kitchen is a delivery-only commercial kitchen with no dine-in customers.

## Features

**Admin Portal**
- Add new dishes to the menu
- Update dish prices
- Delete dishes from the menu
- Display all menu items
- Change admin password

**Customer Portal**
- View available menu items
- Add items to cart
- Remove items from cart
- Proceed to payment and view bill

## Tech Stack

- Python 3
- MySQL
- mysql.connector
- Tabulate

## How to Run

1. Make sure MySQL is installed and running on your system
2. Install the required libraries:
   ```
   pip install mysql-connector-python tabulate
   ```
3. Update the MySQL credentials in the script:
   ```python
   con = mycon.connect(host="localhost", user="root", passwd="YOUR_PASSWORD")
   ```
4. Run the script:
   ```
   python cloud_kitchen.py
   ```
5. Default admin password is `123hello`

## Menu

The system comes pre-loaded with 31 dishes including starters, mains, beverages, and desserts.

## Project Structure

```
Cloud-Kitchen-Management-System/
│
├── cloud_kitchen.py     # Main application file
└── README.md            # Project documentation
```

## Author

Yohan George Kottoor
Class 12A, The Choice School
CBSE Computer Science Project
