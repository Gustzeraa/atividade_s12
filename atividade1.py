# Importando o módulo math para lidar com arredondamentos nas comparações
import math

# Função para verificar a semelhança usando o critério LAL (Lado-Ângulo-Lado)
def verificar_lal(lado1_triang1, lado2_triang1, angulo_triang1, lado1_triang2, lado2_triang2, angulo_triang2):
    if angulo_triang1 == angulo_triang2:
        proporcao1 = lado1_triang1 / lado1_triang2
        proporcao2 = lado2_triang1 / lado2_triang2
        return math.isclose(proporcao1, proporcao2, rel_tol=1e-9)
    return False

# Função para verificar a semelhança usando o critério AA (Ângulo-Ângulo)
def verificar_aa(angulo1_triang1, angulo2_triang1, angulo3_triang1, angulo1_triang2, angulo2_triang2, angulo3_triang2):
    return (angulo1_triang1 == angulo1_triang2 and angulo2_triang1 == angulo2_triang2) or \
           (angulo1_triang1 == angulo1_triang2 and angulo3_triang1 == angulo3_triang2) or \
           (angulo2_triang1 == angulo2_triang2 and angulo3_triang1 == angulo3_triang2)

# Função para verificar a semelhança usando o critério LLL (Lado-Lado-Lado)
def verificar_lll(lado1_triang1, lado2_triang1, lado3_triang1, lado1_triang2, lado2_triang2, lado3_triang2):
    proporcao1 = lado1_triang1 / lado1_triang2
    proporcao2 = lado2_triang1 / lado2_triang2
    proporcao3 = lado3_triang1 / lado3_triang2
    return math.isclose(proporcao1, proporcao2, rel_tol=1e-9) and math.isclose(proporcao2, proporcao3, rel_tol=1e-9)

# Função principal que solicita as informações e verifica todos os critérios
def verificar_semequeca():
    print("Informe os valores para verificar a semelhança dos triângulos.")

    # Coleta de dados do primeiro triângulo
    lado1_triang1 = float(input("Informe o primeiro lado do triângulo 1: "))
    lado2_triang1 = float(input("Informe o segundo lado do triângulo 1: "))
    lado3_triang1 = float(input("Informe o terceiro lado do triângulo 1: "))
    angulo1_triang1 = float(input("Informe o primeiro ângulo do triângulo 1: "))
    angulo2_triang1 = float(input("Informe o segundo ângulo do triângulo 1: "))
    angulo3_triang1 = float(input("Informe o terceiro ângulo do triângulo 1: "))

    # Coleta de dados do segundo triângulo
    lado1_triang2 = float(input("Informe o primeiro lado do triângulo 2: "))
    lado2_triang2 = float(input("Informe o segundo lado do triângulo 2: "))
    lado3_triang2 = float(input("Informe o terceiro lado do triângulo 2: "))
    angulo1_triang2 = float(input("Informe o primeiro ângulo do triângulo 2: "))
    angulo2_triang2 = float(input("Informe o segundo ângulo do triângulo 2: "))
    angulo3_triang2 = float(input("Informe o terceiro ângulo do triângulo 2: "))

    # Verifica cada critério
    semelhante_lal = verificar_lal(lado1_triang1, lado2_triang1, angulo1_triang1, lado1_triang2, lado2_triang2, angulo1_triang2)
    semelhante_aa = verificar_aa(angulo1_triang1, angulo2_triang1, angulo3_triang1, angulo1_triang2, angulo2_triang2, angulo3_triang2)
    semelhante_lll = verificar_lll(lado1_triang1, lado2_triang1, lado3_triang1, lado1_triang2, lado2_triang2, lado3_triang2)

    # Exibe os resultados
    if semelhante_lal:
        print("Os triângulos são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")
    else:
        print("Os triângulos NÃO são semelhantes pelo critério LAL (Lado-Ângulo-Lado).")

    if semelhante_aa:
        print("Os triângulos são semelhantes pelo critério AA (Ângulo-Ângulo).")
    else:
        print("Os triângulos NÃO são semelhantes pelo critério AA (Ângulo-Ângulo).")

    if semelhante_lll:
        print("Os triângulos são semelhantes pelo critério LLL (Lado-Lado-Lado).")
    else:
        print("Os triângulos NÃO são semelhantes pelo critério LLL (Lado-Lado-Lado).")

# Executa a função principal
verificar_semequeca()
