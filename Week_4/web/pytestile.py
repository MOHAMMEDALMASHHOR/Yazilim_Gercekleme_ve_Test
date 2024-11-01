import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# Dosya yolunu belirler; bu örnekte yerel bir klasördeki HTML dosyaları kullanılmaktadır.
base_path = f"file:///{os.getcwd()}/web/"


# Selenium WebDriver için bir fixture oluşturur.
@pytest.fixture
def driver():
    # Test başlamadan önce tarayıcıyı başlatır.
    driver = webdriver.Chrome()
    # Sayfa yüklemeleri için 10 saniyelik varsayılan bir bekleme süresi ayarlar.
    driver.implicitly_wait(10)
    # Tarayıcı açıldıktan sonra kısa bir bekleme süresi.
    time.sleep(5)
    yield driver  # Testin çalıştığı süre boyunca driver'ı sağlar.
    # Test tamamlandıktan sonra tarayıcıyı kapatır.
    driver.quit()


# Ürün arama fonksiyonunu test eden bir test senaryosu
def test_search_product(driver):
    # Ana sayfayı açar; burada 'index.html' sayfası açılıyor.
    driver.get(base_path + "index.html")

    # Arama çubuğunu bulur (NAME ile) ve 'laptop' kelimesini arama çubuğuna yazar.
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("laptop")
    # Bir süre bekleyerek kullanıcının işlemi tamamlamasını taklit eder.
    time.sleep(5)
    # Enter tuşuna basarak arama işlemini başlatır.
    search_box.send_keys(Keys.RETURN)

    # Arama sonuçları sayfasına yönlendiriliyor.
    driver.get(base_path + "search_results.html")
    time.sleep(5)

    # Arama sonuçlarında "product" sınıfına sahip ürünlerin yüklendiğini kontrol eder.
    results = driver.find_elements(By.CLASS_NAME, "product")
    # Arama sonucunda en az bir ürün olup olmadığını kontrol eder; yoksa hata verir.
    assert len(results) > 0, "Arama sonucu bulunamadı"


# Ürün sayfasının başarıyla yüklendiğini test eden bir test senaryosu
def test_product_page_load(driver):
    # Ürün sayfasını açar; burada 'product_laptop.html' sayfası açılıyor.
    driver.get(base_path + "product_laptop.html")
    time.sleep(5)

    # Ürün başlığını doğrular; sayfadaki ana başlığı (h1) bulup metnini alır.
    product_title = driver.find_element(By.TAG_NAME, "h1").text
    # Ürün başlığının "Laptop" kelimesini içerip içermediğini kontrol eder.
    assert "Laptop" in product_title, "Ürün başlığı beklenenden farklı"

#
# Kod Açıklamaları:
# import: Gerekli kütüphaneler ve modüller kodun başında içe aktarılır.
# base_path: os.getcwd() fonksiyonu ile mevcut çalışma dizini alınır ve web klasöründeki HTML dosyalarına erişim sağlamak için kullanılacak olan dosya yolu oluşturulur.
# pytest.fixture: driver fonksiyonu, test sırasında kullanılacak Selenium WebDriver nesnesini oluşturur. yield ifadesi, testin bu noktada çalışmasına izin verirken tarayıcıyı açar. Test tamamlandıktan sonra tarayıcı kapatılır.
# test_search_product: Bu test, ana sayfayı açar, bir ürün araması yapar ve arama sonuçlarının yüklendiğini doğrular.
# test_product_page_load: Bu test, belirli bir ürün sayfasının başarıyla yüklendiğini ve doğru başlık metnini içerip içermediğini kontrol eder.