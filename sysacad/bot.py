from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://www.alumnos.frro.utn.edu.ar/")
print("entro a la web")

time.sleep(2)

with open('legajo.txt', 'r') as myfile:
    legajo = myfile.read().replace('\n', '')
browser.find_element(By.NAME, "legajo").send_keys(legajo)
print("Escribio el legajo")
time.sleep(0.5)

with open('password.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')
browser.find_element(By.NAME, "password").send_keys(password + Keys.ENTER)

time.sleep(5)