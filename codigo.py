#Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 1.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

site = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(site)
pyautogui.press('enter')
time.sleep(3)

#Passo 2: Fazer login
pyautogui.click(x=727, y=377)
pyautogui.write('nath_2002@gmail.com')
pyautogui.press('tab')
pyautogui.write('12345')
pyautogui.press('enter')
time.sleep(3)

#Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('produtos.csv')

#Passo 4: Cadastrar 1 produto
for linha in tabela.index:
    #clicar no campo a ser preenchido 
    pyautogui.click(x=708, y=261)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    obs = tabela.loc['obs']
    if not pd.isna(obs): 
        pyautogui.write(str(tabela.loc[linha, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter') #Cadastra o produto 
    pyautogui.scroll(5000) #Da scroll de tudo para cima


#Passo 5: Repetir o processo de cadastro até acabar os produtos

