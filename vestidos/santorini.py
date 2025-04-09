import pyautogui
import time

def escolher_santorini():
    pyautogui.moveTo(x=1315, y=415)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=1314, y=154)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=1212, y=153)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(x=1306, y=498)
    time.sleep(2)
    pyautogui.click()
    pyautogui.write("https://www.chalo.com.br/produtos/vestido-santorini/")
    time.sleep(2)
    pyautogui.moveTo(x=1185, y=287)
    time.sleep(2)
    pyautogui.click()
    pyautogui.write("Saiba Mais")
    time.sleep(2)
    pyautogui.moveTo(x=1313, y=172)
    time.sleep(2)
    pyautogui.click()
    #Reposicionar a figurinha
    pyautogui.moveTo(x=1193, y=430)
    time.sleep(2)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.doubleClick()
    



