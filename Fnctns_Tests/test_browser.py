from Functions import Funciones as Selenium
import unittest

class test1(Selenium, unittest.TestCase):
    def setUp(self):
        Selenium.open_browser(self)

    def test_prueba(self):
        pass

    def tearDown(self):
        Selenium.closeBrowser(self)

if __name__ == '__main__':
    unittest.main()