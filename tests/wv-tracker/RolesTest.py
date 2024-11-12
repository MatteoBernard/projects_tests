import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browser import Browser
from utils.data_loader import load_data

data = load_data()


class RolesTest(unittest.TestCase):

    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()
        print("TESTING ROLES DISPLAY")
        cls.browser.get(data["wv-tracker"]["url"])
        cls.browser.driver.find_element(By.ID, "roles").click()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def click_on_role(self):
        wait = WebDriverWait(self.browser.driver, 10)
        role_element = wait.until(EC.visibility_of_element_located((By.ID, data["wv-tracker"]["doctor-role-id"])))
        role_element.click()

        role_name = self.browser.driver.find_element(By.ID, "role-name")
        role_description = self.browser.driver.find_element(By.ID, "role-description")
        role_aura = self.browser.driver.find_element(By.ID, "role-aura")
        role_team = self.browser.driver.find_element(By.ID, "role-team")

        self.assertIsNotNone(role_name, "'role-name' element not found")
        self.assertIsNotNone(role_description, "'role-description' element not found")
        self.assertIsNotNone(role_aura, "'role-aura' element not found")
        self.assertIsNotNone(role_team, "'role-team' element not found")

        self.assertEquals(role_name.text, data["wv-tracker"]["doctor-role-name"], "Role name does not match")
        self.assertEquals(role_description.text, data["wv-tracker"]["doctor-role-description"], "Role description does not match")
        self.assertEquals(role_aura.text, data["wv-tracker"]["doctor-role-aura"], "Role aura does not match")
        self.assertEquals(role_team.text, data["wv-tracker"]["doctor-role-team"], "Role team does not match")

        close_btn = self.browser.driver.find_element(By.ID, "close-btn")
        self.assertIsNotNone(close_btn, "'close-btn' element not found")
        close_btn.click()


def roles_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(RolesTest("click_on_role"))
    return suite