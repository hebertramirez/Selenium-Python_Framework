from Functions import Funciones as Selenium
import unittest
import os


class TestExcel(Selenium, unittest.TestCase):
    def test001(self):
        Selenium.leer_celda(self, 'A2')

if __name__ == '__main__':
    unittest.main()

