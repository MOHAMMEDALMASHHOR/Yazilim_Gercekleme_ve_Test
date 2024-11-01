import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Dosya yolunu belirtin (bu örnekte yerel bir klasördeki HTML dosyaları kullanılmaktadır)
# 'base_path' değişkeni, çalışılan klasördeki 'web' klasörüne erişim sağlar.
base_path = f"C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/web/"

# Test sınıfı oluşturuluyor; unittest.TestCase'den türetildiği için tüm unittest işlevlerini kullanabilir
class EcommerceTest(unittest.TestCase):

    def setUp(self):
        # Tarayıcıyı başlatır, testler sırasında kullanılacak driver nesnesi oluşturuluyor
        self.driver = webdriver.Chrome()
        # Sayfa yüklemeleri için 10 saniyelik varsayılan bir bekleme süresi ayarlanıyor
        self.driver.implicitly_wait(10)
        # Tarayıcı açıldıktan sonra kısa bir bekleme süresi
        time.sleep(5)

    def test_search_product(self):
        # Bu test, arama çubuğu aracılığıyla ürün arama işlevini doğrulamak için kullanılır
        driver = self.driver
        # Ana sayfayı açar; burada 'index.html' sayfası açılıyor
        driver.get(base_path + "index.html")
        print("Ana sayfa açıldı")
        # Sayfanın yüklenmesini beklemek için bir süre bekleniyor
        time.sleep(5)

        # Arama çubuğunu bulur (NAME ile), 'laptop' kelimesini arama çubuğuna yazar
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("laptop")
        # Bir süre bekleyerek kullanıcının işlemi tamamlamasını taklit eder
        time.sleep(5)
        # Enter tuşuna basarak arama işlemini başlatır
        search_box.send_keys(Keys.RETURN)

        # Arama sonuçlarının yüklendiği sayfaya yönlendiriliyor
        driver.get(base_path + "search_results.html")
        time.sleep(5)

        # Arama sonuçlarında "product" sınıfına sahip ürünlerin yüklendiğini kontrol eder
        results = driver.find_elements(By.CLASS_NAME, "product")
        # Arama sonucunda en az bir ürün olup olmadığını kontrol eder; yoksa hata verir
        self.assertGreater(len(results), 0, "Arama sonucu bulunamadı")
        # Test tamamlanmadan önce kısa bir bekleme süresi
        time.sleep(5)

    def test_product_page_load(self):
        # Bu test, belirli bir ürün sayfasının başarıyla yüklendiğini doğrular
        driver = self.driver
        # Ürün sayfasını açar; burada 'product_laptop.html' sayfası açılıyor
        driver.get(base_path + "product_laptop.html")
        print("Ürün sayfası açıldı")
        # Sayfanın yüklenmesi için kısa bir bekleme süresi
        time.sleep(5)

        # Ürün başlığını doğrular; sayfadaki ana başlığı (h1) bulup metnini alır
        product_title = driver.find_element(By.TAG_NAME, "h1").text
        # Ürün başlığının "Laptop" kelimesini içerip içermediğini kontrol eder
        self.assertIn("Laptop", product_title, "Ürün başlığı beklenenden farklı")

    def tearDown(self):
        # Testlerin ardından tarayıcıyı kapatır, belleği temizler
        self.driver.quit()

# Bu dosya doğrudan çalıştırıldığında tüm testleri çalıştırır
if __name__ == "__main__":
    unittest.main()
    # unittest.main() tamamlandıktan sonra kısa bir bekleme süresi
    time.sleep(5)



# Kod Açıklaması
# setUp: Her test çalıştırılmadan önce setUp() metodu ile tarayıcı başlatılır ve test ortamı hazırlanır.
# test_search_product: Ana sayfada bir ürün araması yapar ve arama sonuçlarının yüklendiğini doğrular.
# test_product_page_load: Belirli bir ürün sayfasını açar ve sayfanın doğru ürün başlığını içerip içermediğini kontrol eder.
# tearDown: Her testten sonra tearDown() metodu ile tarayıcı kapatılır, böylece testlerin her biri temiz bir ortamda çalıştırılır.
# unittest.main(): Kod doğrudan çalıştırıldığında test sınıfındaki tüm testleri başlatır.
# Bu kod, yerel bir e-ticaret sitesinin basit bir simülasyonunu yapar ve unittest kullanarak otomatik test senaryoları hazırlar.