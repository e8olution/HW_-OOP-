
#создание_класса
class Category:
    # атрибуты
    name_category: str
    description_category: str
    products: list
    count_categories = 0
    count_uniq_cat = 0

    # конструктор_класса
    def __init__(self, name_category, description_category, products):
        # self
        self.name_category = name_category
        self.description_category = description_category
        self.__products = products
        Category.count_uniq_cat += len(set([product.name_product for product in products]))
        Category.count_categories += 1

    #Добавление обьекта в список класса Product и его наследников
    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)


    # Выыод товаров в формате: Продукт, 80 руб. Остаток: 15 шт.
    # декоратор(getter,setter,deleter)
    @property
    def products(self):
        #Геттер
        return [f'{product.name_product}, {product.price} руб. Остаток: {product.quantity} шт.' for product in self.__products]
    def __str__(self):
        return f'{self.description_category}, количество продуктов: {len(self.__products)} шт.'
    def __len__(self):
        return sum(product.quantity for product in self.__products)


##########################__Product__##########################

#создание_класса
class Product:
    # атрибуты
    name_product: str
    description_product: str
    price: float
    quantity: int

    # конструктор_класса
    def __init__(self, name_product, description_product, price, quantity):
        # self
        self.name_product = name_product
        self.description_product = description_product
        self._price = price
        self.quantity = quantity

    #Декоратор(статический)
    @staticmethod
    def new_product(name_product, description_product, price, quantity, product_list):
        # Проверка наличия дубликатов
        for product in product_list:
            if product.name_product == name_product:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
        # Создание нового продукта, если дубликат не найден
        new_product = Product(name_product, description_product, price, quantity)
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


    def __str__(self):

        return f'({self.name_product}, {self.price} руб. Остаток: {self.quantity} шт.)'

# Добавление товаров только из одного класса
    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        total_price = self.price * self.quantity + other.price * other.quantity
        return total_price


# Подкласс от родительского Product
class Smartphone (Product):

    def __init__(self, name_product, description_product, _price, quantity, productivity, model, storage, color):

        super().__init__(name_product, description_product, _price, quantity)
        self.productivity = productivity
        self.model = model
        self.storage = storage
        self.color = color


#Подкласс от родительского Product
class Grass (Product):
    def __init__(self, name_product, description_product, _price, quantity, producing_country, germination_period, color):

        super().__init__(name_product, description_product, _price, quantity)
        self.producing_country = producing_country
        self.germination_period = germination_period
        self.color = color