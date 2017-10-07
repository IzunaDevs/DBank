from rates import Converter


class User:
    def __init__(self, manager, id: int):
        self.id = id
        self.wallet = Wallet(manager, self, manager.get_data(id))


class Wallet:
    def __init__(self, manager, user: User, data: dict = None):
        data = data or {}

        self.id = user.id
        self.converter = Converter()

        for currency, amount in data.items():
            self.converter.register(manager, currency, amount)

    def convert(self, from_currency, to_currency, amount):
        self.converter.convert(from_currency, to_currency, amount)
