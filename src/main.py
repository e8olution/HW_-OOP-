from abc import ABC, abstractmethod


class AbstractCategory(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Создание класса
class Category:
    # Атрибуты
    name_category: str
    description_category: str
    products: list
    count_categories = 0
    count_uniq_cat = 0

    # Конструктор класса
    def __init__(self, name_category, description_category, products):
        super().__init__()
        self.name_category = name_category
        self.description_category = description_category
        self.__products = products
        Category.count_uniq_cat += len(
            set([product.name_product for product in products])
        )
        Category.count_categories += 1

    # Добавление объекта в список класса Product и его наследников
    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        if product.quantity == 0:
            raise ZeroDivisionError()
        self.__products.append(product)
        print("Товар добавлен")

    def average_price(self):
        try:
            if len(self.__products) == 0:
                raise ZeroDivisionError
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

    # Вывод товаров в формате: Продукт, 80 руб. Остаток: 15 шт.
    @property
    def products(self):
        return [
            f'{product.name_product}, {product.price} руб. Остаток: '
            f'{product.quantity} шт.'
            for product in self.__products
        ]

    def __str__(self):
        return (
            f'{self.description_category}, количество продуктов: '
            f'{len(self.__products)} шт.'
        )

    def __len__(self):
        return sum(product.quantity for product in self.__products)


class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return (
            f"Создание нового экземпляра продукта - {self.__class__.__name__} "
            f"({self.__dict__.items()})"
        )


# Создание класса
class Product(AbstractProduct, MixinLog):
    # Атрибуты
    name_product: str
    description_product: str
    price: float
    quantity: int

    # Конструктор класса
    def __init__(self, name_product, description_product, price, quantity):
        super().__init__()
        if quantity == 0:
            raise ValueError("Товар с нулевым "
                             "количеством не может быть добавлен")

        self.name_product = name_product
        self.description_product = description_product
        self._price = price
        self.quantity = quantity

    # Декоратор (статический)
    @staticmethod
    def new_product(name_product, description_product, price, quantity,
                    product_list):
        if quantity == 0:
            raise ValueError("Товар с нулевым "
                             "количеством не может быть добавлен")
        # Проверка наличия дубликатов
        for product in product_list:
            if product.name_product == name_product:
                product.quantity += quantity
                product.price = max(product.price, price)
                return product
        # Создание нового продукта, если дубликат не найден
        new_product = Product(
            name_product, description_product, price, quantity
        )
        product_list.append(new_product)
        return new_product

    # Геттер для цены
    @property
    def price(self):
        return self._price

    # Сеттер для цены
    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена введена некорректная")
            return
        # Подтверждение пользователем понижения цены товара
        if value < self._price:
            confirm = input(
                f"Подтвердите снижение цены с {self._price} до {value} (y/n)"
            )
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
        return (
            f'({self.name_product}, {self.price} руб. '
            f'Остаток: {self.quantity} шт.)'
        )


# обьект: Смартфон от родительского Product
class Smartphone(Product, MixinLog):
    productivity: float
    model: str
    storage: int
    color: str

    def __init__(
        self, name_product, description_product, _price, quantity,
        productivity, model, storage, color
    ):
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
        return (
            f'Бренд: {self.name_product}, '
            f'Производительность: {self.productivity}, '
            f'Модель: {self.model}, '
            f'Объем встроенной памяти: {self.storage}, '
            f'Цвет: {self.color}'
        )


# обьект: Трава от родительского Product
class Grass(Product):
    producing_country: str
    germination_period: int
    color: str

    def __init__(
        self, name_product, description_product, _price, quantity,
        producing_country, germination_period, color
    ):
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
        return (
            f'Бренд: {self.name_product}, '
            f'Cтрана-производитель: {self.producing_country},'
            f'Cрок прорастания: {self.germination_period}, '
            f'Цвет: {self.color}'
        )


class ShellException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else ("Товар с нулевым "
                                             "количеством не "
                                             "может быть добавлен")


# Выполнение заказа
class Order(AbstractCategory):
    def __init__(self, name_category, description_category, product, quantity):
        super().__init__()
        try:
            if quantity == 0:
                raise ShellException("товар с нулевым "
                                     "количеством не может быть добавлен")
            # Проверка продукта на схожесть класса и его наследников
            if not isinstance(product, Product):
                raise TypeError
    # Проверка если количество заказа соответствует количеству на складе
            if quantity > product.quantity:
                raise ValueError(f'Максимальное доступное количество'
                                 f' {product.quantity}')
            self.name_category = name_category
            self.description_category = description_category
            self.product = product
            self.quantity = quantity
            self.total_price = product.price * quantity
            product.quantity -= quantity
            print("товар добавлен")
        except ShellException as e:
            print(e)
        finally:
            print("обработка добавления товара завершена")

    def __str__(self):
        return (
            f'Заказ: {self.name_category}, '
            f'Описание: {self.description_category}, '
            f'Товар: {self.product.name_product}, '
            f'Количество: {self.quantity}, '
            f'Итоговая стоимость: {self.total_price} руб.'
        )


# Вводные данные
if __name__ == '__main__':
    try:
        product_1 = Product('Samsung', 'New_1', 99.99, 10)
        product_2 = Product('iPhone', 'New_2', 89999, 5)
#           product_3 = Product('iPhone', 'New_2', 89999, 0)
        print(
            f'\nОбщая цена для продуктов '
            f'с одной категории: {product_1 + product_2}'
        )

        phone_1 = Smartphone(
            'Iphone', 'New_1', 99.99, 10, 2000.00, '15 Pro', 512, 'Black'
        )
        phone_2 = Smartphone(
            'Samsung', 'New_2', 89999, 5, 1000, 'A10', 256, 'White'
        )

        grass_1 = Grass(
            'Мини-газон', 'Смесь трав', 1000, 10, 'Россия', 35, 'Светлый'
        )
        grass_2 = Grass(
            'Газонная трава', 'Универсальный', 500.99, 20, 'США', 25, 'Темный'
        )

        print(f'\n{phone_1}')
        print(
            f'Общая сумма товаров в категории Смартфон: {phone_1 + phone_2}'
        )
        print(f'\n{grass_1}')
        print(
            f'Общая сумма товаров в категории '
            f'Трава газонная: {grass_1 + grass_2}'
        )

    except (ValueError, ZeroDivisionError, TypeError) as e:
        print(e)
