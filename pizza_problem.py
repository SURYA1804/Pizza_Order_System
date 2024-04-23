#=============================
#Pizza Problem Using OOPS
#=============================
class pizza:
    def __init__(self,name,price):
        self.name=name
        self.price=price
c=[]
p=[pizza("regular pizza",50),pizza("whole wheat pizza",75)]
while True:
  print("------------------Available pizza----------------")
  for i in range(0,len(p)):
    print(p[i].name,":",p[i].price)
  print("Enter 'next' to show other option.")
  pchoice=input("Enter the pizza:")
  if pchoice == 'next':
    break;
  count=int(input("Enter the count:"))
  for i in range(0,len(p)):
    if pchoice==p[i].name:
      c.append(cart(count,p[i].name,p[i].price))

class toppings:
    def __init__(self,name,price):
        self.name=name
        self.price=price

t=[toppings("mozzarella cheese",30),toppings("cheddar",35),toppings("spanish",20),toppings("corn",15),toppings("mushroom",15)]
while True:
  print("--------------Available Toppings-----------------")
  for i in range(0,len(t)):
    print(t[i].name,":",t[i].price)
  print("Enter next to show other option.")
  tchoice=input("Enter the toppings:")
  if tchoice=='next':
    break;
  count=int(input("Enter the count:"))
  for i in range(0,len(t)):
    if tchoice==t[i].name:
      c.append(cart(count,t[i].name,t[i].price))


class drink:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class calculation:
        def calculation(self):
                print("**************BILL***************")
                print("You have selected:")
                total=0
                for i in range(0,len(c)):
                  print("Item = ",c[i].name,"|| Price =",c[i].price,"|| Count = ",c[i].count,"|| Total = ",c[i].count*c[i].price)
                  total=total+(c[i].count*c[i].price)
                print("The final amount to pay:",total-(discounts()*total))
                print("************+++++++*************")
class cart:
  def __init__(self,count,name,price):
    self.count=count
    self.name=name
    self.price=price
class discount:
  def __init__(self,pizza,toppings,drink,discountrate):
    self.pizza=pizza
    self.toppings=toppings
    self.drink=drink
    self.discountrate=discountrate
dis=discount('regular pizza','corn','pepsi',0.05)

def discounts():
  for i in c:
    if dis.pizza == i.name:
      for i in c:
        if dis.toppings == i.name:
          for i in c:
            if dis.drink == i.name:
              return dis.discountrate
    else:
      return 0

def isDrinkOptionSelected(selectedDrinkOption):
    return selectedDrinkOption == 1
drinkoption=int(input("If you need drink press 1  (OR)\nIf you dont need press 2: "))
if(isDrinkOptionSelected(drinkoption)):
    d=[drink("pepsi",15),drink("7-up",20),drink("coke",25)]
    while True:
      print("----------------Available Drinks----------------")
      for i in range(0,len(d)):
        print(d[i].name,":",d[i].price)
      print("Enter next to show other option.")
      dchoice=input("Enter the drink:")
      if dchoice=='next':
        break;
      count=int(input("Enter the count:"))
      for i in range(0,len(d)):
        if dchoice==d[i].name:
          c.append(cart(count,d[i].name,d[i].price))

cal=calculation()
cal.calculation()


