from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time

legajo = 51026

browser = webdriver.Firefox()
browser.get("https://www.alumnos.frro.utn.edu.ar/")
print("entro a la web")

time.sleep(2)

user = browser.find_elements('xpath','//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
print("encontro el elemento legajo")
time.sleep(0.5)
user.clear()
print("limpio el input de legajo")
time.sleep(0.5)
user.send_keys(legajo + Keys.ENTER)
print("Escribio el legajo")
time.sleep(0.5)

user = browser.find_elements ('xpath','//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
with open('password.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')
user.send_keys(password + Keys.ENTER)

time.sleep(0.5)

button = browser.find_elements('xpath','//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td/input')
button[0].click()

time.sleep(5)