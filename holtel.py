import time

def delay(n):
    time.sleep(n)

def greet():
    print("Welcome to our Restaurant")
    delay(2)

def day():
    answer = input('Waiter: How was your day, sir? ')
    if answer.lower() in ['good', 'nice', 'bravo']:
        delay(1)
        print("Waiter: That's bravo! Then, what would you like to have to increase your mood?")
    else:
        delay(1)
        print("Waiter: I am so sorry to hear that. What would you like to have to increase your mood?")

def menu():
    print(
        "Menu to increase your mood: \n"
        "1. Pizza - $10\n"
        "2. Burger - $8\n"
        "3. French Fries - $5\n"
        "4. Pasta - $12\n"
        "5. Aalu Paratha - $6\n"
        "6. Sandwich - $7\n"
        "7. Pav Bhaji - $9\n"
        "8. Chicken Biryani - $15\n"
    )

def get_order():
    menu()
    order = input("Please enter the numbers of the items you want to order, separated by spaces: ")
    order_list = order.split()
    return [int(item) for item in order_list]

def calculate_bill(order_list, menu_prices):
    total = 0
    for item in order_list:
        total += menu_prices[item - 1]
    return total

def main():
    menu_prices = [10, 8, 5, 12, 6, 7, 9, 15]
    menu_items = ["Pizza", "Burger", "French Fries", "Pasta", "Aalu Paratha", "Sandwich", "Pav Bhaji", "Chicken Biryani"]

    greet()
    day()
    delay(5)

    order_list = get_order()

    print("\nYour order:")
    for item in order_list:
        print(f"- {menu_items[item - 1]}")

    total_bill = calculate_bill(order_list, menu_prices)
    print(f"\nTotal Bill: ${total_bill}")

if __name__ == "__main__":
    main()
