from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Firefox için headless mod ayarları
options = Options()
options.add_argument("--headless")  # Tarayıcı arayüzü olmadan çalışır

# Firefox tarayıcısını başlat
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

# Belirli bir URL'ye git
url = "http://www.google.com"
print(f"Headless modda {url} adresine gidiliyor...")
driver.get(url)
time.sleep(3)

# Sayfa başlığını yazdır
page_title = driver.title
print(f"Sayfa başlığı: {page_title}")
print("Tarayıcı kapatılıyor...")
driver.quit()
