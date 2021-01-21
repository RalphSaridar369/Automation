# Main purpos of this program is to facilitate some code writing,
# that by making use of pyautogui



import pyautogui,time
from bs4 import BeautifulSoup
import os
import keyboard
from PIL import Image

print("Hello welcome to AUTOGUI menu: \n\n")

print("Make your decision:\n\n")

print("1 - do a switch statement --- 6 -  webscrape a page\n")
print("2 - encrypt with cryptography --- 7 - change files' name inside a certain folder\n")
print("3 - decrypt with cryptography --- 8\n")
print("4 --- 9\n")
print("5 - Check if an element is existant in an array ---  0 - Spam a message to someone on whatsapp!\n")

choice = input("choose between 0-9")


while(int(choice.isdigit())==False):
    choice = input("Please choose a digit between 0-9")






if(choice==str(1)):

    cases=input("how many cases?")

    toPrint="def switch(choice):"
    toPrint2=[]
    string=""
    for k in range(int(cases)):
        string = "\nif choice==" + str(k) +"\npass"
        toPrint2.append(string)

    time.sleep(3)

    for i in toPrint:
        pyautogui.typewrite(i)

    for j in toPrint2:
        pyautogui.typewrite(j)







if(choice=="0"):

    message=input("input the message you want to spam\n")
    times=input("input how many times you want to send this message\n")
    print("go to whatsapp")
    time.sleep(5)

    for i in range(int(times)):
        pyautogui.typewrite(message)
        pyautogui.press("ENTER")







if(choice=="2"):

    print("Type this in your terminal :\npip3 install cryptography\n")
    print=["from cryptography.fernet import Fernet\n","def generate_key():","#Generates a key and save it into a file",
            "\tkey = Fernet.generate_key()","with open('secret.key', 'wb') as key_file:","key_file.write(key)","\n"]
    print2=["def load_key():","#Load the previously generated key","return open('secret.key','rb').read()","",""]
    print3=["def encrypt_message(message):","#Encrypts a message","\tkey = load_key()","encoded_message = message.encode()",
            "f = Fernet(key)","encrypted_message = f.encrypt(encoded_message)"
        ,"","if __name__ == '__main__':","encrypt_message('encrypt this message')"]

    time.sleep(5)

    for i in print:
        pyautogui.typewrite(i)
        pyautogui.press("ENTER")

    for j in print2:
        pyautogui.typewrite(j)
        pyautogui.press("ENTER")

    for k in print3:
        pyautogui.typewrite(k)
        pyautogui.press("ENTER")







if(choice=="3"):


    print("Type this in your terminal :\npip3 install cryptography\n")
    time.sleep(5)
    print = ["from cryptography.fernet import Fernet\n","def load_key():"
        ,"#Load the previously generated key","\treturn open('secret.key', 'rb').read()"]
    print2=["def decrypt_message(encrypted_message):","#Decrypts an encrypted message",
            "\tkey = load_key()","f = Fernet(key)","decrypted_message = f.decrypt(encrypted_message)",
            "print(decrypted_message.decode())","\nif __name__ == '__main__':",
            "decrypt_message( b'gAAAAABesCUIAcM8M-_Ik_-I1-JD0AzLZU8A8-AJITYCp9Mc33JaHMnYmRedtwC8LLcYk9zpTqYSaDaqFUgfz-tcHZ2TQjAgKKnIWJ2ae9GDoea6tw8XeJ4=')"]

    for i in print:
        pyautogui.typewrite(i)
        pyautogui.press("ENTER")

    for j in print2:
        pyautogui.typewrite(j)
        pyautogui.press("ENTER")



if(choice==4):
    pass






if(choice=="5"):

    type=input("input type of data : int , str ")

    time.sleep(3)

    if (type=="str"):

        string=["def checkExist(data , table):","\nbool exist=False","\nfor i in table:" ,
                "\nif (i==str(data)):","\nexist=True "]

        for i in string:
            pyautogui.typewrite(i)

        pyautogui.press["SHIFT TAB"]
        pyautogui.typewrite("\n return exist")

    else:

        string=["def checkExist(data , table):","\nbool exist=False","\nfor i in table:" ,
                "\nif (i==int(data)):","\nexist=True "]

        for i in string:
            pyautogui.typewrite(i)

        pyautogui.typewrite("\n return exist")







if(choice=="6"):

    print("\nYou need to install BeautifulSoup so the program works ")

    toPrint=["from bs4 import BeautifulSoup","\nimport requests","\n",
            "page = requests.get('insert your URL here')","soup = BeautifulSoup(page.content ,'html.parser')",
            "\n#to access divs and other body elements you need to go through parents first ... for example ",
            "\nweek = soup.find(id='seven-day-forecast')","\n#you can also do:","\n",
            "#print = week.find_all(class_='hero')","\n#print.get_text()","\n#for i in print:",
             "\n#print(i.find_all(<p>).get_text()","\n#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))"]

    time.sleep(5)

    for i in toPrint:
        pyautogui.typewrite(i)
        pyautogui.press("ENTER")





if(choice=="7"):
    sub_choice=input("1 --- images   2 --- Text,JSON or CSV")
    time.sleep(2)

    if(sub_choice=="1"):

        typeOfFile=input("jpg or png?")

        while(typeOfFile!="jpg" and typeOfFile!="png"):
               typeOfFile=input("jpg or png?")

        print("please insert all your files inside the folder 'was' then press a when done.")
        one=input("press 1 when done")
        if (one=="1"):

            input=input("please enter the name for your files ")
            directory = "C:/Users/Ralph/PycharmProjects/pythonProject/automation/script/was"
            newdir="C:/Users/Ralph/PycharmProjects/pythonProject/automation/script/became"
            for file in os.listdir(directory):
                im = Image.open(file)
                im.save(f'{newdir}/{input}.{typeOfFile}')

    else:

        typeOfFile=input("txt,JSON or CSV ?")

        while(typeOfFile!="txt" and typeOfFile!="JSON" and typeOfFile !="CSV"):
               typeOfFile=input("txt,JSON or CSV ?")

        print("please insert all your files inside the folder 'was' then press a when done.")
        one=input("press 1 when done")
        if (one=="1"):

            input=input("please enter the name for your files ")
            directory = "C:/Users/Ralph/PycharmProjects/pythonProject/automation/script/was"
            newdir="C:/Users/Ralph/PycharmProjects/pythonProject/automation/script/became"
            for file in os.listdir(directory):
                os.rename(f'{directory}/{file}.{typeOfFile}',f'{newdir}/{input}.{typeOfFile}')


if(choice==8):
    pass
if(choice==9):
    string="this sentence was written using python"
    for i in string:
        pyautogui.typewrite(i)
        pyautogui.press("ENTER")

time.sleep(5)


