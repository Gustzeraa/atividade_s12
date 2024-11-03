def calcular_idades(idade_homem1, idade_homem2, idade_mulher1, idade_mulher2):
    # Valida se as idades são números inteiros positivos
    for idade in [idade_homem1, idade_homem2, idade_mulher1, idade_mulher2]:
        if not isinstance(idade, int) or idade <= 0:
            return "Erro: Todas as idades devem ser números inteiros positivos."

    # Identifica o homem mais velho e o mais novo
    homem_mais_velho = max(idade_homem1, idade_homem2)
    homem_mais_novo = min(idade_homem1, idade_homem2)

    # Identifica a mulher mais velha e a mais nova
    mulher_mais_velha = max(idade_mulher1, idade_mulher2)
    mulher_mais_nova = min(idade_mulher1, idade_mulher2)

    # Calcula a soma e o produto conforme as regras
    soma_idades = homem_mais_velho + mulher_mais_nova
    produto_idades = homem_mais_novo * mulher_mais_velha

    return {
        "Soma das idades (homem mais velho + mulher mais nova)": soma_idades,
        "Produto das idades (homem mais novo * mulher mais velha)": produto_idades
    }

# Exemplo de uso
resultado = calcular_idades(30, 25, 22, 28)
print(resultado)
