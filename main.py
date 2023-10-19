from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
opciones = webdriver.ChromeOptions()
# opciones.add_argument("")

driver = webdriver.Chrome(options=opciones)
driver.get("http://www.foddy.net/Athletics.html")
sleep(.1)
xpaths = ['//*[@id="topnav"]/ins', '//*[@id="left"]', '//*[@id="right"]', '/html/head', '//*[@id="footer"]' ,'//*[@id="layout"]/tbody/tr[1]']

for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
    """, element)

sleep(.1)
input()

ventana = driver.find_element(By.XPATH,'//*[@id="window1"]')
ventana.click()

sleep(3)

ventana.send_keys('q')
ventana.send_keys('w')
ventana.send_keys('o')
ventana.send_keys('p')

input("Enter awnao")
