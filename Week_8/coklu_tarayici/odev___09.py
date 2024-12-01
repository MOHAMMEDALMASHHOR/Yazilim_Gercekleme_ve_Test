from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def open_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://www.google.com")
    time.sleep(2)
    driver.quit()


def open_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("http://www.google.com")
    time.sleep(2)
    driver.quit()


def open_edge():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.get("http://www.google.com")
    time.sleep(2)
    driver.quit()


open_chrome()
open_firefox()
open_edge()
#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


test_url = "https://www.python.org/"


def test_headless_chrome():

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(test_url)


    current_url = driver.current_url
    print(current_url)
    print(driver.current_url)
    if current_url == test_url:
        print("Chrome: Doğru URL")
    else:
        print("Chrome: Yanlış URL")

    driver.quit()


def test_headless_firefox():

    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")


    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
    driver.get(test_url)

    current_url = driver.current_url
    print(current_url)
    if current_url == test_url:
        print("Firefox: Doğru URL")
    else:
        print("Firefox: Yanlış URL")

    driver.quit()

test_headless_chrome()
test_headless_firefox()
#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def start_browser(browser_name):
    try:
        if browser_name == "chrome":

            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":

            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser_name == "edge":

            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            print("Geçersiz tarayıcı adı. Lütfen 'chrome', 'firefox' veya 'edge' girin.")
            return


        url = "http://www.google.com"
        print(f"{browser_name.capitalize()} başlatılıyor...")
        driver.get(url)
        print(f"Sayfa başlığı: {driver.title}")


        time.sleep(5)


        driver.quit()
        print(f"{browser_name.capitalize()} kapatıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")


browser_name = input("Hangi tarayıcıyı başlatmak istiyorsunuz? (chrome, firefox, edge): ").strip().lower()
start_browser(browser_name)
#%%
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

name = "MOHAMMED MASHHOR ALMASHHOR"
email = "mohammed.almashhor2020@gmail.com"
current_address = "Turkiey/Samsun"
permanent_address = "Yemen/Hadramout"

url = "https://demoqa.com/text-box"


def fill_form_and_check(browser_name):
    try:

        if browser_name == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            print("Geçersiz tarayıcı adı.")
            return

        driver.get(url)
        time.sleep(2)

        driver.execute_script("document.querySelectorAll('iframe').forEach(iframe => iframe.style.display = 'none');")

        driver.find_element("id", "userName").send_keys(name)
        driver.find_element("id", "userEmail").send_keys(email)
        driver.find_element("id", "currentAddress").send_keys(current_address)
        driver.find_element("id", "permanentAddress").send_keys(permanent_address)

        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "submit")))
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        submit_button.click()

        time.sleep(2)

        output_name = driver.find_element("id", "name").text
        output_email = driver.find_element("id", "email").text
        output_current_address = driver.find_element("xpath", "//p[@id='currentAddress']").text
        output_permanent_address = driver.find_element("xpath", "//p[@id='permanentAddress']").text

        results = {
            "Name": output_name.split(":")[1].strip(),
            "Email": output_email.split(":")[1].strip(),
            "Current Address": output_current_address.split(":")[1].strip(),
            "Permanent Address": output_permanent_address.split(":")[1].strip(),
        }

        expected_results = {
            "Name": name,
            "Email": email,
            "Current Address": current_address,
            "Permanent Address": permanent_address,
        }

        if results == expected_results:
            print(f"{browser_name.capitalize()}: Sonuçlar doğru.")
        else:
            print(f"{browser_name.capitalize()}: Sonuçlar yanlış!")
        time.sleep(2)
        driver.quit()
    except Exception as e:
        print(f"{browser_name.capitalize()} için bir hata oluştu: {e}")


fill_form_and_check("chrome")
fill_form_and_check("firefox")
