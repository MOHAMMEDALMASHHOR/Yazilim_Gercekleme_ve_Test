import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test metadata
print("Date: 08.11.2024")
print("Name: MOHAMMED MASHHOR MOHAMMED ALMASHHOR")
print("Student Number: 9211118091")
print("Experiment No: 6\n")

# Base path for HTML files
base_path = "file:///C:/Users/Lenovo/PycharmProjects/Yazilim_Gercekleme_ve_Test/Week_6/"


class TestWebPages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    # Test Scenario 1: Register on the Registration Page
    def test_registration_page(self):
        driver = self.driver
        driver.get(base_path + "register.html")
        time.sleep(2)

        # Fill registration form
        driver.find_element(By.ID, "username").send_keys("testuser")
        driver.find_element(By.ID, "password").send_keys("testpass")

        # Submit form and verify alert
        driver.find_element(By.ID, "registerButton").click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Registration successful!")
        alert.accept()

        # Verify redirection to main page
        time.sleep(2)
        self.assertEqual(driver.current_url, base_path + "main_page.html")

    # Test Scenario 2: Interact with Elements on the Main Page
    def test_main_page_elements(self):
        driver = self.driver
        driver.get(base_path + "main_page.html")
        time.sleep(2)

        # Interact with "Remember Me" checkbox
        remember_me_checkbox = driver.find_element(By.ID, "rememberMe")
        self.assertTrue(remember_me_checkbox.is_displayed())
        if not remember_me_checkbox.is_selected():
            remember_me_checkbox.click()
        self.assertTrue(remember_me_checkbox.is_selected())

        # Modify checkbox visibility using JavaScript
        driver.execute_script("arguments[0].style.display='block';", remember_me_checkbox)
        self.assertTrue(remember_me_checkbox.is_displayed())

        # Switch to iframe for profile page
        driver.switch_to.frame("profileIframe")

        # Test Scenario 3: Interact with Profile Page (Inside Iframe)
        username_display = driver.find_element(By.ID, "usernameDisplay").text
        email_display = driver.find_element(By.ID, "emailDisplay").text
        self.assertEqual(username_display, "testuser")
        self.assertEqual(email_display, "testuser@example.com")

        # Click update profile button
        driver.find_element(By.ID, "updateProfileButton").click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Profile updated successfully!")
        alert.accept()

        # Switch back to main page
        driver.switch_to.default_content()

    # Test Scenario 4: Logout from Main Page
    def test_logout(self):
        driver = self.driver
        driver.get(base_path + "main_page.html")
        time.sleep(2)

        # Click logout button and verify alert
        driver.find_element(By.ID, "logoutButton").click()
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "You have logged out.")
        alert.accept()

        # Verify redirection to registration page
        time.sleep(2)
        self.assertEqual(driver.current_url, base_path + "register.html")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
