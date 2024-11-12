import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browser import Browser
from utils.data_loader import load_data

data = load_data()


class SearchPlayer(unittest.TestCase):

    browser = None

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser()
        print("TESTING PLAYER SEARCH")
        cls.browser.get(data["wv-tracker"]["url"])

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_search_player(self):
        search_player = self.browser.driver.find_element(By.ID, "player-btn")
        self.assertIsNotNone(search_player, "'player-btn' element not found")
        search_player.click()

        search_input = self.browser.driver.find_element(By.ID, "search-input")
        self.assertIsNotNone(search_input, "'search-input' element not found")

        search_input.send_keys(data["wv-tracker"]["player-username"])

        search_btn = self.browser.driver.find_element(By.ID, "search-btn")
        self.assertIsNotNone(search_btn, "'search-btn' element not found")
        search_btn.click()

        wait = WebDriverWait(self.browser.driver, 10)
        player_result = wait.until(EC.visibility_of_element_located((By.ID, "player-result")))
        self.assertIsNotNone(player_result, "'player-result' element not found")

        player_result.click()

        player_username = wait.until(EC.visibility_of_element_located((By.ID, "player-username")))
        self.assertIsNotNone(player_username, "'player-username' element not found")
        self.assertEquals(player_username.text, data["wv-tracker"]["player-username"], "Player username does not match")


def search_player_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(SearchPlayer("test_search_player"))
    return suite