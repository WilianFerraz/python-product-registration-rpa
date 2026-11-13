import time
import pandas as pd
import pyautogui

pyautogui.PAUSE = 0.3

# Open browser and navigate to system URL
pyautogui.press("win")
pyautogui.write("chrome")  # Could be any browser
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Perform login (adjust coordinates according to your screen resolution)
pyautogui.click(x=685, y=451)
pyautogui.write("Your Email")
pyautogui.press("tab")
pyautogui.write("Your Password")
pyautogui.click(x=955, y=638)
time.sleep(3)

# Load product dataset
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Iterate through dataset and register each product
for linha in tabela.index:
    pyautogui.click(x=653, y=294)  # Adjust coordinates according to your screen resolution
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    time.sleep(0.5)
