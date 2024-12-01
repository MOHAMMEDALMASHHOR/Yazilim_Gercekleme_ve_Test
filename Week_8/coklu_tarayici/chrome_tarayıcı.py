from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL'ye git
driver.get("http://www.google.com")

# 5 saniye bekle
time.sleep(5)