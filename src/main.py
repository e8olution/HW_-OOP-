from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

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
        super().__init__()
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

class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class MixinLog():
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"Создание нового экземпляра продукта - {self.__class__.__name__} ({self.__dict__.items()})"


#создание_класса
class Product(AbstractProduct,MixinLog):
    # атрибуты
    name_product: str
    description_product: str
    price: float
    quantity: int

    # конструктор_класса
    def __init__(self, name_product, description_product, price, quantity):
        super().__init__()
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

        # Добавление товаров только из одного класса
    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        total_price = self.price * self.quantity + other.price * other.quantity
        return total_price

    def __repr__(self):
        super().__repr__()

    def __str__(self):

        return f'({self.name_product}, {self.price} руб. Остаток: {self.quantity} шт.)'




# Подкласс от родительского Product
class Smartphone (Product,MixinLog):
    productivity: float
    model: str
    storage: int
    color: str

    def __init__(self, name_product, description_product, _price, quantity, productivity, model, storage, color):
        super().__init__(name_product, description_product, _price, quantity)
        self.productivity = productivity
        self.model = model
        self.storage = storage
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        total_price = self.price * self.quantity + other.price * other.quantity
        return total_price

    def __repr__(self):
        super().__repr__()

    def __str__(self):
        return (f'Бренд: {self.name_product}, Производительность: {self.productivity}, Модель: {self.model}, '
                f'Объем встроенной памяти: {self.storage}, Цвет: {self.color}')

#Подкласс от родительского Product
class Grass (Product):
    producing_country: str
    germination_period: int
    color: str

    def __init__(self, name_product, description_product, _price, quantity, producing_country, germination_period, color):
        super().__init__(name_product, description_product, _price, quantity)
        self.producing_country = producing_country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        total_price = self.price * self.quantity + other.price * other.quantity
        return total_price

    def __repr__(self):
        super().__repr__()

    def __str__(self):
        return (f'Бренд: {self.name_product}, Cтрана-производитель: {self.producing_country}, '
                f'Cрок прорастания: {self.germination_period} '
                f'Цвет: {self.color}')

class Order(AbstractCategory):
    def __init__(self, name_category, description_category, product, quantity):
        super().__init__()
        # Проверка продукта на схожесть класса и его наследников
        if not isinstance(product, Product):
            raise TypeError
        # Проверка если кол-во эл. заказа соответствует кол-ву на складе
        if quantity > product.quantity:
            raise ValueError (f'Максимальное доступное количество {product.quantity}')
        self.name_category = name_category
        self.description_category = description_category
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
        product.quantity -= quantity

    def __str__(self):
        return (f'Заказ: {self.name_category}, Описание: {self.description_category}, Товар: {self.product.name_product}, '
                f'Количество: {self.quantity}, Итоговая стоимость: {self.total_price} руб.')


# Вводные данные

if __name__ == '__main__':


    product_1 = Product('Samsung', 'New_1',
                        99.99, 10)
    product_2 = Product('iPhone', 'New_2',
                        89999, 5)
    print(f'\nОбщая цена для продуктов с одной категории: '
          f'{Product.__add__(product_1, product_2)}:')

    phone_1 = Smartphone('Iphone', 'New_1',
                         99.99, 10, 2000.00, '15 Pro',
                          512, 'Black')
    phone_2 = Smartphone('Samsung', 'New_2',
                         89999, 5, 1000, 'A10',
                          256, 'White')


    grass_1 = Grass('Мини-газон', 'Смесь трав',
                    1000, 10, 'Россия',
                        35, 'Светлый')

    grass_2 = Grass('Газонная трава', 'Универсальный',
                    500.99, 20, 'США',
                        25, 'Темный')

    print(f'\n{phone_1}')
    print(f'Общая сумма товаров в категории Смартфон: {phone_1 + phone_2}')
    print(f'\n{grass_1}')
    print(f'Общая сумма товаров в категории Трава газонная: {grass_1 + grass_2}')