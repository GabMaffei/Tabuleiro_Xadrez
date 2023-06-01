import re


class Genetica:
    def __init__(self):
        self.lista = list()

    def add_genetica(self, gene):
        if re.search('\d{8}', gene):
            self.lista.append(gene)