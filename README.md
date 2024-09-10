# Controle de Estoque com Aprendizado por Reforço

Este projeto implementa uma solução de **Aprendizado por Reforço (Reinforcement Learning - RL)** para resolver um problema de controle de estoque. O objetivo é treinar um agente para aprender a melhor política de gerenciamento dos níveis de estoque em uma loja, considerando as probabilidades de venda, custos de manutenção e custos de entrega.

## Tabela de Conteúdos

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Instalação](#instalação)
- [Uso](#uso)
- [Treinamento do Agente](#treinamento-do-agente)
- [Avaliação](#avaliação)
- [Tecnologias](#tecnologias)
- [Licença](#licença)

## Visão Geral

Neste projeto, simulamos o sistema de estoque de uma loja usando **Aprendizado por Reforço**. O agente aprende a gerenciar o estoque de forma eficiente, maximizando os lucros das vendas e minimizando os custos associados à manutenção do estoque e às entregas.

O ambiente modela:
- **Níveis de estoque**: O número de itens disponíveis na loja (0, 1 ou 2).
- **Vendas**: A probabilidade de venda de um item em qualquer dia é `p(sale) = 0.3`.
- **Custos**: Os custos de manutenção aumentam conforme o nível de estoque aumenta, e há uma taxa fixa de entrega quando novos produtos são pedidos.

### Políticas:
Nós comparamos diferentes políticas:
- Reabastecer sempre que o estoque estiver abaixo da capacidade.
- Reabastecer apenas quando o estoque estiver zerado.
- Reabastecimento aleatório.

O objetivo é determinar qual é a estratégia de gerenciamento de estoque mais eficaz.

## Funcionalidades

- Simula um sistema de estoque com vendas estocásticas.
- Implementa um ambiente usando **OpenAI Gym**.
- Treina um agente de aprendizado por reforço usando a biblioteca **Stable-Baselines3**.
- Compara diferentes políticas de gerenciamento de estoque.

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/inventory-rl.git
   ```

2. Crie um ambiente e ative-o:
   ```
   python -m venv venv
   source venv\bin\activate # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```

4. Navegue até o diretório do projeto:
   ```
   cd inventory-rl
   ```
