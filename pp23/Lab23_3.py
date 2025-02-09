class Product:
    def __init__(self, name, category, price, rebate):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__rebate = rebate

    def calculate_price(self):
        discounted_price = self.__price * ( 1 -(self.__rebate / 100))
        print(f"Cena po uwzględnieniu rabatu to {discounted_price}.")

    def determine_category(self):
        print(f"Ten produkt należy do kategorii {self.__category}.")

    def apply_rebate(self, rebate: float):
        if rebate >= 0:
            self.__rebate = rebate

    def __str__(self):
        return (f"Produkt: {self.__name}, Kategoria: {self.__category}, "
                f"Cena: {self.__price:.2f} PLN, Rabat: {self.__rebate}%")




products = [
    Product("Laptop", "Elektronika", 3999.99, 10),
    Product("Smartfon", "Elektronika", 2999.99, 10),
    Product("Buty sportowe", "Obuwie", 299.99, 0),
    Product("Koszula", "Odzież", 149.99, 0),
    Product("Kurtka", "Odzież", 499.99, 0)
]

# Ustawienie rabatu dla kategorii "Odzież"
for product in products:
    if product._Product__category == "Odzież":
        product.apply_rebate(15)

# Wyświetlenie listy produktów
for product in products:
    print(product)
