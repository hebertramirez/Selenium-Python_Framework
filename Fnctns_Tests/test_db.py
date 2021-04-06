from Functions import Funciones as Selenium
import unittest

class DB_Test(Selenium, unittest.TestCase):
    def test_001(self):
        Selenium.db_query(self, "your_query")

if __name__ == '__main__':
    unittest.main()