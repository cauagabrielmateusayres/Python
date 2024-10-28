import os

# Inicializando variáveis
idade = 0
altura = 0
peso = 0.0

# Perguntando o sexo do usuário
sexo = input('Digite se você é homem(1) ou mulher(2): ')
os.system('cls')
if sexo == '1':
    idade = int(input('Digite sua idade: '))
    os.system('cls')
    altura = float(input('Digite sua altura (cm): ')) / 100
    os.system('cls')
    peso = float(input('Digite seu peso (kg): '))
    os.system('cls')

    # Calculando a Taxa Metabólica Basal (TMB) para homens
    tmb = (13.75 * peso) + (5 * altura * 100) - (6.75 * idade) + 66.5
else:
    idade = int(input('Digite sua idade: '))
    os.system('cls')
    altura = float(input('Digite sua altura (cm): '))
    os.system('cls')
    peso = float(input('Digite seu peso (kg): '))
    os.system('cls')
    
    # Calculando a Taxa Metabólica Basal (TMB) para mulheres
    tmb = (9.56 * peso) + (1.85 * altura * 100) - (4.68 * idade) + 65.7

# Inicializando a lista de atividades físicas
atividades_fisicas = []

# Perguntando quantas atividades o usuário faz
quantidade = int(input('Quantas atividades físicas você faz no dia? '))


# Coletando informações sobre cada atividade
for i in range(quantidade):
    atividade = input(f'Digite o nome da atividade {i + 1}: ')
    intensidade = input('Qual a intensidade da atividade? (leve, moderada, alta): ').lower()
    os.system('cls')
    
    # Armazenando a atividade e a intensidade
    atividades_fisicas.append({'atividade': atividade, 'intensidade': intensidade})

# Calculando o Total de Calorias Gastas por Dia (TMT)
fator_intensidade = 1.0  # Fator inicial

# Atribuindo fatores com base na intensidade
for atividade in atividades_fisicas:
    if atividade['intensidade'] == 'leve':
        fator_intensidade += 0.3
    elif atividade['intensidade'] == 'moderada':
        fator_intensidade += 0.5
    elif atividade['intensidade'] == 'alta':
        fator_intensidade += 0.7

# Calculando TMT
tmt = tmb * fator_intensidade

# Perguntando ao usuário se ele quer déficit ou superávit calórico
objetivo = input('Você deseja um déficit calórico ou superávit? (digite "déficit" ou "superávit"): ').lower()

# Definindo as calorias com base no objetivo
if objetivo == 'déficit':
    calorias_recomendadas = tmt - 400  # Exemplo de déficit de 400 calorias
    print(f'Para um déficit calórico, você deve consumir cerca de {calorias_recomendadas:.2f} calorias por dia.')
    # Aumento na proteína durante o déficit
    proteinas = calorias_recomendadas * 0.30 / 4  # 30% para proteínas
    lipidios = calorias_recomendadas * 0.25 / 9    # 25% para lipídios
    carboidratos = calorias_recomendadas * 0.45 / 4  # 45% para carboidratos
elif objetivo == 'superávit':
    calorias_recomendadas = tmt + 400  # Exemplo de superávit de 400 calorias
    print(f'Para um superávit calórico, você deve consumir cerca de {calorias_recomendadas:.2f} calorias por dia.')
    # Ajuste na proteína durante o superávit
    proteinas = calorias_recomendadas * 0.25 / 4  # 25% para proteínas
    lipidios = calorias_recomendadas * 0.25 / 9    # 25% para lipídios
    carboidratos = calorias_recomendadas * 0.50 / 4  # 50% para carboidratos
else:
    print('Opção inválida. Por favor, escolha "déficit" ou "superávit".')
    exit()  # Encerra o programa se a opção for inválida

# Exibindo os resultados dos macronutrientes
print(f'\nPara atingir sua meta calórica você deve consumir aproximadamente:\n')
print(f'{proteinas:.2f} gramas de proteínas')
print(f'{lipidios:.2f} gramas de lipídios')
print(f'{carboidratos:.2f} gramas de carboidratos\n')


# Exibindo o total de calorias gastas
print(f'Total de calorias gastas por dia: {tmt:.2f} calorias')