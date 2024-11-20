#CHAT-BOT jarvis or tony stark
'''
as web-site owner ask
creating this to help customers
for orders or more 
using this for many purpose
features-
1.price calculation
2.gives id after order
New order                    track-order                         offers/store hours
Place new order            Track order by order-ID                ongoing offers
cash on dilevary 
support payment            Track order by phone number            upcoming offers
through a chat boat        track order by customer name              Store hours
'''
import random

# Hotel menu with items and prices
menu = {
    1: {"name": "Pav Bhaji", "price": 80},
    2: {"name": "Chinese", "price": 150},
    3: {"name": "Pizza", "price": 200},
    4: {"name": "Burger", "price": 100},
    5: {"name": "Rolls", "price": 90},
    6: {"name": "Fries", "price": 50},
    7: {"name": "Veg Thali", "price": 180},
    8: {"name": "Chicken Thali", "price": 220},
    9: {"name": "Ice Cream", "price": 60},
    10:{"name": "Cold Drink", "price": 40},
}

# Ongoing and upcoming offers
offers = {
    "ongoing": ["10% off on Pizza", "Buy 1 Get 1 Free on Ice Cream", "Get Free Lassi On Veg Thali!"],
    "upcoming": ["20% off on Veg Thali", "Free Cold Drink with Chinese Combo"]
}

# Dictionary to store orders
orders = {}

# Function to display the menu
def display_menu():
    print("Menu:")
    for key, value in menu.items():
        print(f"{key}. {value['name']} - ₹{value['price']}")

# Function to calculate the total price with discounts
def calculate_total(order_items):
    total = 0
    for item in order_items:
        if item == 3:  # Pizza (10% off)
            discount_price = menu[item]["price"] * 0.9  # 10% discount
            total += discount_price
            print("Yay! You got 10% off on Pizza!")
        elif item == 9:  # Ice Cream (Buy 1 Get 1 Free)
            total += menu[item]["price"]
            print("Yay! You got one Ice Cream for free!")
        else:
            total += menu[item]["price"]
    return total

# Function to place a new order
def place_order(customer_name):
    display_menu()
    order_items = []
    while True:
        try:
            item = int(input("Enter item number you want to order (0 to finish): "))
            if item == 0:
                break
            elif item in menu:
                order_items.append(item)
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    if order_items:
        order_id = random.randint(1000, 9999)  # Generate a random order ID
        total_amount = calculate_total(order_items)  # Calculate total price
        
        # Ask for payment method
        print("\nSelect Payment Method:")
        print("1. Cash on Delivery")
        print("2. Credit/Debit Card (Online)")
        payment_method = input("Enter your choice (1/2): ")
        
        if payment_method == '1':
            payment_type = "Cash on Delivery"
        elif payment_method == '2':
            print("Online payment is not available at the moment, please use Cash on Delivery.")
            payment_type = "Cash on Delivery"
        else:
            print("Invalid payment method selected. Defaulting to Cash on Delivery.")
            payment_type = "Cash on Delivery"
        
        # Store order details
        orders[order_id] = {
            "name": customer_name,
            "items": order_items,
            "total": total_amount,
            "payment": payment_type
        }
        
        # Display order summary
        print(f"\nOrder placed successfully! Your order ID is {order_id}.")
        print(f"Items Ordered: {', '.join(menu[item]['name'] for item in order_items)}")
        print(f"Total Amount: ₹{total_amount}")
        print(f"Payment Method: {payment_type}")
        print("Thank you for using Jarvis!")
    else:
        print("No items selected. Order not placed.")

# Function to track an order by Order ID
def track_order():
    try:
        # Choose tracking method
        print("Track your order by:")
        print("1. Order ID")
        print("2. Customer Name")
        choice = int(input("Enter your choice (1 or 2): "))

        # Track by Order ID
        if choice == 1:
            order_id = int(input("Enter your Order ID: "))
            if order_id in orders:
                order = orders[order_id]
                print(f"Order found! Customer: {order['name']}, Items: {', '.join(menu[item]['name'] for item in order['items'])}")
                print(f"Total: ₹{order['total']}, Payment Method: {order['payment']}")
            else:
                print("Order ID not found.")

        # Track by Customer Name
        elif choice == 2:
            customer_name = input("Enter the Customer Name: ").strip().lower()
            found = False
            for order_id, order in orders.items():
                if order['name'].strip().lower() == customer_name:
                    print(f"Order found! Order ID: {order_id}, Items: {', '.join(menu[item]['name'] for item in order['items'])}")
                    print(f"Total: ₹{order['total']}, Payment Method: {order['payment']}")
                    found = True
                    break
            if not found:
                print("No orders found for the given name.")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter numeric values where applicable.")



# Function to display ongoing and upcoming offers
def show_offers():
    print("1. Ongoing Offers")
    print("2. Upcoming Offers")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        print("Ongoing Offers:")
        for offer in offers["ongoing"]:
            print(f"- {offer}")
    elif choice == '2':
        print("Upcoming Offers:")
        for offer in offers["upcoming"]:
            print(f"- {offer}")
    else:
        print("Invalid choice.")

# Function to show store hours
def show_store_hours():
    print("Store Hours: 9 AM to 11 PM")

# Jarvis chatbot function
def jarvis():
    print("Welcome to Jarvis Chatbot!")
    customer_name = input("Enter your name: ")
    
    while True:
        print("\nHow can I assist you?")
        print("1. Place a New Order")
        print("2. Track an Order")
        print("3. View Ongoing/Upcoming Offers")
        print("4. Store Hours")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            place_order(customer_name)
        elif choice == '2':
            track_order()
        elif choice == '3':
            show_offers()
        elif choice == '4':
            show_store_hours()
        elif choice == '5':
            print("Thank you for using Jarvis! Have a great day.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the Jarvis chatbot
jarvis()
