def razao_bissetriz(b, c):
    # Verificação básica de divisão por zero
    if c == 0:
        return "Erro: o lado c não pode ser zero."
    
    # Cálculo da razão
    razao = b / c
    return razao

def main():
    # Entrada dos lados
    a = float(input("Digite o lado a (oposto ao ângulo A): "))
    b = float(input("Digite o lado b (oposto ao ângulo B): "))
    c = float(input("Digite o lado c (oposto ao ângulo C): "))
    
    # Verificação da validade do triângulo
    if a + b <= c or a + c <= b or b + c <= a:
        print("Erro: os lados fornecidos não formam um triângulo válido.")
    else:
        # Cálculo da razão para a bissetriz interna
        razao_interna = razao_bissetriz(b, c)
        print("A razão dos segmentos formados pela bissetriz interna é:", razao_interna)

        # Cálculo da razão para a bissetriz externa
        razao_externa = razao_bissetriz(b, c)
        print("A razão dos segmentos formados pela bissetriz externa é:", razao_externa)

main()
