"""
CHALLENGE: Take a Full Order
DIFFICULTY: Beginner
FOLDER: 01-cafe-pos / tier2_beginner

STORY
-----
A customer wants to order several things, one at a time, until they say
they're finished. You need to keep a running total of what they owe.

YOUR TASK
---------
1. Keep asking the customer "What would you like? (type 'done' to finish)"
2. Every time they type a valid menu item, add its price to a running total
   and print a short confirmation.
3. If they type something not on the menu (and not "done"), print a message
   saying it's not available, and ask again.
4. When they type "done", stop asking and print their final total.

EXAMPLE OUTPUT
--------------
What would you like? (type 'done' to finish): Coffee
Added Coffee - $4.5
What would you like? (type 'done' to finish): Muffin
Added Muffin - $5.0
What would you like? (type 'done' to finish): Pizza
Sorry, Pizza is not on the menu.
What would you like? (type 'done' to finish): done
Your total is $9.5

HINTS
-----
- Use a `while True:` loop, and use `break` to stop it when the customer
  types "done".
- Keep a variable like `total = 0` outside the loop, and add to it inside.
"""

MENU = {
    "Coffee": 4.50,
    "Tea": 3.50,
    "Muffin": 5.00,
    "Toastie": 6.50,
    "Hot Chocolate": 4.00,
}

ordertotal = 0

running = True
while running:
   order = input("What would you like? ")
   if order in MENU:
      ordertotal += MENU[order]
      print(f"{order} ${MENU[order]}")
      print(f"Your total is ${ordertotal}")
      print(f'Type "done" to finish your order.')
   elif order == "done":
      print("Thanks for ordering! Your item will be ready soon.")
      running = False
   else:
      print('Item or command not found. Please try again or type "done" to finish.')


# TODO: write a while loop that:
#   - asks "What would you like? (type 'done' to finish): "
#   - if the answer is "done", stops the loop
#   - if the answer is a valid menu item, adds its price to `total`
#     and prints "Added {item} - ${price}"
#   - otherwise prints "Sorry, {item} is not on the menu."


# TODO: after the loop finishes, print the final total, e.g. "Your total is $9.5"
