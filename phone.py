from item import Item
class Phone(Item):
         def __init__(self, name: str, price: float, quantity = 0,broken_phones = 0):
         #call to super function to have acccess to all methods
              super().__init__(
                  name,price,quantity
               )
        #Run validations to the received arguments
              assert broken_phones >= 0
        #Assign to self object
              self.broken_phones = broken_phones
              
              
phone1 = Phone("Iphone13", 500, 5, 1)

print(Phone.all)
print(Item.all)