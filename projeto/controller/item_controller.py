from dao.item_dao import ItemDAO
from model.item import Item

class ItemController:
    def __init__(self):
        self.dao = ItemDAO()

    def criarItem(self, descricao, quantidade):
        item = Item(descricao=descricao, quantidade=quantidade)
        self.dao.adicionar(item)

    def obterTodosOsItens(self):
        return self.dao.listarTodos()
