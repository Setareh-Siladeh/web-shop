from shop import Product, find_by_name

products = [
    Product("A1", "Mouse", 1000),
    Product("B2", "Keyboard", 2500)
]

def test_find_case_insensitive():
    assert [p.sku for p in find_by_name(products, "KEY")] == ["B2"]