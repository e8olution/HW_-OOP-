
#создание_класса
class Category:
    # атрибуты
    name: str
    description: str
    products: list
    count_categories = 0
    count_uniq_cat = 0

    # конструктор_класса
    def __init__(self,name,description,products):
        # self
        self.name = name
        self.description = description
        self.__products = products
        Category.count_uniq_cat += len(set([product.name for product in products]))
        Category.count_categories += 1
    #Добавление товара в список
    def add_product(self, product):
        return self.__products.append(product)

    # Выыод товаров в формате: Продукт, 80 руб. Остаток: 15 шт.
    #декоратор(getter,setter,deleter)
    @property
    def products(self):
        #Геттер
        return [f'{Product.name},{Product.price}руб. Остаток: {Product.quantity} шт.' for Product in self.__products]

def __repr__(self):
    return f'Product(name={self.name}, description={self.description}, price={self.price}, quantity={self.quantity})'

#создание_класса
class Product:
    # атрибуты
    name: str
    description: str
    price: float
    quantity: int

    # конструктор_класса
    def __init__(self,name,description,price,quantity):
        # self
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    #Декоратор(статический)
    @staticmethod
    def new_product(name, description, price, quantity, product_list):
        # Проверка наличия дубликатов
        for product in product_list:
            if product.name == name:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
        # Создание нового продукта, если дубликат не найден
        new_product = Product(name, description, price, quantity)
        product_list.append(new_product)
        return new_product
    #Геттер для цены
    @property
    def price(self):
        return self._price
    #Сеттер для цены
    @price.setter
    def price(self,value):
        if value <= 0:
            print("Цена введена некорректная")
            return
        # Подтверждение пользователем понижения цены товара
        if value < self._price:
            confirm = input (f"Подтвердите снижение цены с {self._price} до {value} (y/n)")
            if confirm.lower() != 'y':
                return
        self._price = value