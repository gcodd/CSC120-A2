class ResaleShop:
    """
    Description: ResaleShop class allows objects representing a computer resale store to be made
    Author: Grace Codd (@gcodd)
    Date: 9/20/2022

    Attributes:
    -----------
    inventory: Dict[int, Computer]
        Dictionary holding information about computers in store inventory. Key is integer representing 
        item id and value is object representing a computer
    inv_size: int
        Number of computers stored in the inventory

    Methods:
    ---------
    buy(computer: Computer)
        Adds a computer to the store's inventory
    sell(item_id: int)
        searches for item ID in inventory and removes computer from store's inventory
    refurbish(item_id: int, new_OS)
        searches for object in inventory and updates its price based on the year it was made
        and updates OS if an argument has been passed through new_OS
    print_inventory
        Prints information about all computers stored in store's inventory


    """

    from typing import Dict, Optional
    #ResaleShop inherits Computer class so objects of Computer type can be added to inventory
    from computer import Computer

    # What attributes will it need?
    inventory : Dict[int, Computer] #Holds dictionary containing info about each computer
    inv_size: int #Hold size of inventory

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        """ When a new ResaleShop object is instantiated, inventory will be initialized
        as an empty dictionary and inv_size will be initialized as 0
        """
        self.inventory = {}
        self.inv_size = 0

    # What methods will you need?

    #Buy method: add computer to inventory
    def buy(self, computer: Computer):
        """ Adds a new item to the inventory. Increments inventory size to reflect 
        the addition of a new item.
        
        Parameters:
        -----------
        computer: Computer
            An object of Computer type to be added to inventory
        """
        self.inv_size += 1 # increment inv_size because you are adding a new computer
        itemID = self.inv_size # Assign value stored in inv_size to item_ID, this will be new item's ID
        self.inventory[itemID] = computer # Store copy of Computer obj in inventory at key<itemID>
        return itemID #return the new item's ID

    # Sell method: remove item from inventory
    def sell(self, item_id: int):
        """Searches inventory for an item ID. If the item ID is found, the corresponding object
        will be removed from the inventory. Inventory size is decrememnted if an object is removed.

        Parameters
        ----------
        item_id: int
            ID number of computer object to be searched for and removed from inventory
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            self.inv_size -= 1
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")



    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """ Searches for item ID in inventory. If ID is found, the price 
        of the corresponding object will update based on what year the computer was made.
        The operating system will also update if new_Os is not None.

        Parameters:
        ----------
        item_id: int
            ID number of computer object to be searched for and removed from inventory
        new_OS
            string representing new operating system. Can be None.
        """
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    # Print inventory method: displays all items in inventory 
    def print_inventory(self):
        """
        Prints information about each item in the inventory including their attributes and item ID
        """
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
            # Print its details
                print("Item ID: " + str(item_id))
                self.inventory[item_id].toString()
        else:
            print("No inventory to display.")

