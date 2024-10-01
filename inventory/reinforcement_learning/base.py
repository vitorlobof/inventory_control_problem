import numpy as np
import matplotlib.pyplot as plt

# Definir parâmetros
p_sale = 0.3  # Probabilidade de uma venda por dia
max_stock = 2  # Estoque máximo de 2 unidades
custo_manutencao_1 = 1  # Custo de manter 1 ou nenhuma unidade
custo_manutencao_2 = 2 * custo_manutencao_1  # Custo de manter 2 unidades
custo_entrega = 5  # Custo de entrega para reabastecer

# Definir políticas


def politica_continua(stock):
    return stock < max_stock  # Reabastece se o estoque for menor que 2


def politica_zerado(stock):
    return stock == 0  # Reabastece apenas se o estoque for 0


def politica_aleatoria(stock):
    return np.random.choice([True, False])  # Reabastece aleatoriamente

# Simular o ambiente


def simular_politica(politica, dias=1000):
    estoque = max_stock
    recompensa_acumulada = 0
    historico_recompensas = []

    for dia in range(dias):
        # Calcular custo de manutenção
        if estoque == 2:
            custo_diario = custo_manutencao_2
        else:
            custo_diario = custo_manutencao_1

        # Calcular vendas
        venda = np.random.choice([True, False], p=[p_sale, 1 - p_sale])
        if venda and estoque > 0:
            recompensa_acumulada += 10  # Ganha 10 por venda
            estoque -= 1

        # Ação da política
        if politica(estoque):
            estoque = min(estoque + 1, max_stock)
            recompensa_acumulada -= custo_entrega  # Paga taxa de entrega

        # Subtrair custo de manutenção
        recompensa_acumulada -= custo_diario
        historico_recompensas.append(recompensa_acumulada)

    return historico_recompensas


# Simular as políticas
dias = 1000
recompensas_continua = simular_politica(politica_continua, dias)
recompensas_zerado = simular_politica(politica_zerado, dias)
recompensas_aleatoria = simular_politica(politica_aleatoria, dias)

# Plotar os resultados
plt.figure(figsize=(10, 6))
plt.plot(recompensas_continua, label='Política Contínua (Sempre reabastece)')
plt.plot(recompensas_zerado, label='Política Reabastece ao Zerado')
plt.plot(recompensas_aleatoria, label='Política Aleatória')
plt.xlabel('Dias')
plt.ylabel('Recompensa Acumulada')
plt.legend()
plt.title('Comparação de Políticas de Reabastecimento')
plt.show()
