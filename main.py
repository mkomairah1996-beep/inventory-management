import os
import psycopg
from dotenv import load_dotenv
load_dotenv()
conn = psycopg.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password=os.environ["DB_PASSWORD"],
    port=5432
)

cursor = conn.cursor()

print("Inventory Management System")
print("Welcome to your inventory")

try:
    product_name = input("Enter product name: ").strip()
    sku = input("Enter SKU: ").strip()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

except ValueError:
    print("Invalid price or quantity")

else:
    valid = True

    if not product_name:
        print("Product name cannot be empty")
        valid = False
    elif not any(char.isalpha() for char in product_name):
        print("Product name must contain at least one letter")
        valid = False

    if not sku:
        print("SKU cannot be empty")
        valid = False

    if price <= 0:
        print("Price rejected")
        valid = False
    else:
        print("Price accepted")

    if quantity < 0:
        print("Quantity rejected")
        valid = False
    else:
        print("Quantity accepted")

    if valid:
        cursor.execute(
            "SELECT id FROM products WHERE sku = %s",
            (sku,)
        )

        existing_product = cursor.fetchone()

        if existing_product is not None:
            print("SKU already exists")
        else:
            cursor.execute(
                """
                INSERT INTO products (name, sku, price, quantity)
                VALUES (%s, %s, %s, %s)
                """,
                (product_name, sku, price, quantity)
            )

            conn.commit()
            print("Product added successfully")

cursor.close()
conn.close()