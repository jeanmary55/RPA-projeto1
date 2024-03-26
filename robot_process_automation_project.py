import pyautogui
import time
import pandas as pd




pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')

time.sleep(4)

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3)


pyautogui.click(x=386, y=360)

pyautogui.write('jeanmaryjeanlus29@gmail.com')
pyautogui.press('tab')

pyautogui.write('senha12')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(4)


tabela = pd.read_csv('produtos (1).csv')
for linha in tabela.index :
    time.sleep(2)
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']
    pyautogui.click(x=392, y=246)

    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    pyautogui.write(str(marca))
    pyautogui.press('tab')

    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')

    pyautogui.write(str(custo))
    pyautogui.press('tab')


    if not pd.isna(obs) :
        pyautogui.write(str(obs))
        pyautogui.press('tab')

    pyautogui.press('enter')

    pyautogui.scroll(5000)






