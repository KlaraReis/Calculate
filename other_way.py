class OtherCalculate:

    def choices(self):
        print("Which operation do you want to perform?\n"
              "    Type 1 for sum of two values \n"
              "    Type 2 for subtraction of two values\n"
              "    Type 3 for a division of two values \n"
              "    Type 4 for a multiplication of two values \n")
        choice = int(input("Enter the corresponding number: "))

        if choice == 1:
            result = self.addition()
            print("The sum of the values is", result)

        elif choice == 2:
            result = self.subtraction()
            print("The subtraction of the values is", result)

        elif choice == 3:
            result = self.division()
            print("The division of the values is", result)

        elif choice == 4:
            result = self.multiplication()
            print("The multiplication of the values is", result)

        else:
            print("ERROR: Invalid choice.")

    def get_value(self, value_name):
        return int(input("Enter the {} value: ".format(value_name)))

    def addition(self):
        value1 = self.get_value("first")
        value2 = self.get_value("second")
        return value1 + value2

    def subtraction(self):
        value1 = self.get_value("first")
        value2 = self.get_value("second")
        return value1 - value2

    def division(self):
        value1 = self.get_value("first")
        value2 = self.get_value("second")
        return value1 / value2

    def multiplication(self):
        value1 = self.get_value("first")
        value2 = self.get_value("second")
        return value1 * value2


calc = OtherCalculate()
calc.choices()