print(f"seja muito bem vindo!")
N1=float(input("Quanto você ganha por hora?: "))
N2=float(input("Quantas horas você trabalha no mês?: "))

N3 = (N1*N2)

IPR = (N3 * 11) / 100

INSS = (N3 * 8) / 100

SDC = (N3 * 5) / 100

print(f" seu salário bruto por mês é de {N3} reais")

print(f" Você pagou {INSS} reais ao inss")

print(f" Você pagou {SDC} reais ao sindicato")

print(f" Você pagou {IPR} reais ao imposto de renda")

liquido = (N3 - INSS-SDC-IPR)

print(f" seu salário liquido por mês é de {liquido} reais")