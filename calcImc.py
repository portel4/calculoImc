class CalcImc:

    def main():
        peso = float(input("Insira seu Peso:"))
        print("-------------------")
        altura = float(input("Insira sua altura:"))

        print("Calculando o seu IMC...")

        imc = peso / (altura ** 2)

        if imc < 18.5:
            print("Magreza") 
        elif imc > 18.5 and imc < 24.9:
            print("Normal")
        elif imc > 24.9 and imc < 30:
            print("Sobrepeso")
        else:
            print("Obesidade")

    if __name__ == "__main__":
        print("Verificando prog")
        app = main()
        app.run()



