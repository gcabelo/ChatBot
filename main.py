from chatbot import ChatBot

myChatBot = ChatBot()
# apenas carregar um modelo pronto
#myChatBot.loadModel()

# criar o modelo
myChatBot.createModel()

print("Bem vindo ao Chatbot")

pergunta = input("como posso te ajudar?")
resposta, intencao = myChatBot.chatbot_response(pergunta)


while True:
    controle = 0

    # Tentativa de realizar o encadeamento
    if pergunta == "O que esperar como resultado final do TCC?" or pergunta == "O que devo entregar no final do semestre?"  or pergunta == "Qual documento devo entregar no final do semestre?":

        print(resposta + "   [" + intencao[0]['intent'] + "]")
        pergunta = input("\nDeseja saber mais informacoes sobre o tema? [SIM/NÃO]")
        resposta, intencao = myChatBot.chatbot_response(pergunta)

        controle = 1

        # Retorna a descrição e pede para o usuário fazer uma nova pergunta
        if (pergunta == 'Sim' or pergunta == 'SIM' or pergunta == 'sim' or pergunta == 'S' or pergunta == 's') and controle == 1:
            print(resposta + "   [" + intencao[0]['intent'] + "]")

            pergunta = input("\nposso lhe ajudar com algo a mais?")
            resposta, intencao = myChatBot.chatbot_response(pergunta)

        # Pede para o usuário fazer uma nova pergunta
        elif pergunta == 'Não' or pergunta == 'NÃO' or pergunta == 'não' or pergunta == 'Nao' or pergunta == 'NAO'\
                or pergunta == 'nao' or pergunta == 'N' or pergunta == 'n':
            pergunta = input("\nposso lhe ajudar com algo a mais?")
            resposta, intencao = myChatBot.chatbot_response(pergunta)

        # Se a pergunta não for nos padrões válidos, vai pedir para ela realizar uma nova pergunta
        else:
            print('Não entendi, tente novamente')

            pergunta = input("\nposso lhe ajudar com algo a mais?")
            resposta, intencao = myChatBot.chatbot_response(pergunta)

    # Caso a intenção for de despedida, encerra o código
    elif intencao[0]['intent'] == "despedida":
        print(resposta + "   [" + intencao[0]['intent'] + "]")
        break

    # Não libera a descrição
    elif (pergunta == 'Sim' or pergunta == 'SIM' or pergunta == 'sim' or pergunta == 'S' or pergunta == 's') and controle == 0:
        print('Não entendi, tente novamente')

        pergunta = input("\nposso lhe ajudar com algo a mais?")
        resposta, intencao = myChatBot.chatbot_response(pergunta)

    # Se a pergunta for nos padrões válidos
    else:
        print(resposta + "   [" + intencao[0]['intent'] + "]")

        pergunta = input("\nposso lhe ajudar com algo a mais?")
        resposta, intencao = myChatBot.chatbot_response(pergunta)

print("Foi um prazer atendê-lo")