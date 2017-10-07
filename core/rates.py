DEFAULT = 0


class RateManager:
    pass


class Converter:
    registered_currencies = []

    def register_currency(self, manager, cur_name, initial_value):
        self.currencies.append(cur_name)
        manager.register_rate(cur_name, initial_value)

    def get_default_rate(self, from_cur, to_cur):
        manager.get
