import pyautogui
import time
from vestidos.santorini import escolher_santorini
#from vestidos.noronha import escolher_noronha  # se quiser ativar

print("Automação vai começar em 3 segundos...")
time.sleep(3)

# Abrir Instagram
pyautogui.moveTo(x=1154, y=752)
time.sleep(2)
pyautogui.doubleClick()
time.sleep(2)

# Clicar em story
pyautogui.moveTo(x=1090, y=230)
time.sleep(2)
pyautogui.click()
time.sleep(2)

# Escolher vestido Santorini
escolher_santorini()

# Se quiser depois:
# escolher_noronha()

print("Automação finalizada.")