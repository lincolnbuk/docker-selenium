import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

class SwagLabsLoginTest(unittest.TestCase):
    def setUp(self):
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=options)
        self.driver.get('https://www.saucedemo.com/')

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Find and fill the username field
        username_field = wait.until(EC.presence_of_element_located((By.ID, 'user-name')))
        username_field.send_keys('standard_user')

        # Find and fill the password field
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys('secret_sauce')

        # Find and click the login button
        login_button = driver.find_element(By.ID, 'login-button')
        login_button.click()

        # Verify successful login by checking the presence of the inventory page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))
        self.assertIn('inventory.html', driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
