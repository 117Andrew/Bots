from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()                                                                      
#Drivers para firefox
browser.get("https://www.alumnos.frro.utn.edu.ar/")                                                
#Abre el navegador en el url espeficicado

time.sleep(2)
#Da un retardo de 2 segundos
url = browser.current_url

while (url == browser.current.url):
    with open('legajo.txt', 'r') as myfile:
        legajo = myfile.read().replace('\n', '')
    #Abre el archivo que contiene el legajo y lo asigna a una variable
    browser.find_element(By.NAME, "legajo").send_keys(legajo)
    #Encuentra la casilla donde se escribe el legajo y lo ingresa
    time.sleep(0.5)

    with open('password.txt', 'r') as myfile:
        password = myfile.read().replace('\n', '')
    #Abre el archivo que contiene la contraseña y la asigna a una variable
    browser.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)
    #Encuentra la casilla donde se escribe la contraseña y la ingresa
    time.sleep(5)