import pytest
from src.main import Product,Category



@pytest.fixture
def category_data():
    return Category('Electronics', 'Smartphones',
                    [Product('Iphone','New_1', 99.999, 100),
                     Product('Samsung','New_2', 89.999, 99)])
def test_init_Category(category_data):
    # Проверка корректности инициализации объектов класса Category
    assert category_data.name == 'Electronics'
    assert category_data.description == 'Smartphones'
    assert category_data.products == [Product('Iphone','New_1', 99.999, 100),
                     Product('Samsung','New_2', 89.999, 99)]

    assert category_data.count_uniq_cat == 1
    assert category_data.count_categories == 2

@pytest.fixture
def product_data():
    return Product('Electronics','Smartphones',99.999, 100)
def test_init_Product(product_data):
    assert product_data.name == "Samsung"
    assert product_data.description == "A mobile phone with advanced features"
    assert product_data.price == 999.99
    assert product_data.quantity == 100

