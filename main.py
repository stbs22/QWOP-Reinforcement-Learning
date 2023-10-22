from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

def prettyException(ex):
    print(f'__________________\nExcepción:\t{sys.exc_info()[0]}\nMensaje:\t{ ":".join(str(ex).split(":")[:-1]) }\nInfo:\t\t{ex.__traceback__}\n__________________\n')

def press(tecla,driver=driver):
    driver.execute_script("""
        var tecla = arguments[0];
                          
        function simulateKeyPress(key) {
            const event = new KeyboardEvent('keydown', { key });
            textField.dispatchEvent(event);
        }

        function press(key) {
            simulateKeyPress(key);
        }

        simulateKeyPress(tecla);
    """, tecla)

opciones = webdriver.ChromeOptions()
# opciones.add_argument("")

driver = webdriver.Chrome(options=opciones)
driver.get("http://www.foddy.net/Athletics.html")
sleep(.1)

#Remove adds
xpaths = ['//*[@id="topnav"]/ins', '//*[@id="left"]', '//*[@id="right"]', '/html/head', '//*[@id="footer"]' ,'//*[@id="layout"]/tbody/tr[1]']
for xpath in xpaths:
    element = driver.find_element(By.XPATH, xpath)
    driver.execute_script("""
        var element = arguments[0];
        element.parentNode.removeChild(element);
    """, element)
sleep(1)

ventana = driver.find_element(By.XPATH,'//*[@id="window1"]')
ventana.click()

sleep(3)

while True:
    try:
        input("enter pa send key q")
        driver.execute_script('document.dispatchEvent(new KeyboardEvent("keydown", { key: "q" }))')
    except Exception as e:
        prettyException(e)
        pass

    try:
        input("enter pa send key w")
        press("w")
    except Exception as e:
        prettyException(e)
        pass

    try:
        input("enter pa send key o")
        ventana.send_keys("o")
    except Exception as e:
        prettyException(e)
        pass

    try:
        input("enter pa send key p")
        press("p")
    except Exception as e:
        prettyException(e)
        pass 


    




input("enter pa cerrar")
driver.quit()
