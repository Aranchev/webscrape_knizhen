
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

a = input('Keywords:')

b = ['kostadinov', 'vzaimnost', 'daianna', 'svraki', 'avis-rara', 'novi-i-stari-knigi', 'knigi'] 

driver = webdriver.Firefox()

class Xpath:
    def __init__(self, search):
        self.search = search 

    def find(self):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.search))
            )  
            return element
        except:
            driver.quit()
    
    def send(self, element):  #! for search engines
        element.send_keys(f'{a}')
        element.send_keys(Keys.RETURN)

    def click(self, element):
        element.click()

for i in b:
    print('----------' + i.capitalize() + '----------')
    driver.get(f'https://{i}.knizhen-pazar.net/')

    time.sleep(1)

    obj = Xpath('//*[@id="js_q"]')  #! search engine

    search_element = obj.find()

    time.sleep(1)

    obj.send(search_element)

    time.sleep(1)

    obj1 = Xpath('/html/body/div/div/div/main/div[2]/section/nav/div[2]/div') #! dropdown

    search_element1 = obj1.find()

    time.sleep(1)

    search_element1.click()

    time.sleep(1)

    obj2 = Xpath('/html/body/div/div/div/main/div[2]/section/aside/div/div/form/div/div[1]/section[1]/div[2]/ol/li[3]/label') #! dropdown option

    search_element2 = obj2.find()

    time.sleep(1)

    search_element2.click()

    time.sleep(1)

    for i in range(1, 10):
        try:
            search4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/div/div/div/main/div[2]/section/div/div/div[{i}]/div[2]/div[2]/div[1]/div[1]/a'))
        ) #! name of book
        except:
            break

        try:
            search5 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'/html/body/div/div/div/main/div[2]/section/div/div/div[{i}]/div[2]/div[2]/div[3]/div/div[1]/div'))
        ) #! price of book
        except:
            break

        print(f'{search5.text} | {search4.text} | {search4.get_attribute('href')}')

driver.quit()
