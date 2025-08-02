class Discount:

    def __init__(self, price, discount):
        self.price = price
        self.discount = discount

    def apply_discount(self):
        raise NotImplementedError("Please implement the apply discount method")


class NewYearDiscount(Discount):
    def __init__(self, price, discount):
        super().__init__(price, discount)
