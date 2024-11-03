def calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos):
    # Percentual fixo sobre o total das vendas
    percentual_vendas = 0.05
    # Bônus sobre o total das vendas para mais de 10 carros vendidos
    bonus_percentual = 0.10 if carros_vendidos > 10 else 0

    if carros_vendidos > 0:
        # Calcula comissão por carro e percentual sobre as vendas
        comissao_total = comissao_por_carro * carros_vendidos
        percentual_total_vendas = total_vendas * percentual_vendas
        bonus = total_vendas * bonus_percentual
        salario_final = salario_fixo + comissao_total + percentual_total_vendas + bonus
    else:
        # Se nenhum carro foi vendido, apenas o salário fixo é recebido
        salario_final = salario_fixo

    return salario_final

# Exemplo de uso
salario_fixo = 2000.00
comissao_por_carro = 150.00
total_vendas = 50000.00
carros_vendidos = 12

salario_final = calcular_salario(salario_fixo, comissao_por_carro, total_vendas, carros_vendidos)
print(f"Salário final do vendedor: R$ {salario_final:.2f}")
