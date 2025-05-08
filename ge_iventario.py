class iventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado ao iventário.")

    def listar_itens(self):
        print("Itens no iventário")
        if not self.itens:
            print("O iventário está vazio")
        else:
            for i, item in enumerate(self.itens):
                print(f"{i +1}. {item}")

meu_iventario = iventario()

meu_iventario.adicionar_item("Espada de Diamante")
meu_iventario.adicionar_item("Escudo de Madeira")
meu_iventario.adicionar_item("Poção de Cura")
meu_iventario.adicionar_item("Flechas (x20)")
meu_iventario.adicionar_item("Pedregulho")
meu_iventario.adicionar_item("Bloco de Madeira")

meu_iventario.listar_itens()