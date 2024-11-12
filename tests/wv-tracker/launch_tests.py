import unittest
from LayoutTest import header_test_suite
from RolesTest import roles_test_suite
from SearchPlayerTest import search_player_test_suite
from SearchClanTest import search_clan_test_suite


def load_all_tests():
    suite = unittest.TestSuite()
    suite.addTests(header_test_suite())
    suite.addTests(roles_test_suite())
    suite.addTests(search_player_test_suite())
    suite.addTests(search_clan_test_suite())
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(load_all_tests())

