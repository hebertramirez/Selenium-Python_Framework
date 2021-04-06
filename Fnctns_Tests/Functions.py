import openpyxl
import pyodbc
from Inicializar import Inicializar
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, NoSuchWindowException, TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.ie.options import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pytest
import time
import datetime
import re
import os


class Funciones(Inicializar):
    def open_browser(self, URL=Inicializar.url, NAVEGADOR=Inicializar.navegador):
        print("Directorio: " + Inicializar.dir_base)
        print("-----------------" + NAVEGADOR + "-----------------")

        if NAVEGADOR == ("Chrome"):
            self.driver = webdriver.Chrome(
                Inicializar.dir_base + '/drivers/chromedriver')
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.driver.maximize_window()
            return self.driver

        if NAVEGADOR == ("Firefox"):
            self.driver = webdriver.Firefox(
                Inicializar.dir_base + '/drivers/geckodriver')
            self.driver.implicitly_wait(10)
            self.driver.get(URL)
            self.driver.maximize_window()
            return self.driver

    def closeBrowser(self):
        print("Se cerrara el navegador")
        self.driver.quit()

    ##########################################################
    ################ LEER / ESCRIBIR EXCEL ###################
    ##########################################################

    def leer_celda(self, celda):
        workbook = openpyxl.load_workbook(Inicializar.excel)
        sheet = workbook["users"]
        valor = str(sheet[celda].value)
        print(u'----------------------------------')
        print(u'El libro es: ' + Inicializar.excel)
        print(u'El valor de la celda es: ' + valor)
        return valor

    def escribir_celda(self, celda, valor):
        workbook = openpyxl.load_workbook(Inicializar.excel)
        sheet = workbook["users"]
        sheet[celda] = valor
        workbook.save(Inicializar.excel)
        print(u'-----------------------')
        print(u'El libro es: ' + Inicializar.excel)
        print(u'Se escribio en la celda: ' + str(celda) + ' y el valor es: ' + str(valor))

    #########################################################
    #################### BASES DE DATOS #####################
    def db_conn(self, _host=Inicializar.DB_HOST, _port=Inicializar.DB_PORT, _dbname=Inicializar.DB_DATABASE, _username=Inicializar.DB_USER, _password=Inicializar.DB_PASSWORD):
        try:
            config = dict(
                server = _host,
                port = _port,
                database = _dbname,
                user = _username,
                password = _password
            )

            conn_str = (
                'SERVER = {server};'
                'PORT={port};' +
                'DATABASE={database};' +
                'UID={user};' +
                'PWD={password}')

            conn = pyodbc.connect(r'DRIVER={MySQL ODBC 8.0 ANSI Driver};' +
            conn_str.format(**config))


            self.cursor = conn.cursor()
            print("Siempre conectado")
            return self.cursor

        except (pyodbc.OperationalError) as error:
            self.cursor = None
            pytest.skip("error en la conexion" + str(error))

    def db_query(self, _query):
        self.cursor = Funciones.db_conn(self)
        if self.cursor is not None:
            try:
                self.cursor.execute(_query)
                self.Result = self.cursor.fetchall()
                for row in self.Result:
                    print(row)

            except (pyodbc.Error) as error:
                print("error en la consulta", error)

            finally:
                if (self.cursor):
                    self.cursor.close()
                    print("pyodbc ha cerrado la conexion")



