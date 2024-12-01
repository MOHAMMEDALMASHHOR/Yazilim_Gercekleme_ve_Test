from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome için headless mod ayarları
options = Options()
options.add_argument("--headless")  # Tarayıcı arayüzü olmadan çalışır
options.add_argument("--disable-gpu")  # Windows sistemlerde GPU kullanımı kapatılır (önerilir)


# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


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
