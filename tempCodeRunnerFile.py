import pyautogui
n = int(input(""))  
for i in range(0, n):  
    pyautogui.keyDown('shift')
    pyautogui.write("# " * (i+1), interval=0.25)       
    print()