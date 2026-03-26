from datetime import datetime
nome = input ("Nome completo: ").strip().title()

while True:
    sexo = input("Informe seu sexo (masculino/feminino): ").strip().lower()

    if sexo in ["masculino", "feminino"]:
        break
    else:
        print("Sexo inválido. Digite masculino ou feminino.")

while True:
    data_nascimento = input(
        "Data de nascimento (dd/mm/aaaa): "
    ).strip()

    try:
        data = datetime.strptime(
            data_nascimento,
            "%d/%m/%Y"
        )
        break

    except ValueError:
        print("Data inválida. Tente novamente.")

while True:
    anos_contribuicao = input(
        "Quantos anos de contribuição para o INSS? "
    ).strip()  
    
    try:
        anos_contribuicao = int(anos_contribuicao)

        if anos_contribuicao >= 0:
            break
        else:
            print("Digite um número válido: ")

    except ValueError:
        print("Digite apenas números")
        

dia = data.day
mes = data.month
ano = data.year
hoje = datetime.today()

idade = hoje.year - ano

if hoje.month < mes or (hoje.month ==mes and hoje.day < dia):
    idade -= 1

while True:
    trabalho_risco = input("Já operou em trabalho de risco? (sim/não): ").strip().lower()

    if trabalho_risco in ["sim", "não", "nao", "naõ"]:
        break
    else:
        print("Resposta inválida. Digite sim ou não.")

if sexo == "masculino":
    idade_minima = 65
elif sexo == "feminino":
    idade_minima = 60
else: 
    print("Sexo invalidado")

if trabalho_risco =="sim":
    idade_minima -= 10


print("Nome:", nome)    
print("idade:", idade)
print("Idade mínima para aposentadoria:", idade_minima)
if idade >= idade_minima and anos_contribuicao >= 30:
    print("Aposentadoria aprovada.")
else:
    print("Aposentadoria ainda não aprovada.")
