from selenium import webdriver
import time
import os
import pyautogui

PATH ="C:\Program Files (x86)\chromedriver.exe"

#insert the data below before running the program and insert your own Email and password below
#where it's written 'test'

emails=["ralphsaridar@hotmail.com"]
title="test"
message="hello and welcome"

driver = webdriver.Chrome(PATH)
driver.get("https://outlook.com")
time.sleep(10)

#to check if logged in or not

if (driver.current_url=="https://outlook.live.com/owa/"):
    print("logging in...")
    login = driver.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]/a")
    login.click()

    email= driver.find_element_by_xpath('//*[@id="i0116"]')
    email.send_keys("test")
    acceptEmail= driver.find_element_by_xpath('//*[@id="idSIButton9"]')    
    acceptEmail.click()
    time.sleep(30)
    password= driver.find_element_by_xpath('//*[@id="i0118"]')
    password.send_keys("test")
    acceptPassword= driver.find_element_by_xpath('//*[@id="idSIButton9"]')
    acceptPassword.click()
    time.sleep(30)
time.sleep(10)
time.sleep(10)

for Email in emails:

    sendMail =driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/button/span')
    sendMail.click()

    MailReciever=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/input')
    MailReciever.send_keys(Email)

    MailSubject=driver.find_element_by_xpath('//*[@id="TextField1228"]')
    MailSubject.send_keys(title)

    MailText=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[2]/div[1]/div')
    MailText.send_keys(message)

    FinishSend= driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]/span')
    FinishSend.click()
    time.sleep(10)
    time.sleep(10)

driver.close()
print("All done :D  .")
