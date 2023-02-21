from selenium import webdriver   
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://www.alumnos.frro.utn.edu.ar/")

time.sleep(3)

user = browser.find_elements_by_xpath ('//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input')
user[0].send.keys('51026')

time.sleep(0.5)

user = browser.find_elements_by_xpath ('//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input')
with open('password.txt', 'r') as myfile:
    password = myfile.read().replace('\n', '')
user.send_keys(password)

time.sleep(0.5)

button = browser.find_elements_by_xpath('//*[@id="page-container"]/div[2]/form/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td/input')
button[0].click()

time.sleep(5)
