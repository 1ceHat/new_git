class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:

    def __init__(self, file_name: str):
        self.__file_name = file_name

    def get_products(self):
        file = open(self.__file_name, 'r')
        text = file.read()
        file.close()
        return text

    def add(self, *products: Product):
        for product in products:
            file = open(self.__file_name, 'a')
            text = self.get_products()
            if product.name.lower() not in text.lower():
                file.write(str(product)+'\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине' )
            file.close()


s1 = Shop('products.txt')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())