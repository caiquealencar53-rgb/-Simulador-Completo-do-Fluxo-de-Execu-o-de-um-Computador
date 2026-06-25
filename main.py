from computador import Computador


def main():
    pc = Computador()

    print("=== Simulador do Fluxo de Execução de um Computador ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        pc.executar()
        print("-" * 50)

        continuar = input("Fazer outra operação? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando o simulador...")
            break


if __name__ == "__main__":
    main()