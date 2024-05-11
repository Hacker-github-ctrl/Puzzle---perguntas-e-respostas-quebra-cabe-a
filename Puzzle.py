#!/usr/bin/env python3
#coding utf-8
#Algoritmo
import os
import time
import random

#cores utilizados no Python
Amarelo = '\33[93m'
Azul = '\33[94m'
Verde = '\33[92m'
Vermelho = '\33[91m'

#Banner do primeiro painel
def banner(PYTHON):
    #Banner do painel em Python
    print(Amarelo, "Cicada3301, Puzzles em Python")
    print(Vermelho, "é um enigma díficil")
    print(Amarelo,'████───────────────────────────████')
    print(Amarelo,'─██████────────░█───█░────────██████')
    print(Amarelo,'──██?▓████─────██───██─────████▓?██')
    print(Amarelo,'───██?░░▓███─────█─█─────███▓░░?██')
    print(Amarelo,'───██?░░░░▓███───█─█───███▓░░░░?██')
    print(Amarelo,'────██?░?░░░▓██──███──██▓░░░?░?██')
    print(Amarelo,'────██?░░░?░░▓███─█─██▓░░░?░░░?██')
    print(Amarelo,'───██?░░?░░░?░░▓█████▓░░?░░░?░░?██')
    print(Amarelo,'───██?░░░░░░░░?░▓███▓░?░░░░░░░░?██')
    print(Amarelo,'───█████████▒░░░░▓█▓░░░░▒█████████')
    print(Amarelo,'─────█████████▒░░▒█▒░░▒█████████')
    print(Amarelo,'──███?░░░░░░░██░░▓█▓░░██░░░░░░░?███')
    print(Amarelo,'───███?░░?░?░░░░░███░░░░░?░?░░?███')
    print(Amarelo,'─────██?░░░░░?░░▓███▓░░?░░░░░?██')
    print(Amarelo,'──────██?░?░░░░▓█████▓░░░░?░?██')
    print(Amarelo,'──────██?░░░▓████─█─████▓░░░?██')
    print(Amarelo,'───────██?▓███────█────███▓?██')
    print(Amarelo,'──────██████───────────██████')
    print(Amarelo,'────────███──────────────████')
    print()
    
    #Lista de respostas
    respostas = ["goku", "naruto", "luffy", "meliodas", "saitama"]
    bônus = 0

    #Entrada da pergunta
    try:
        pergunta1 = str(input('Quem ganha ? (naruto ou luffy): '))
        if str(pergunta1) == "luffy":
            bônus += 1
            print('Parabens !')
            print(f'+{bônus}+ Bônus !')

            #Condição1
        elif str(pergunta1) == "naruto":
            bônus -= 1
            print('Errou !')
            print(f'{bônus} Bônus !')

        #puzzle2
        pergunta2 = input('Quem ganha ? (meliodas ou goku: ) ')
        if str(pergunta2) == "goku":
            bônus += 1
            print('Parabens !')
            print(f'+{bônus} Bônus !')
        #Condição2
        elif str(pergunta2) == 'meliodas':
            bônus -= 2
            print('Errou !')
            print(f'{bônus} Bônus !')
        
        #puzzle3    
        pergunta3 = input('Quem ganha ? (goku ou saitama: )')
        if str(pergunta3) == "saitama":
            bônus += 1
            print('Parabens !')
            print(f'+{bônus} Bônus !')
        #Condição3
        elif str(pergunta3) == 'goku':
            bônus -= 1
            print("Errou !")
            print(f'{bônus} Bônus')  
        
        #Saída
        média = bônus + bônus + bônus
    
        print(f"{Azul}A média obtido pelo Puzzles é de {média:.2f} pontos por Cálculos!")
          
    except ValueError:
        print("Não é possivel fazer isso !")

two = banner('PYTHON')    
#proximo painel
#painel nome
#Python.org
time.sleep(3)
os.system('cls')

def proximo_painel(nome):
    print('___'*12)
    print('Olá Mundo!')
    print('___'*12)
    print()
    
    nome = input('Qual é o seu nome ?: ')
    if nome != "":
        print(Verde, "Olá", nome)
        print("Vc fez bem em vir até aqui, a paciência é uma virtude !")
        print("Irei lançar mais Puzzles tipo estilo Cicada3301.")
        print("Caso queira se tornar um Programador(a) ou um(a) Hacker Ético -> https://hackersec.com/  ")
        print("Me segue no instagram -> https://www.instagram.com/ethicalhacking9979?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==")
        print("Sou Programador Python.")
    else:
        print("Digite novamente !")
        exit()
    return nome
#Saída
proximo = proximo_painel('nome')
#boa sorte
#deixarei um código qrcode
#Cicada3301
#PYTHON.ORG
#Python, C++, Java
#JavaScript, C, C#
#Matlab
#ETHICAL HACKING, PENTEST, BUG_BOUNTY
#PROGRAMAÇÃO DE COMPUTADORES, ALGORITMOS E LÓGICA DE PROGRAMAÇÃO E RESOLUÇÃO DE PROBLEMAS.
