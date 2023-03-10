from selenium import webdriver 
import time
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
s =  Service("C:/Users/91700/OneDrive/Desktop/extracted/chromedriver.exe")
driver  = webdriver.Chrome(service = s)
driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)
driver.find_element(by=By.XPATH , value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(2)
driver.find_element(by=By.XPATH , value = '//*[@id="app"]/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(3)
old_height = driver.execute_script('return document.body.scrollHeight')
time.sleep(1)
count = 1
while True:

    driver.find_element(by=By.XPATH , value = '//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    time.sleep(2)
    print(count)
    print(old_height)
    print(new_height)
    count = count+1

    if old_height == new_height :
        break 
    old_height  = new_height

html  = driver.page_source 
with open('smartprix.html','w',encoding='utf-8') as f:
    f.write(html)


