import streamlit as st
from controller.item_controller import ItemController

def main():
    st.title("Cadastro de Itens")
    controller = ItemController()

    menu = ["Cadastrar Item", "Listar Itens"]
    escolha = st.sidebar.selectbox("Menu", menu)

    if escolha == "Cadastrar Item":
        st.subheader("Novo Item")
        descricao = st.text_input("Descrição")
        quantidade = st.number_input("Quantidade", min_value=0, step=1)
        if st.button("Salvar"):
            controller.criarItem(descricao, quantidade)
            st.success("Item cadastrado com sucesso")

    elif escolha == "Listar Itens":
        st.subheader("Itens Cadastrados")
        itens = controller.obterTodosOsItens()
        if itens:
            for item in itens:
                st.text(str(item))

        else:
            st.info("Nenhum item cadastrado")
