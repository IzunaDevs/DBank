DEFAULT = 0


class Currency:
    def __init__(self, name, relative_value):
        self.name = name
        self.relative_value = relative_value

    def update_value(self, value):
        self.relative_value = value


class RateManager:
    currencies = {}

    def register(self, cur, val):
        self.currencies[cur] = Currency(cur, val)

    def __getitem__(self, name):
        return self.currencies[name]

    def __setitem__(self, name, value):
        self.currencies[name] = value


def check(func):
    def inner(self, *args, **kwargs):
        for a in args:
            assert self.check_rate(a)

        return func(*args, **kwargs)
    return inner


class Converter:
    currencies = []

    def register_currency(self, manager, cur_name, initial_value):
        self.currencies.append(cur_name)
        self.manager = manager
        manager.register_rate(cur_name, initial_value)

    def check_rate(self, cur_name):
        return cur_name in self.currencies

    @check
    def get_rate(self, from_cur, to_cur):
        c = self.manager.get_currency(from_cur)
        t = self.manager.get_currency(to_cur)
        return c.rate / t.rate

    @check
    def update_rate(self, curname, value=0):
        c = self.manager.get_currency(curname)
        c.update_value(value)
