from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Firefox tarayıcısını başlat
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# URL'ye git
driver.get("http://www.google.com")

# 5 saniye bekle
time.sleep(5)

# Tarayıcıyı kapat
driver.quit()
