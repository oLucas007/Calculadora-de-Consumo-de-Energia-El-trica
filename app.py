# Calculadora de Consumo de Energia Elétrica

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal da potência das horas utilizadas nos dias
consumoMensal = (potencia * horasDia * 30) / 1000

# Valor fixo do kWh por R$
valorKwh = 0.82

# Cálculo do custo estimado
custoMensal = consumoMensal * valorKwh

print("\n Calculadora de Consumo Elétrico")
print("-----------------------------------")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custoMensal:.2f}/mês")

