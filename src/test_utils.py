
from utils import Category,Product

def test_category_initialization():
    # Проверка корректности инициализации объектов класса Category
    category = Category(name="Electronics", description="Devices and gadgets", products=[])
    assert category.name == "Electronics"
    assert category.description == "Devices and gadgets"
    assert category.products == []

def test_product_initialization():
    # Проверка корректности инициализации объектов класса Product
    product = Product(name="Smartphone", description="A mobile phone with advanced features", price=999.99, quantity=10)
    assert product.name == "Smartphone"
    assert product.description == "A mobile phone with advanced features"
    assert product.price == 999.99
    assert product.quantity == 10

def test_count_products():
    # Подсчет количества продуктов в категории
    products = [
        Product(name="Smartphone", description="A mobile phone with advanced features", price=999.99, quantity=10),
        Product(name="Laptop", description="A portable computer", price=1299.99, quantity=5),
        Product(name="Tablet", description="A mobile device with a larger screen", price=499.99, quantity=7)
    ]
    category = Category(name="Electronics", description="Devices and gadgets", products=products)
    assert len(category.products) == 3

def test_count_categories():
    # Подсчет количества категорий
    categories = [
        Category(name="Electronics", description="Devices and gadgets", products=[]),
        Category(name="Clothing", description="Apparel and accessories", products=[]),
        Category(name="Books", description="Printed and digital books", products=[])
    ]
    assert len(categories) == 3
