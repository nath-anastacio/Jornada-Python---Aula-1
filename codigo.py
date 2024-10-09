#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui

pyautogui.PAUSE = 1.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(site)
pyautogui.press('enter')


#Passo 2: Fazer login
pyautogui.click(x=727, y=377)
pyautogui.write('nath_2002@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345')
pyautogui.press('enter')


#Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')

#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir o processo de cadastro até acabar os produtos

