from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# İndirme konumunu belirtiyoruz
download_path = "C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_7"
file_name = "Odev_8.txt"  # İstediğiniz dosya adı

# WebDriver'ı başlatırken indirme seçeneklerini belirtiyoruz
chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": download_path}  # İndirme dizinini belirtiyoruz
chrome_options.add_experimental_option("prefs", prefs)

#driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)
try:
    # Yüklenen dosyanın URL'sine git
    driver.get("https://file.io/Eu5Sdebimrib") #Bu here sefer duzeltmeliyiz

    # İndirme işlemi için download düğmesine tıklama
    time.sleep(10)
    download_button = driver.find_element(By.CSS_SELECTOR, '[title="Download"]')
    download_button.click()
    print("Download düğmesine tıklandı.")

    
    # Dosyanın indirilip indirilmediğini kontrol etme
    timeout = 20  # Bekleme süresi (saniye)
    downloaded_file = None

    while timeout > 0:
        # İndirilen dosyaların listesini alıyoruz
        files = os.listdir(download_path)
        for file in files:
            if file.endswith(".txt"):  # Dosya uzantısına göre kontrol (gerektiğinde değiştirilebilir)
                downloaded_file = file
                break
        if downloaded_file:
            print(f"Dosya başarıyla indirildi: {downloaded_file}")
            break
        else:
            time.sleep(1)
            timeout -= 1

    # Dosyanın içeriğini kontrol etme
    if downloaded_file:
        file_path = os.path.join(download_path, downloaded_file)
        with open(file_path, 'r') as file:
            content = file.read()
            print("Dosya içeriği:", content)
    else:
        print("Dosya indirme işlemi zaman aşımına uğradı.")
    assert content == "Odev 8--ad: MOHAMMED ALMASHHOR--NO: 9211118091"
finally:
    driver.quit()