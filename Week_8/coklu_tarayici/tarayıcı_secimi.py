from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Kullanıcıdan tarayıcı adı al
browser_name = input("Hangi tarayıcıyı kullanmak istiyorsunuz? (chrome, firefox, edge): ").strip().lower()

# Tarayıcı başlatma
try:
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError("Geçersiz tarayıcı adı! Lütfen 'chrome', 'firefox' veya 'edge' girin.")

    # Belirli bir URL'ye git
    url = "http://www.google.com"
    print(f"{browser_name.capitalize()} tarayıcısı başlatılıyor ve {url} adresine gidiliyor...")
    driver.get(url)

    # Sayfa başlığını yazdır
    print("Sayfa başlığı:", driver.title)

    # 5 saniye bekle
    time.sleep(5)

finally:
    # Tarayıcıyı kapat
    print(f"{browser_name.capitalize()} tarayıcısı kapatılıyor...")
    driver.quit()
