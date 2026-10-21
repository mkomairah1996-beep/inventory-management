print(" Inventory Managment System")
print("Welcome to your inventory")



try:
   product_name = input("enter product name:").strip()
   sku= input("enter sku").strip()
   price = float(input("price:"))
   quantity= int(input("quantity: "))
   if not product_name:
     print("product name connot be empty")
   elif not any (char.isalpha() for char in product_name):
     print("product name must contain at least one letter")
   if not sku:
     print("sku cannot be empty")
   if price<=0:
     print("price rejected")
   else :
     print("price accepted")
   if quantity<0:
     print("quantity")
   else:
     print(" quantity accepted")
   
except ValueError:
 print("invalid price")
products=[] 
product = {"name":product_name,
            "Sku": sku,
            "price":price,
            "quantity":quantity
 }
for existing_product in products:
  if existing_product["sku"]==sku:
    print("sku already exists")
    break
else:
  print("sku is available to add")
  products.append(product)





