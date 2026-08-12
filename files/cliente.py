class Cliente:
    def __init__(self, nome, cpf, locacoes=[]):
        self.nome = nome
        self.cpf = cpf
        self.locacoes = locacoes

    def adicionar_locacao(self, veiculo, dias):
        self.locacoes.append((veiculo, dias))

    def historico(self):
        if len(self.locacoes) == 0:
            print("Nenhuma locação registrada.")
            return

        for veiculo, dias in self.locacoes:
            print(f"{veiculo.placa} - {dias} dias - R${veiculo.valor_diaria * dias:.2f}")
