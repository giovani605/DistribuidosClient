import requests
import json
urlPassagem = 'http://localhost:8080/passagem'
urlPassagemId = 'http://localhost:8080/passagem/id'
urlHotelGetID = 'http://localhost:8080/hotel/id'
urlHotelGet = 'http://localhost:8080/hotel'


def imprimePassagem(passagem):
    print("ID: " + str(passagem['id']))
    print("Origem:" + str(passagem['origem']))
    print("Destino:" + str(passagem['destino']))
    print("Data:" + str(passagem['data']))
    print("Data Volta:" + str(passagem['dataVolta']))
    print("Passagens disponiveis:" + str( passagem['limite'] - passagem['numero']))
    print("Tipo:" + str(passagem['tipo']))
    print("-=-=-=-=-=-=-=-")

def imprimeHotel(hotel):
    print("ID:" + str(hotel['id']))
    print("Local:" + str(hotel['local']))
    print("checkin:" + str(hotel['checkin']))
    print("checkout:" + str(hotel['checkout']))
    print("Quartos Disponiveis:" + str(hotel['limite'] - hotel['numero']))
    print("-=-=-=-=-=-=-=-")

entrada = -1
while entrada != 0:
    print('''
    [1]Listar Passagens
    [2]Filtrar Passagens
    [3]Comprar Passagens
    [4]Listar Hoteis
    [5]Filtrar Hoteis
    [6]Reservar Hoteis
    [0]SAIR
    ''')
    entrada=int(input('Qual das opcoes deseja?'))
    try:
        if (entrada==1):
            # executa o request
            resp = requests.get(urlPassagem)
            # transforma o request em json
            respdec=resp.json()
            certo = respdec['dados']
            for passagem in certo:
                imprimePassagem(passagem)

        elif (entrada==2):
            data = input("Data da viagem: ")
            origem = input("Origem: ")
            destino = input("Destino: ")
            dataVolta = input("Data Volta: ")
            opcao = input("Opção (ida ou ida e volta): ")
            parametros = (('data', data), ('origem', origem), ('destino', destino), ('dataVolta',dataVolta),('opcao',opcao))
            # executa os requests passandos os parametros
            resp = requests.get(urlPassagem, params=parametros)
            respdec=resp.json()
            print("-=-=-=-=-=-=-=-")
            dados = respdec['dados']
            for passagem in dados:
                imprimePassagem(passagem)

        elif (entrada==3):
            id = input("Digite o ID da passamgem: ")
            bandeira = input("Bandeira do cartão:")
            parcelas = input("Parcelas:")
            idade = input("Idade: ")
            qtd = input("Quantidade Pessoas: ")
            ## passo os parametros via body
            r = requests.post(url='http://localhost:8080/passagem/'+id, json={"cartao": bandeira, "parcela": parcelas, "idade": idade, "numeroPessoas": qtd})
            print(r.json()["message"])

        elif (entrada==4):
            resp = requests.get(urlHotelGet)
            respdec=resp.json()
         ##   print (len(respdec))
         ##   print (respdec)
            certo = respdec['dados']
            for hotel in certo:
                imprimeHotel(hotel)
        elif (entrada == 5):
            local = input("Local: ")
            checkin = input("checkin: ")
            checkout = input("checkout: ")
            parametros = (('local', local), ('checkin', checkin), ('checkout', checkout))
            # executa os requests passandos os parametros
            resp = requests.get(urlHotelGet, params=parametros)
            respdec = resp.json()
            print("-=-=-=-=-=-=-=-")
            dados = respdec['dados']
            for hotel in dados:
                imprimeHotel(hotel)

        elif (entrada==6):
            id = input("ID: ")
            quartoh = input("Quantidade de quartos: ")
            bandeirah = input("Bandeira do cartão:")
            parcelash = input("Parcelas:")
            r = requests.post(url='http://localhost:8080/hotel/' + id, json={"qtdQuartos": quartoh, "cartao": bandeirah, "parcela": parcelash})
            print (r.json()["message"])

        elif (entrada==0):
            print("Finalizando...")

        else:
            print("Entrada inválida!!")
    except:
        print("Problemas no Web services")