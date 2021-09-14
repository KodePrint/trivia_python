from os import system
import time
import math
import questions
import random

CATEGORIES = [
    'Artes','Ciencia','Deportes','Entretenimiento',
    'Geografia','Historia','Ingenieria']

def player_register():
    player1 = input('Ingresa el nombre del primer jugador: ')
    print('Bienvenido: ', player1)
    time.sleep(2)
    system('clear')
    player2 = input('Ingresa el nombre del segudo jugador: ')
    print('Bienvenido: ', player2)
    time.sleep(2)
    system('clear')
    players = [
        {
            'name':player1,
            'points':0
        },
        {
            'name':player2,
            'points':0
        }
    ]

    return players


def question_list_select(number):
    if number == 0:
        q_list = questions.ARTES
    elif number == 1:
        q_list = questions.CIENCIA
    elif number == 2:
        q_list = questions.DEPORTES
    elif number == 3:
        q_list = questions.ENTRETENIMIENTO
    elif number == 4:
        q_list = questions.GEOGRAFIA
    elif number == 5:
        q_list = questions.HISTORIA
    elif number == 6:
        q_list = questions.INGENIERIA

    return q_list


def select_question(ronda, questions, players, category):
    for player in players:
        print('Ronda No. ', ronda + 1, '\n')
        print('Categoria: ', category, '\n')
        number = random.randint(0, (len(questions) - 1))

        my_question = questions.pop(number)
        print('Turno del jugador: ', player['name'], '\n')
        # print(number)
        correct_response = my_question['response']
        correct_response = correct_response.upper()

        print(my_question['question'])
        player_response = input('Ingresa tu respuesta: ')
        player_response = player_response.upper()
        # print(correct_response)
        # print(player_response)
        if correct_response == player_response:
            print('Felicidades tu respuesta es correcta..! ✨')
            player['points'] += 1
        else:
            print('Lo siento tu respuesta es incorrecta..! 👻')
            print(f'La respuesta correcta era: {correct_response}')
        time.sleep(2)
        system('clear')
    
    return players


def win_player(players):
    player1 = players[0]
    player2 = players[1]
    if player1['points'] > player2['points']:
        porcentaje = round((player1['points']*100)/7)
        print(f'Felicidades el ganador es: {player1["name"]} con un porcentaje de acierto de {porcentaje}%')
    elif player1['points'] == player2['points']:
        porcentaje = round((player1['points']*100)/7)
        print(f'Felicidades ambos jugadores empataron contestando correctas un total de: {player1["points"]} preguntas')
        porcentaje = round((player2['points']*100)/7)
        print(f'El porcentaje de aciertos fue de {porcentaje}%')
    else:
        porcentaje = round((player2['points']*100)/7)
        print(f'Felicidades el ganador es: {player2["name"]} con un porcentaje de acierto de {porcentaje}%')


if __name__ == '__main__':
    system('clear')
    players = player_register()
    for seq in range(0, 7):
        
        list_question = question_list_select(seq) 
        category = CATEGORIES[seq]
        
        select_question(seq, list_question, players, category)
    win_player(players)
        

