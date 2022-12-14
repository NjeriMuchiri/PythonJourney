import csv
class Item:
    pay_rate = 0.8 #pay rate after 20% discount
    all = []
    def __init__(self,name: str, price: float, quantity = 0):
        #Run validations to the received arguments
        assert price >= 0 
        assert quantity >= 0
        
        #Assign to self object
        self.__name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
    @property 
    #property decorator = Read-only attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        #  print("You are trying to set a new name:")
         self.__name = value
          
    def calculate_total_price(self):
          return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
    @classmethod
    #used to manipulate python data structure
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
    #for uniqueness       
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
    
       
# print(Item.is_integer(7.0))
# print(Item.__dict__) #All the attribute for class level
# print(item2.__dict__)#All the attribute for instance level



