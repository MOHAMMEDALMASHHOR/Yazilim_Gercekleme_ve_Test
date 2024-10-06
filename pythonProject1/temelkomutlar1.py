

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# # Edge tarayıcısını başlat
# driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
#
# # Belirtilen URL'ye git
# driver.get("https://www.samsun.edu.tr")
#
# # Tarayıcıyı kapat
# driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome tarayıcısını başlat
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Belirtilen URL'ye git
driver.get("https://www.samsun.edu.tr")

# Tarayıcıyı kapat
driver.quit()
