from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Edge için headless mod ayarları
options = Options()
options.add_argument("--headless")  # Tarayıcı arayüzü olmadan çalışır
options.add_argument("--disable-gpu")  # Windows sistemlerde GPU kullanımı kapatılır (önerilir)

# Edge tarayıcısını başlat
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

# Belirli bir URL'ye git
url = "http://www.google.com"
print(f"Headless modda {url} adresine gidiliyor...")
driver.get(url)
time.sleep(3)

# Sayfa başlığını yazdır
page_title = driver.title
print(f"Sayfa başlığı: {page_title}")

# Tarayıcıyı kapat
print("Tarayıcı kapatılıyor...")
driver.quit()
