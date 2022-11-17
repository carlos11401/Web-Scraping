from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
time.sleep(3)
def document_initialised(driv):
    return driv.execute_script('return initialised')

def get_price(product):
    driver.get("https://guatemaladigital.com/Busqueda/"+product)
    result= WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, 'Rectangle_8_PB'))
    return result.text


code = ""
while code != "0":
    product = input("Enter a code: ")
    price = get_price(product)
    print("Code: " + product)
    print("Price: " + price)

