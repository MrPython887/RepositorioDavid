# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 21:23:40 2023

@author: david
"""

import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title("O Jogo do Galo")
jogador = "X"
tabuleiro = [["" for _ in range(3)] for _ in range(3)]

botoes = []
for linha in range(3):
    linha_botoes = []
    for coluna in range(3):
        botao = tk.Button(janela, text="", width=10, height=5,
                          command=lambda linha=linha, coluna=coluna: fazer_jogada(linha, coluna))
        botao.grid(row=linha, column=coluna)
        linha_botoes.append(botao)
    botoes.append(linha_botoes)
    
    

def fazer_jogada(linha, coluna):
    global jogador
    if tabuleiro[linha][coluna] == "":
        tabuleiro[linha][coluna] = jogador
        botoes[linha][coluna].config(text=jogador)
        if verificar_vitoria(jogador):
            messagebox.showinfo("Fim de jogo", f"Parabéns!! O jogador {jogador} venceu!")
            reiniciar_jogo()
        elif verificar_empate():
            messagebox.showinfo("Fim de jogo", "Que pena ! O jogo terminou em empate!")
            reiniciar_jogo()
            
            
        else:
            jogador = "O" if jogador == "X" else "X"
            
            
#confirmar em caso de vitoria

def verificar_vitoria(jogador):
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
        
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False


#Função de empate


def verificar_empate():
    for linha in tabuleiro:
        if "" in linha:
            return False
    return True


def reiniciar_jogo():
    global jogador
    jogador = "X"
    tabuleiro.clear()
    tabuleiro.extend([["" for _ in range(3)] for _ in range(3)])
    for linha in botoes:
        for botao in linha:
            botao.config(text="")

janela.mainloop()