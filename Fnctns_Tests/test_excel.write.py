from Functions import Funciones as Selenium
import unittest
import os


class TestExcel(Selenium, unittest.TestCase):
    def test001(self):
        Selenium.escribir_celda(self, 'A2', 'John')

if __name__ == '__main__':
    unittest.main()