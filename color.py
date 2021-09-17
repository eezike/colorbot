#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os



options = Options()


c = input("C: ")
d = input("D: ")


options.headless = False
path = f"{os.getcwd()}/driver/chromedriver"

driver = webdriver.Chrome(executable_path = path, options=options)


# go
driver.get('https://home.color.com/sign-in')
sleep(2)

driver.find_element_by_name("email").send_keys("eezike@college.harvard.edu")
driver.find_element_by_name("password").send_keys("")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/div/div/form/div[3]/button').click()
sleep(2)

driver.get("https://home.color.com/covid/activation/ready-to-activate")
sleep(2)

xpaths = [
    '//*[@id="onetrust-close-btn-container"]/button',
    '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div/div/div/a',
    '//*[@id="root"]/div/div/div[3]/div/a',
    '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/button',
    '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/button',
    '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[1]/div[4]/button',
    '//*[@id="root"]/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/button',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[4]/label/span[1]/span[1]/input',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[5]/label/span[1]/span[1]/input',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[6]/label/span[1]/span[1]/input',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/div[7]/label/span[1]/span[1]/input',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/a',
    '//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/div[9]/button',
    '/html/body/div[3]/div[3]/div/div[3]/button[2]',
]

for xpath in xpaths:
    driver.find_element_by_xpath(xpath).click()
    sleep(3)

driver.find_element_by_name("kit_barcode").send_keys(d)
driver.find_element_by_name("accession_number").send_keys(c)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div[2]/div/div[1]/form/div[3]/button').click()
sleep(2)

driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/button[1]').click()


try:
    driver.close()
except:
    print("Fail")
    driver.close()
