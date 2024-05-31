

#создание_класса
class Category:
 # атрибуты
 #типы_данных
 name: str
 description:str
 products: str

# конструктор_класса
# __init__
 def __init__(self,name,description,products):
#self
  self.name = name
  self.description = description
  self.products = products


#создание_класса
class Product:
 # атрибуты
 #типы_данных
 name: str
 description: str
 price: float
 quantity: int

# конструктор_класса
# __init__
 def __init__(self,name,description,price,quantity):
# self
  self.name = name
  self.description = description
  self.price = price
  self.quantity = quantity