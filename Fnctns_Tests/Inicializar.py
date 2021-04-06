import os 

class Inicializar():
    #directorio
    dir_base = os.path.abspath(os.path.join(__file__, "../.."))
    dateFormat = '%d/%m/%Y'
    hourFormat = "%H%M%S"

    #browser
    navegador = u'Chrome'
    url = "https://www.google.com.ec"
    
    #evidencias
    ss_folder = dir_base + u'/capturas'

    #DB
    DB_HOST = ""
    DB_PORT = ""
    DB_DATABASE = ""
    DB_USER = ""
    DB_PASSWORD = ""

    #libro excel
    excel = dir_base + u'/libros_excel/test_book.xlsx'