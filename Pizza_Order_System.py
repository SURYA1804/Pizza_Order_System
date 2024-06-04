#=============================
#Pizza Order System Using OOPS
#=============================
class Pizza:
    def __init__(self,name,price):
        self.name=name
        self.price=price

pizza=[Pizza("regular pizza",50),Pizza("whole wheat pizza",75)]

class Toppings:
    def __init__(self,name,price):
        self.name=name
        self.price=price

toppings=[Toppings("mozzarella cheese",30),Toppings("cheddar",35),Toppings("spanish",20),Toppings("corn",15),Toppings("mushroom",15)]

class Drink:
    def __init__(self,name,price):
        self.name=name
        self.price=price

class Cart:
  def __init__(self,count,name,price):
    self.count=count
    self.name=name
    self.price=price

cart=[]

class Discount:
  def __init__(self,Pizza,Toppings,Drink,discount_rate):
    self.Pizza=Pizza
    self.Toppings=Toppings
    self.Drink=Drink
    self.discount_rate=discount_rate
  @classmethod
  def discount_calculation(self):
     for k in discount:
        if k.Pizza in [i.name for i in cart if True]:
           if k.Toppings in [i.name for i in cart if True]:
              if k.Drink in [i.name for i in cart if True]:
                 return k.discount_rate
     return 0
           

discount=[Discount('regular pizza','corn','pepsi',0.05),Discount('whole wheat pizza','spanish','coke',0.10)]


while True:
  print("------------------Available Pizza----------------")
  for i in range(0,len(pizza)):
    print(pizza[i].name,":",pizza[i].price)
  print("Enter 'next' to show other option.")
  pchoice=input("Enter the Pizza:")
  if pchoice == 'next':
    break;
  count=int(input("Enter the count:"))
  for i in range(0,len(pizza)):
    if pchoice==pizza[i].name:
      cart.append(Cart(count,pizza[i].name,pizza[i].price))

while True:
  print("--------------Available Toppings-----------------")
  for i in range(0,len(toppings)):
    print(toppings[i].name,":",toppings[i].price)
  print("Enter next to show other option.")
  tchoice=input("Enter the Toppings:")
  if tchoice=='next':
    break;
  count=int(input("Enter the count:"))
  for i in range(0,len(toppings)):
    if tchoice==toppings[i].name:
      cart.append(Cart(count,toppings[i].name,toppings[i].price))

drinkoption=int(input("If you need Drink press 1  (OR)\nIf you dont need press 2: "))

def isDrinkOptionSelected(selectedDrinkOption):
    return selectedDrinkOption == 1

if(isDrinkOptionSelected(drinkoption)):
    drink=[Drink("pepsi",15),Drink("7-up",20),Drink("coke",25)]
    while True:
      print("----------------Available Drinks----------------")
      for i in range(0,len(drink)):
        print(drink[i].name,":",drink[i].price)
      print("Enter next to show other option.")
      dchoice=input("Enter the Drink:")
      if dchoice=='next':
        break;
      count=int(input("Enter the count:"))
      for i in range(0,len(drink)):
        if dchoice==drink[i].name:
          cart.append(Cart(count,drink[i].name,drink[i].price))

class Calculation:
        @classmethod
        def calculation(self):
                print("**************BILL***************")
                print("You have selected:")
                total=0
                for i in range(0,len(cart)):
                  print("Item = ",cart[i].name,"|| Price =",cart[i].price,"|| Count = ",cart[i].count,"|| Total = ",cart[i].count*cart[i].price)
                  total=total+(cart[i].count*cart[i].price)
                print("The final amount to pay:",total-(Discount.discount_calculation()*total))
                print("************+++++++*************")

Calculation.calculation()


