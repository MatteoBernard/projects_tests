import unittest
from selenium.webdriver.common.by import By

from utils.browser import Browser
from utils.data_loader import load_data

data = load_data()


class LayoutTest(unittest.TestCase):

    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()
        print("TESTING HEADER")
        cls.browser.get(data["wv-tracker"]["url"])

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_home(self):
        home_element = self.browser.driver.find_element(By.ID, "home")
        self.assertIsNotNone(home_element, "'home' element not found")
        home_element.click()

        title_element = self.browser.driver.find_element(By.ID, "title")
        self.assertIsNotNone(title_element, "'title' element not found")
        self.assertIn(title_element.text, ["Search for a player", "Search for a clan"], "Title content does not match")

    def test_gtr(self):
        gtr_element = self.browser.driver.find_element(By.ID, "gtr")
        self.assertIsNotNone(gtr_element, "'gtr' element not found")
        gtr_element.click()

        title_element = self.browser.driver.find_element(By.ID, "title")
        self.assertIsNotNone(title_element, "'title' element not found")
        self.assertEquals(title_element.text, "Guess the role", "Title content does not match")

    def test_roles(self):
        roles_element = self.browser.driver.find_element(By.ID, "roles")
        self.assertIsNotNone(roles_element, "'roles' element not found")
        roles_element.click()

        title_element = self.browser.driver.find_element(By.ID, "title")
        self.assertIsNotNone(title_element, "'title' element not found")
        self.assertEquals(title_element.text, "Roles", "Title content does not match")

    def test_roles_rotation(self):
        roles_rotation_element = self.browser.driver.find_element(By.ID, "roles-rotation")
        self.assertIsNotNone(roles_rotation_element, "'roles-rotation' element not found")
        roles_rotation_element.click()

        title_element = self.browser.driver.find_element(By.ID, "title")
        self.assertIsNotNone(title_element, "'title' element not found")
        self.assertEquals(title_element.text, "Roles Rotation", "Title content does not match")

    def test_footer(self):

        wolvesville_link_element = self.browser.driver.find_element(By.ID, "wolvesville-link")
        self.assertIsNotNone(wolvesville_link_element, "'wolvesville-link' element not found")

        github_link_element = self.browser.driver.find_element(By.ID, "github-link")
        self.assertIsNotNone(github_link_element, "'github-link' element not found")


def header_test_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(LayoutTest('test_home'))
    test_suite.addTest(LayoutTest('test_gtr'))
    test_suite.addTest(LayoutTest('test_roles'))
    test_suite.addTest(LayoutTest('test_roles_rotation'))
    test_suite.addTest(LayoutTest('test_footer'))
    return test_suite