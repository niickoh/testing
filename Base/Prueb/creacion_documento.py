import unittest

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

class CreacionDocumento:

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, Url):
        self.driver.get(Url)
        return Url

    def login(self, rut):
        t=.1
        driver = self.driver

        try:
            user = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'textfield-1023-inputEl')]")))
            user.send_keys(rut + Keys.TAB + "Ceropapel2019" + Keys.TAB + Keys.TAB + Keys.ENTER)
            CreacionDocumento.Tiempo(self, t)
        except TimeoutException as ex:
            print(ex.msg)
            driver.quit()
        return rut


    def ingresarExpediente(self):
        t = .1
        driver = self.driver

        try:

            btnIngresarExpediente = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(@id,'ZTButton-1217-btnInnerEl')]")))
            btnIngresarExpediente = driver.find_element(By.XPATH, "//span[contains(@id,'ZTButton-1217-btnInnerEl')]")
            btnIngresarExpediente.click()
            ir = driver.execute_script("arguments[0].scrollIntoView();", btnIngresarExpediente)
            CreacionDocumento.Tiempo(self, t)
        except TimeoutException as ex:
            print(ex.msg)
            print("Falló el scroll 3")
            driver.quit()

    def Documento_pt_uno(self):
        t = .1
        driver = self.driver
        inputMateriaEspecifica = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'ZTTextField-1168-inputEl')]")))
        inputMateriaEspecifica.send_keys("PRUEBA DE FOLIOS" + Keys.TAB)
        CreacionDocumento.Tiempo(self, t)

        cmbPrioridad = driver.find_element(By.XPATH, "//input[contains(@id,'ZTComboBox-1194-inputEl')]")
        cmbPrioridad.click()
        CreacionDocumento.Tiempo(self, t)
        cmbPrioridad.send_keys(
            Keys.ARROW_DOWN + Keys.ENTER + Keys.TAB + "PRUEBA DE FOLIOS" + Keys.TAB + "test, prueba, folios")
        CreacionDocumento.Tiempo(self, t)

    def Observaciones_dos(self):
        t = .1
        driver = self.driver
        try:
            observaciones2 = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//textarea[contains(@id,'ZTTextArea-1390-inputEl')]")))
            observaciones2 = driver.find_element(By.XPATH, "//textarea[contains(@id,'ZTTextArea-1390-inputEl')]")
            observaciones2.send_keys(
                "PRUEBA PARA REVISAR SOLUCIÓN DE SALTOS DE FOLIOScd")
            ir = driver.execute_script("arguments[0].scrollIntoView();", observaciones2)
            CreacionDocumento.Tiempo(self, t)
        except TimeoutException as ex:
            print(ex.msg)
            print("Falló el scroll")
            driver.quit()



    def GrabarExpediente(self):
        t = .1
        driver = self.driver
        try:
            btnGrabar = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(@id,'ZTButton-1482-btnInnerEl')]")))
            btnGrabar = driver.find_element(By.XPATH, "//span[contains(@id,'ZTButton-1482-btnInnerEl')]")
            btnGrabar.click()
            ir = driver.execute_script("arguments[0].scrollIntoView();", btnGrabar)
            CreacionDocumento.Tiempo(self, t)
        except TimeoutException as ex:
            print(ex.msg)
            print("Falló el scroll 2")
            driver.quit()

    '''"//span[contains(@id,'button-1005-btnInnerEl')]"'''
    def explicit(self, valorXPATH):
        t = .1
        driver = self.driver
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, valorXPATH)))
        element.click()
        CreacionDocumento.Tiempo(self, t)
        return valorXPATH

