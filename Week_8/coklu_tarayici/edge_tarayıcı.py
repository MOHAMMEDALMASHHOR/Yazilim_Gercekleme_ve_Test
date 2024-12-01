from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Edge tarayıcısını başlat
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# URL'ye git
driver.get("http://www.google.com")

# 5 saniye bekle
time.sleep(5)

# Tarayıcıyı kapat
driver.quit()
