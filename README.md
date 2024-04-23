Pizza Order System with Object-Oriented Programming (OOP)

This Python program simulates a pizza ordering system using OOP concepts. It allows users to select pizzas, toppings, and optionally drinks, and then calculates the final bill amount with a discount applied based on specific criteria.

Classes:

    1.pizza: Represents a pizza with attributes name and price.
    2.toppings: Represents a topping option with attributes name and price.
    3.drink (optional): Represents a drink option with attributes name and price (included if user chooses to add a drink).
    4.cart: Holds the selected items (pizza, toppings, drinks) with attributes count (quantity), name, and price.
    5.calculation: Calculates the total bill amount and applies a discount if applicable.
    6.discount (optional): Defines the discount rate based on specific criteria (currently set for a combination of regular pizza, corn topping, and pepsi drink).

Functionalities:

    1.The program displays available pizzas and toppings.
    2.Users can choose items and specify quantities.
    3.The program allows users to choose a drink if desired.
    4.A discount is applied if the chosen items match the criteria defined in the discount class (customizable).
    5.Finally, the program displays a bill with item details, total price, and the final amount after discount.

Note:

    1.This is a basic example and can be extended to include features like:
        I)Adding more pizza and topping options.
        II)Implementing different discount rules based on various criteria.
        III)User authentication and order history.

Getting Started:

    1.Ensure you have Python installed.
    2.Save the code as a Python file (e.g., pizza_order.py).
    3.Run the script from your terminal using python pizza_order.py.
