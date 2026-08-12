from locadora import Locadora
from veiculo import Veiculo
from cliente import Cliente


def menu():
    locadora = Locadora()
    locadora.cadastrar_veiculo(Veiculo("ABC1234", "Onix", 120.0))
    locadora.cadastrar_veiculo(Veiculo("XYZ9988", "HB20", 100.0))
    locadora.cadastrar_cliente(Cliente("Henrique", "111.222.333-44"))

    while True:
        print("\n1 - Alugar veículo")
        print("2 - Devolver veículo")
        print("3 - Ver histórico do cliente")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Placa do veículo: ")
            cpf = input("CPF do cliente: ")
            dias = input("Quantidade de dias: ")
            valor = locadora.alugar_veiculo(cpf, placa, dias)
            print(f"Valor total: R${valor:.2f}")

        elif opcao == "2":
            placa = input("Placa do veículo: ")
            locadora.devolver_veiculo(placa)

        elif opcao == "3":
            cpf = input("CPF do cliente: ")
            cliente = locadora.buscar_cliente(cpf)
            cliente.historico()

        elif opcao == "4":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


menu()
