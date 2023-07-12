class calculate():

    def choices(self):
        print("digite qual operacao deseja realizar\n"
              "     Digite o numero  1 para a soma de dois valores\n"
              "     Digite o numero 2 Para substracao de dois valores\n"
              "     Digite o numero  3 para a divisao de dois valores \n"
              "     Digite o numero 4  para a multiplicacao de dois valores \n")
        conteudo = int(input("Coloque o numero correspondente: "))
        if conteudo == 1:
           return self.somatoria()
        elif conteudo == 2:
            return self.subtrai()
        elif conteudo == 3:
            return self.divide()
        elif conteudo == 4:
            return self.multiplica()
        else:

            print("ERRO, Valor digitado incorreto ou Nao encontrado")

        return

    def somatoria(self):
        print("Digite um valor:")
        valor1 = int(input())
        print("Digite o segundo valor")
        valor2 = int(input())
        somaa = valor1 + valor2
        print("A soma dos valores é ", somaa)

    def subtrai (self):
        print("Digite um valor:")
        valor1 = int(input())
        print("Digite o segundo valor")
        valor2 = int(input())
        subtracao = valor1 - valor2
        print("A subtracao dos valores é ", subtracao)

    def divide(self):
        print("Digite um valor:")
        valor1 = int(input())
        print("Digite o segundo valor")
        valor2 = int(input())
        divide = valor1 / valor2
        print("A divisao dos valores é ", divide)

    def multiplica(self):
        print("Digite um valor:")
        valor1 = int(input())
        print("Digite o segundo valor")
        valor2 = int(input())
        multiplica = valor1 * valor2
        print("A Multiplicacao dos valores é ", multiplica)


# Criar uma instância da classe
calc = calculate()
# Chamar o método choices() na instância
calc.choices()