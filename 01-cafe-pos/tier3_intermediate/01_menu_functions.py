"""
CHALLENGE: Rebuild Ordering With Functions
DIFFICULTY: Intermediate
FOLDER: 01-cafe-pos / tier3_intermediate

STORY
-----
The head barista wants the ordering logic cleaned up so different parts of
the café's system can reuse it. Instead of one long block of code, you'll
break the logic into three separate functions.

YOUR TASK
---------
Implement the three functions below (read each docstring carefully), then
use them together in the `if __name__ == "__main__":` section at the
bottom to run a full ordering loop.

EXAMPLE OUTPUT
--------------
What would you like? (type 'done' to finish): Coffee
Added Coffee - $4.5
What would you like? (type 'done' to finish): Muffin
Added Muffin - $5.0
What would you like? (type 'done' to finish): done

----- RECEIPT -----
Coffee            $4.50
Muffin            $5.00
--------------------
TOTAL:            $9.50
"""

MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}
def get_price(item_name):
    if item_name in MENU:
        return MENU[item_name]
    else: 
        return 0

def calculate_total(order_list):
    total = 0
    for item_name in order_list:
        total += get_price(item_name)

    return total

def display_receipt(order_list, total):
    print("----------RECEIPT----------")
    for item_name in order_list:
        print(item_name, MENU[item_name])
    """
    Print a neatly formatted receipt for order_list, followed by the total,
    matching the style shown in the EXAMPLE OUTPUT above
    """
    # TODO: implement this function
    pass


if __name__ == "__main__":
    running = True
    order_list = []
    while running:
        item_name = input(".")
        order_list.append(item_name)
        price = get_price(item_name)
        if item_name in MENU:
            print(f"Added {item_name} to your order!")
        elif item_name == "Finish":
            order_list = [item_name for item_name in order_list if item_name in MENU]
            total = calculate_total(order_list)
            display_receipt(order_list, total)
        else:
            print(f"We do not currently have {item_name} in stock")
        print(f"Your current total is {calculate_total(order_list)}")


        # TODO: write a while loop (like in tier2) that asks the customer what
        # they'd like, adds valid items to order_list, and stops when they type
        # "done".

        # TODO: once the loop is done, call calculate_total() and then
        # display_receipt() to show the final receipt.

