"""
CHALLENGE: Build an Order Class
DIFFICULTY: Intermediate
FOLDER: 01-cafe-pos / tier3_intermediate

STORY
-----
The café wants each customer's order to be its own self-contained "thing"
in the code, with its own list of items and its own total — that's exactly
what a class is for.

YOUR TASK
---------
Complete the `Order` class below by implementing each method described in
its docstring. Then test it using the code at the bottom of the file.

EXAMPLE OUTPUT (from the test code at the bottom)
--------------------------------------------------
Added Coffee to the order.
Added Muffin to the order.
Added Tea to the order.
Removed Tea from the order.
Current order: ['Coffee', 'Muffin']
Order total: $9.5
"""

MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}


class Order:
    """Represents one customer's order at The Trendiest Café."""

    def __init__(self):
        self.items = []


    def add_item(self, item_name):
        if item_name in MENU:
            self.items.append(item_name)
            print(f"Added {item_name} to your order!")
        else:
            print("Not in this store bucko")

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"Removed {item_name} from your order!")
        else:
            print(f"You have not ordered {item_name}")

    def get_total(self):
        totalprice = 0
        for item_name in self.items:
            totalprice += MENU[item_name]
        return totalprice



if __name__ == "__main__":
    my_order = Order()
    my_order.add_item("Coffee")
    my_order.add_item("Muffin")
    my_order.add_item("Toastie")
    my_order.add_item("Tea")
    my_order.remove_item("Tea")

    print(f"Current order: {my_order.items}")
    print(f"Order total: ${my_order.get_total()}")
