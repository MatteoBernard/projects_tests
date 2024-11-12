import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browser import Browser
from utils.data_loader import load_data

data = load_data()


class SearchClan(unittest.TestCase):

    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()
        print("TESTING CLAN SEARCH")
        cls.browser.get(data["wv-tracker"]["url"])

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
    
    def test_search_clan(self):
        search_clan = self.browser.driver.find_element(By.ID, "clan-btn")
        self.assertIsNotNone(search_clan, "'clan-btn' element not found")
        search_clan.click()

        search_input = self.browser.driver.find_element(By.ID, "search-input")
        self.assertIsNotNone(search_input, "'search-input' element not found")

        search_input.send_keys(data["wv-tracker"]["player-clan"])

        search_btn = self.browser.driver.find_element(By.ID, "search-btn")
        self.assertIsNotNone(search_btn, "'search-btn' element not found")
        search_btn.click()

        wait = WebDriverWait(self.browser.driver, 10)
        clan_result = wait.until(EC.visibility_of_element_located((By.ID, "clan-" + data["wv-tracker"]["player-clan-id"])))
        self.assertIsNotNone(clan_result, "'clan-result' element not found")

        clan_result.click()

        clan_name = wait.until(EC.visibility_of_element_located((By.ID, "clan-name")))
        self.assertIsNotNone(clan_name, "'clan-name' element not found")
        self.assertEquals(clan_name.text, data["wv-tracker"]["player-clan"], "Clan name does not match")

def search_clan_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(SearchClan("test_search_clan"))
    return suite
