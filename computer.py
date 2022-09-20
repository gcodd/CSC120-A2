class Computer:
    """
    Description: Computer class allows objects representing a computer to be made 
    Author: Grace Codd (@gcodd)
    Date: 9/20/2022

    Attributes:
    ------------
    description: str
        string describing computer i.e. company, type, and year made 
    processor_type: str
        name of processor
    hard_drive_capacity: int
        hard drive storage capacity in GB
    memory: int
        RAM storage capacity in GB
    operating_system: str
        name of operating system
    year_made: int
        year computer was made
    price: float
        price of computer. float to allow for decimal values

    Methods:
    ----------
    computer_dict()
        converts object to dictionary containing info about computer's attributes 
    update_price(new_price: int)
        changes computer's price attribute to value passed through new_price
    update_os(new_os: str)
        changes computer's operating_system attribute to string passed through new_os
    toString()
        prints object's attributes as one string
    """

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                description: str,
                processor_type: str, 
                hard_drive_capacity: int, 
                memory: int,
                operating_system: str, 
                year_made: int, 
                price: float):
        """
        Takes in values for all class attributes and assigns them to each attribute.
        """
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
    def update_price(self, new_price: float):
        """
        Updates computer's price

        Parameters
        ------
        new_price: float
            value representing new price of computer
        """
        self.price = new_price
  
    def update_os(self, new_os: str):
        """
        Updates computer's operating system

        Parameters
        ----------
        new_os: str
            string representing new operating system of computer
        """
        self.operating_system = new_os

    def toString(self):
        """
        Prints object's attributes as a string
        """
        print(self.description, self.processor_type,
                self.hard_drive_capacity, self.memory,
                self.operating_system, self.year_made,
                self.price)
