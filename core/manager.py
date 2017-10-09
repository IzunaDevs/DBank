from .utils import JSONFile


class Manager:
    def __init__(self, data_file: str = "data.json", loop=None):
        self.data_file = JSONFile(data_file, loop)
        self.converter

    def get_data(self, id: str):
        data = self.data.get(id)
        if data is None:
            self.init_data(id)

    def get_currencies(self):
        return [self.cur_manager[x] for x in self.converter.currencies]
