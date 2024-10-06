#%%
#Brinici odev
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Tarih:04.10.2024\nAd-Soyad:MOHAMMED ALMASHHOR \nOgrenci Numarasi:9211118091\nDeney No: 2\n\n")
# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Belirtilen URL'ye git
driver.get("https://mf.samsun.edu.tr/")

page_title = driver.title
print(f"Sayfa Başlığı: {page_title}")
time.sleep(10)
# Tarayıcıyı kapat
driver.quit()
#%%
#Ikinci soru
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Tarih:04.10.2024\nAd-Soyad:MOHAMMED ALMASHHOR \nOgrenci Numarasi:9211118091\nDeney No: 2\n\n")
# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Belirtilen URL'ye git
driver.get("https://mf.samsun.edu.tr/")
time.sleep(2)
driver.get("https://yazilimmuhendisligi.samsun.edu.tr/")
time.sleep(2)
driver.get("https://google.com")
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)

# Tarayıcıyı kapat
driver.quit()
#%%
#Ucunu odev
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Tarih:04.10.2024\nAd-Soyad:MOHAMMED ALMASHHOR \nOgrenci Numarasi:9211118091\nDeney No: 2\n\n")
# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mf.samsun.edu.tr/")

html_source = driver.page_source

print(html_source[:100])

driver.quit()
#%%
#Dorduncu soru
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Tarih:04.10.2024\nAd-Soyad:MOHAMMED ALMASHHOR \nOgrenci Numarasi:9211118091\nDeney No: 2\n\n")
# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mf.samsun.edu.tr/")

window_size = driver.get_window_size()
print(f"Pencere Boyutları: {window_size}")
driver.set_window_size(1200, 600)
time.sleep(5)
window_size = driver.get_window_size()
print(f"Pencere Boyutları: {window_size}")
driver.quit()
#%%
#besinci soru
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Tarih:04.10.2024\nAd-Soyad:MOHAMMED ALMASHHOR \nOgrenci Numarasi:9211118091\nDeney No: 2\n\n")
# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://mf.samsun.edu.tr/")

yenilenmeden_onceki_title= driver.title
driver.refresh()
page_title = driver.title
print(f"Yenilemeden önceki başlık ile aynı olup olmadığını kontrol: {page_title==yenilenmeden_onceki_title}")

driver.quit()







