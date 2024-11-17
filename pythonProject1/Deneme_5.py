#%%
# test_index.py (unittest structure)
import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestIndexPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_3/index.html")
        print("Index page loaded.")

    def test_page_title(self):
        self.assertEqual(self.driver.title, "Üniversite Ana Sayfa")
        print("Page title verified: Üniversite Ana Sayfa")

    def test_main_header(self):
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text, "Üniversitemize Hoş Geldiniz")
        print("Main header verified: Üniversitemize Hoş Geldiniz")

    def test_search_form_exists(self):
        form = self.driver.find_element(By.TAG_NAME, "form")
        input_elem = self.driver.find_element(By.NAME, "fakulte")
        button = self.driver.find_element(By.TAG_NAME, "button")
        self.assertTrue(form)
        self.assertTrue(input_elem and button)
        print("Search form and components found.")

    def test_engineering_faculty_link(self):
        link = self.driver.find_element(By.LINK_TEXT, "Mühendislik Fakültesi")
        self.assertEqual(link.get_attribute("href"), "file:///C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/engineering_faculty.html")
        print("Engineering faculty link verified.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Browser closed after testing index page.")

if __name__ == "__main__":
    unittest.main()

#%%
# test_faculty_search.py (pytest structure)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/faculty_search.html")
    print("Faculty search page loaded.")
    yield driver
    driver.quit()
    print("Browser closed after testing faculty search page.")

def test_page_title(driver):
    assert driver.title == "Fakülte Arama Sonuçları"
    print("Page title verified: Fakülte Arama Sonuçları")

def test_main_header(driver):
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Arama Sonuçları"
    print("Main header verified: Arama Sonuçları")

def test_engineering_faculty_result(driver):
    faculty = driver.find_element(By.CLASS_NAME, "faculty")
    assert "Mühendislik Fakültesi" in faculty.text
    assert "Üniversitemizin mühendislik alanındaki eğitim ve araştırma fakültesi." in faculty.text
    print("Engineering faculty details verified in search results.")
    link = driver.find_element(By.LINK_TEXT, "Fakülte Detayları")
    assert link.get_attribute("href") == "file:///C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/engineering_faculty.html"
    print("Faculty details link verified.")

#%%
# test_engineering_faculty.py (unittest structure)

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestEngineeringFacultyPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("file:///C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/engineering_faculty.html")
        print("Engineering faculty page loaded.")

    def test_page_title(self):
        self.assertEqual(self.driver.title, "Mühendislik Fakültesi")
        print("Page title verified: Mühendislik Fakültesi")

    def test_main_header(self):
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(header.text, "Mühendislik Fakültesi")
        print("Main header verified: Mühendislik Fakültesi")

    def test_faculty_description(self):
        description = self.driver.find_element(By.TAG_NAME, "p")
        self.assertIn("Fakültemiz, alanında uzman akademisyenler ile mühendislik dallarında eğitim sunmaktadır.", description.text)
        print("Faculty description verified.")

    def test_software_engineering_link(self):
        link = self.driver.find_element(By.LINK_TEXT, "Yazılım Mühendisliği Bölümü")
        self.assertEqual(link.get_attribute("href"), "file:///C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/software_engineering_department.html")
        print("Software engineering department link verified.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Browser closed after testing engineering faculty page.")

if __name__ == "__main__":
    unittest.main()

#%%
# test_software_engineering_department.py (pytest structure)

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_4/software_engineering_department.html")
    print("Software engineering department page loaded.")
    yield driver
    driver.quit()
    print("Browser closed after testing software engineering department page.")

def test_page_title(driver):
    assert driver.title == "Yazılım Mühendisliği Bölümü"
    print("Page title verified: Yazılım Mühendisliği Bölümü")

def test_main_header(driver):
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.text == "Yazılım Mühendisliği Bölümü"
    print("Main header verified: Yazılım Mühendisliği Bölümü")

def test_department_description(driver):
    description = driver.find_element(By.TAG_NAME, "p")
    assert "yazılım geliştirme, algoritmalar ve bilgisayar bilimi" in description.text
    print("Department description verified.")
