from enum import Enum

# Creating Enum
class OrderStatus(Enum):
    PENDING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4


# Menu program
print("1. Pending")
print("2. Shipped")
print("3. Delivered")
print("4. Cancelled")

choice = int(input("Enter choice: "))

if choice == 1:
    order = OrderStatus.PENDING

elif choice == 2:
    order = OrderStatus.SHIPPED

elif choice == 3:
    order = OrderStatus.DELIVERED

elif choice == 4:
    order = OrderStatus.CANCELLED

else:
    print("Invalid Choice")

print("Order Status:", order)