def calcular_R(P, Q, M):
    # Condição 1: Se Ana vai, então Bruno vai (P -> Q)
    condicao1 = not P or Q
    
    # Condição 2: Se Ana ou Bruno for, a festa é animada ((P ∨ Q) -> R)
    if P or Q:
        R_cond2 = True
    else:
        R_cond2 = None  # Sem obrigatoriedade para R diretamente
    
    # Condição 3: Se Ana não vai, a festa depende da música de Bruno (¬P -> (M -> R))
    if not P:
        R_cond3 = M  # A festa será animada somente se Bruno trouxer música
    else:
        R_cond3 = R_cond2  # Caso contrário, depende da Condição 2
    
    # Definindo R com base nas condições
    if R_cond2 is not None:
        R = R_cond2  # Se R_cond2 for definido, R deve ser igual a ele
    else:
        R = R_cond3  # Senão, R depende de R_cond3

    return R

# Lista para armazenar combinações e resultados
tabela_verdade = []

# Gerando todas as combinações de valores lógicos para P, Q, M
for P in [True, False]:
    for Q in [True, False]:
        for M in [True, False]:
            R = calcular_R(P, Q, M)
            tabela_verdade.append({'P': P, 'Q': Q, 'M': M, 'R': R})

# Exibindo a tabela verdade
print("Tabela Verdade")
print("P\tQ\tM\tR")
for linha in tabela_verdade:
    print(f"{linha['P']}\t{linha['Q']}\t{linha['M']}\t{linha['R']}")
