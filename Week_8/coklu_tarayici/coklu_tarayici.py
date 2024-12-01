from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def start_browser(browser_name):
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name.lower() == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://www.google.com")
    time.sleep(2)
    print(f"Page Title on {browser_name}: {driver.title}")
    driver.quit()


# Test çalıştırma her bir tarayıcı için testi çalıştırıyoruz
for browser in ["chrome", "firefox", "edge"]:
    start_browser(browser)
