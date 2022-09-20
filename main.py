"""
Driver class for A2
Author: Grace Codd
Date: 9/20/2022
"""


# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import classes Computer and ResaleShop so their instance methods can be used
from computer import Computer
from oo_resale_shop import ResaleShop

def main():
    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Instantiate resale shop object, assign to variable "shop"
    shop = ResaleShop()

    # Instantiate computer object, assign to variable "computer_obj"
    # Pass arguments for all attributes
    computer = Computer("Mac Pro (Late 2013)",
                        "3.5 GHc 6-Core Intel Xeon E5",
                        1024, 64,
                        "macOS Big Sur", 2013, 1500)

    # Add computer to store's inventory                    
    print("Buying", computer.description)
    print("Adding to inventory...")
    # Call buy instance method for shop object, pass computer object as argument
    # Assign return value to computer_id
    computer_id = shop.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    #Call print_inventory instance method 
    shop.print_inventory()
    print("Done.\n")    

    # Now, let's refurbish it
    #Store name of new OS in new_OS variable
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    # Call refurbish instance method from shop object
    # Pass computer_id and new_OS as args
    shop.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    # Call print_inventory instance method from shop object
    shop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    #Call sell instance method from shop object, pass computer_id as arg
    shop.sell(computer_id)

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    #Call print_inventory instance method from shop object
    shop.print_inventory()
    print("Done.\n")
    
if __name__ == "__main__": main()
