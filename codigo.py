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
#Passo 3: Importar a base de dados
#Passo 4: Cadastrar 1 produto
#Passo 5: Repetir o processo de cadastro até acabar os produtos

