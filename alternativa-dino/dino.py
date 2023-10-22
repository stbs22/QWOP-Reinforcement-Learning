from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from time import sleep

opciones = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=opciones)

try:
  driver.get("chrome://dino")
except WebDriverException:
  pass

input("comenzar juego")

driver.execute_script("""
  Runner.instance_.startGame()
  """)

input("saltar")
while True:
  driver.execute_script("""
        Runner.instance_.tRex.startJump();
  """)
  sleep(1)
