import requests
import json
url = 'http://localhost:8080/passagem'
urli = 'http://localhost:8080/passagem/id'
urlhi = 'http://localhost:8080/hotel/id'
urlh = 'http://localhost:8080/hotel'

#   http://localhost:8080/
#/passagem      - get    lista de todas as passagens    #id / data / origem / destino / numero / tipo
#/passagem/id   - get    retorna as informacoes da passagem guarda no id
#/passagem/id   - post   Envia Json com as variaveis "cartao" : "visa","parcela" : "2x","idade" : "10"

#r= requests.get(url)
#x=r.json()

entrada = -1
while entrada != 0:
    print('''
    [1]Listar Passagens
    [2]Filtrar Passagens
    [3]Comprar Passagens
    [4]Listar Hotel
    [5]Reservar Hotel
    [0]SAIR
    ''')
    entrada=int(input('Qual das opcoes deseja?'))

    if (entrada==1):
        resp = requests.get(url)
        respdec=resp.json()
       ## print (len(respdec))
       ## print (respdec)
        certo = respdec['dados']
        rang=int (len(certo))
        for i in range (0, rang):
            print("id:" + str(certo[i]['id']))
            print("data:" + str(certo[i]['data']))
            print("data:" + str(certo[i]['dataVolta']))
            print("origem:" + str(certo[i]['origem']))
            print("destino:" + str(certo[i]['destino']))
            print("numero:" + str(certo[i]['numero']))
            print("tipo:" + str(certo[i]['tipo']))
            print("-=-=-=-=-=-=-=-")

    if (entrada==2):

        data = input("Data da viagem: ")
        origem = input("Origem: ")
        destino = input("Destino: ")
        dataVolta = input("Data Volta: ")
        opcao = input("Opção (ida ou ida e volta): ")
        parametros = (('data', data), ('origem', origem), ('destino', destino), ('dataVolta',dataVolta),('opcao',opcao))
        resp = requests.get(url, params=parametros)
        respdec=resp.json()
       ## print (len(respdec))
       ## print (respdec)
        certo = respdec['dados']
        rang=int (len(certo))
        print("-=-=-=-=-=-=-=-")
        for i in range (0, rang):
            print("id:"+ str(certo[i]['id']))
            print("data:" + str(certo[i]['data']))
            print("data:" + str(certo[i]['dataVolta']))
            print("origem:" + str(certo[i]['origem']))
            print("destino:" + str(certo[i]['destino']))
            print("numero:" + str(certo[i]['numero']))
            print("tipo:" + str(certo[i]['tipo']))
            print("-=-=-=-=-=-=-=-")

    elif (entrada==3):
        id = input("Digite o ID da passamgem: ")
        bandeira = input("Bandeira do cartão:")
        parcelas = input("Parcelas:")
        idade = input("Idade: ")
        qtd = input("Quantidade Pessoas: ")
        r = requests.post(url='http://localhost:8080/passagem/'+id, json={"cartao": bandeira, "parcela": parcelas, "idade": idade, "numeroPessoas": qtd})
        print(r.json()["message"])

    elif (entrada==4):
        resp = requests.get(url)
        respdec=resp.json()
     ##   print (len(respdec))
     ##   print (respdec)
        certo = respdec['dados']
        rang=int (len(certo))
        for i in range (0, rang):
            print("id:"+ str(certo[i]['id']))
            print("data:" + str(certo[i]['data']))
            print("local:" + str(certo[i]['local']))
            print("numero:" + str(certo[i]['numero']))
            print("-=-=-=-=-=-=-=-")

    elif (entrada==5):
        datah = input("Data de saida: ")
        quartoh = input("Quantidade de quartos: ")
        bandeirah = input("Bandeira do cartão:")
        parcelash = input("Parcelas:")
        idadeh = input("Idade")
        r = requests.post(url='http://localhost:8080/hotel/1', json={"dataSaida": datah, "qtdQuartos": quartoh, "cartão": bandeirah, "parcela": parcelash,"idade": idadeh })
        print (r.status_code)

    elif (entrada==0):
        print("Finalizando...")

    else:
        print("Entrada inválida!!")