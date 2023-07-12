class betterCalculate():

    def choices(self):
        print("Which operation do you want to perform?\n"
              "     Type 1 for sum of two values \n"
              "     Type 2 for subtraction of two values\n"
              "     Type 3 for a division of two values \n"
              "     Type 4 for a multiplication of two values \n")
        conteudo = int(input("Enter the corresponding number: "))
        if conteudo == 1:
           soma = self.get_first_value() + self.get_second_value()
           print("The sum of values is  ", soma)

        elif conteudo == 2:
            subtracao = self.get_first_value() - self.get_second_value()
            print("The subtraction  of values is ", subtracao)

        elif conteudo == 3:
            divide = self.get_first_value() / self.get_second_value()
            print("The division of values is ", divide)

        elif conteudo == 4:
            multiplica = self.get_first_value() * self.get_second_value()
            print("The multiplication of values is ", multiplica)
        else:

            print("ERROR: Invalid choice.")

        return

    def get_first_value(self):
        print("Type the first value")
        valor1 = int(input())
        return valor1

    def get_second_value(self):
        print("Type the second value")
        valor2 = int(input())
        return valor2


# Criar uma instância da classe
calc = betterCalculate()
# Chamar o método choices() na instância
calc.choices()