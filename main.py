from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
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
sleep(.1)

input("wait")

ventana = driver.find_element(By.XPATH,'//*[@id="window1"]')
ventana.click()

# driver.execute_script("""
# function simulateKeyPress(key) {
#     const event = new KeyboardEvent('keydown', { key });
#     textField.dispatchEvent(event);
# }

# function press(key) {
#     simulateKeyPress(key);
# }
# """)

# def press(key,driver=driver):
#     driver.execute_script("""
#         var key = arguments[0];
#         simulateKeyPress(key);
#     """, key)

sleep(3)

while True:
    input("send key q")
    driver.execute_script('document.dispatchEvent(new KeyboardEvent("keydown", { key: "q" }))')  # Presiona la tecla 'Q'press("q")

input("send key w")
press("w")

input("send key o")
press("o")

input("send key p")
press("p")

input("enter pa cerrar")
driver.quit()
