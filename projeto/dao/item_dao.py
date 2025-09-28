from model.item import Item
from database.con import criar_conexao

class ItemDAO:
    def adicionar(self, item: Item):
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO itens (descricao, quantidade) VALUES (?, ?)",
            (item.get_descricao(), item.get_quantidade())
        )
        conn.commit()
        conn.close()

    def listarTodos(self) -> list:
        conn = criar_conexao()
        cursor = conn.cursor()
        cursor.execute("SELECT id, descricao, quantidade FROM itens")
        rows = cursor.fetchall()
        conn.close()

        itens = []
        for row in rows:
            id, descricao, quantidade = row
            itens.append(Item(descricao=descricao, quantidade=quantidade, id=id))
        return itens
