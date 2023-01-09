import csv
class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity = 0):
        #Run validations to the received arguments
        assert price >= 0 
        assert quantity >= 0
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
       
    def calculate_total_price(self):
          return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r')as f:
            reader = csv.DictReader(f) #reads content as a dictionary
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
         )
    @staticmethod         
    def is_integer(num):
        #we will count out the floats that are point zeroi.e 10.0 etc
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
    
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

       
# print(Item.is_integer(7.0))
# print(Item.__dict__) #All the attribute for class level
# print(item2.__dict__)#All the attribute for instance level



