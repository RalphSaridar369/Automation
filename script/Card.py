import pyautogui
import random
import time

cards=[]

for i in range(9):
    card = str(i+2) + " Heart"
    cards.append(card)

cards.append("J Heart")
cards.append("Q Heart")
cards.append("K Heart")
cards.append("A Heart")

for i in range(9):
    card = str(i+2) + " Bastoune"
    cards.append(card)

cards.append("J Bastoune")
cards.append("Q Bastoune")
cards.append("K Bastoune")
cards.append("A Bastoune")

for i in range(9):
    card = str(i+2) + " Sbete"
    cards.append(card)

cards.append("J Sbete")
cards.append("Q Sbete")
cards.append("K Sbete")
cards.append("A Sbete")

for i in range(9):
    card = str(i+2) + " Dinere"
    cards.append(card)

cards.append("J Dinere")
cards.append("Q Dinere")
cards.append("K Dinere")
cards.append("A Dinere")

random.shuffle(cards)
random.shuffle(cards)

num=13

for k in range(4):
    time.sleep(6)
    pyautogui.typewrite("no cheating!")
    pyautogui.press("ENTER")
    for j in range(num):
        pyautogui.typewrite(cards[j])
        pyautogui.press("SPACE")
    pyautogui.press("ENTER")
    pyautogui.typewrite("done")
    pyautogui.press("ENTER")
    for n in range(13):
        cards.pop(0)


