import time
import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Prueb.creacion_documento import CreacionDocumento



class base_test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        driver = self.driver

    def test_uno(self):

        driver = self.driver
        expediente = CreacionDocumento(driver)

        expediente.Navegar("http://10.64.110.36:8080/ceropapel/")
        # Le indica a la pagina esperar a ver el contenido un max de 10 seg, si el contenido se muestra antes de los 10 seg, la prueba comienza, si el contenido no se muestra en 10 seg, la prueba falla
        driver.implicitly_wait(60)
        driver.maximize_window()
        # Inicio de sesión Ceropapel
        expediente.login("9754597-9")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")
        # Click Gestión
        expediente.explicit("//span[contains(@id,'button-1048-btnInnerEl')]")
        # Click Crear Expediente
        expediente.explicit("//span[contains(@id,'menuitem-1050-textEl')]")
        # Comienza creación de Documento primera parte
        expediente.Documento_pt_uno()
        # CLick en Ingresar
        expediente.ingresarExpediente()
        # Click en Si
        expediente.explicit("//span[contains(@id,'button-1006-btnInnerEl')]")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnEl')]")
        # Comienza a completar la parte dos del Expediente comenzando por las observaciones
        expediente.Observaciones_dos()
        # Click en Grabar
        expediente.GrabarExpediente()
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")


        print("Documento creado")
        print("Prueba finalizada con éxito.")


    def test_dos(self):

        driver = self.driver
        expediente = CreacionDocumento(driver);

        expediente.Navegar("http://10.64.110.36:8080/ceropapel/")
        # Le indica a la pagina esperar a ver el contenido un max de 10 seg, si el contenido se muestra antes de los 10 seg, la prueba comienza, si el contenido no se muestra en 10 seg, la prueba falla
        driver.implicitly_wait(60)
        driver.maximize_window()
        # Inicio de sesión Ceropapel
        expediente.login("10836708-3")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")
        # Click Gestión
        expediente.explicit("//span[contains(@id,'button-1048-btnInnerEl')]")
        # Click Crear Expediente
        expediente.explicit("//span[contains(@id,'menuitem-1050-textEl')]")
        # Comienza creación de Documento primera parte
        expediente.Documento_pt_uno()
        # CLick en Ingresar
        expediente.ingresarExpediente()
        # Click en Si
        expediente.explicit("//span[contains(@id,'button-1006-btnInnerEl')]")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnEl')]")
        # Comienza a completar la parte dos del Expediente comenzando por las observaciones
        expediente.Observaciones_dos()
        # Click en Grabar
        expediente.GrabarExpediente()
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")


        print("Documento creado")
        print("Prueba finalizada con éxito.")


    def test_tres(self):
        driver = self.driver
        expediente = CreacionDocumento(driver);

        expediente.Navegar("http://10.64.110.36:8080/ceropapel/")
        # Le indica a la pagina esperar a ver el contenido un max de 10 seg, si el contenido se muestra antes de los 10 seg, la prueba comienza, si el contenido no se muestra en 10 seg, la prueba falla
        driver.implicitly_wait(60)
        driver.maximize_window()
        # Inicio de sesión Ceropapel
        expediente.login("14331990-3")

        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")
        # Click Gestión
        expediente.explicit("//span[contains(@id,'button-1048-btnInnerEl')]")
        # Click Crear Expediente
        expediente.explicit("//span[contains(@id,'menuitem-1050-textEl')]")
        # Comienza creación de Documento primera parte
        expediente.Documento_pt_uno()
        # CLick en Ingresar
        expediente.ingresarExpediente()
        # Click en Si
        expediente.explicit("//span[contains(@id,'button-1006-btnInnerEl')]")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnEl')]")
        # Comienza a completar la parte dos del Expediente comenzando por las observaciones
        expediente.Observaciones_dos()
        # Click en Grabar
        expediente.GrabarExpediente()
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")

        print("Documento creado")
        print("Prueba finalizada con éxito.")

    def test_cuatro(self):
        driver = self.driver
        expediente = CreacionDocumento(driver);

        expediente.Navegar("http://10.64.110.36:8080/ceropapel/")
        # Le indica a la pagina esperar a ver el contenido un max de 10 seg, si el contenido se muestra antes de los 10 seg, la prueba comienza, si el contenido no se muestra en 10 seg, la prueba falla
        driver.implicitly_wait(60)
        driver.maximize_window()
        # Inicio de sesión Ceropapel
        expediente.login("11693332-2")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")
        # Click Gestión
        expediente.explicit("//span[contains(@id,'button-1048-btnInnerEl')]")
        # Click Crear Expediente
        expediente.explicit("//span[contains(@id,'menuitem-1050-textEl')]")
        # Comienza creación de Documento primera parte
        expediente.Documento_pt_uno()
        # CLick en Ingresar
        expediente.ingresarExpediente()
        # Click en Si
        expediente.explicit("//span[contains(@id,'button-1006-btnInnerEl')]")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnEl')]")
        # Comienza a completar la parte dos del Expediente comenzando por las observaciones
        expediente.Observaciones_dos()
        # Click en Grabar
        expediente.GrabarExpediente()
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")

        print("Documento creado")
        print("Prueba finalizada con éxito.")

    def test_cinco(self):
        driver = self.driver
        expediente = CreacionDocumento(driver);

        expediente.Navegar("http://10.64.110.36:8080/ceropapel/")
        # Le indica a la pagina esperar a ver el contenido un max de 10 seg, si el contenido se muestra antes de los 10 seg, la prueba comienza, si el contenido no se muestra en 10 seg, la prueba falla
        driver.implicitly_wait(60)
        driver.maximize_window()
        # Inicio de sesión Ceropapel
        expediente.login("17910338-9")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")
        # Click Gestión
        expediente.explicit("//span[contains(@id,'button-1048-btnInnerEl')]")
        # Click Crear Expediente
        expediente.explicit("//span[contains(@id,'menuitem-1050-textEl')]")
        # Comienza creación de Documento primera parte
        expediente.Documento_pt_uno()
        # CLick en Ingresar
        expediente.ingresarExpediente()
        # Click en Si
        expediente.explicit("//span[contains(@id,'button-1006-btnInnerEl')]")
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnEl')]")
        # Comienza a completar la parte dos del Expediente comenzando por las observaciones
        expediente.Observaciones_dos()
        # Click en Grabar
        expediente.GrabarExpediente()
        # Aceptar
        expediente.explicit("//span[contains(@id,'button-1005-btnInnerEl')]")

        print("Documento creado")
        print("Prueba finalizada con éxito.")


    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main();