import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'launch Chrome browser')
def LanchingBorwser(context):
    context.driver = webdriver.Chrome(executable_path='C:\\Users\\Asus\\PycharmProjects\\PythonModelFramework'
                                                      '\\chromedriver.exe')
    context.driver.maximize_window()
    url = "http://allucyne.mobelite.fr/login/"
    context.driver.get(url)


@when(u'CLiquer sur Ajouter un uster saisir username user et password bitnami')
def Login(context):
    context.driver.find_element(By.XPATH, "(//input[@id='username'])[1]").send_keys("user")
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("bitnami")
    context.driver.find_element(By.XPATH, "//button[@id='loginbtn']").click()
    time.sleep(1.5)


@then(u'open home page et cliquer sur administration du site')
def GoToAdministrationDuSite(context):
    context.driver.find_element(By.XPATH, "//div[@class='custom_card account']").click()
    time.sleep(1.5)
    context.driver.find_element(By.XPATH, "//div[@class='dashbord_nav_list']//a[normalize-space()='Administration du "
                                          "site']").click()
    time.sleep(1.5)


@then(u'Remplir les champs et Cliquer sur le bouton Ajouter un user')
def AddUser(context):
    context.driver.find_element(By.XPATH,
                                "//a[normalize-space()='Ajouter un utilisateur']").click()
    time.sleep(1.5)
    context.driver.find_element(By.ID, "id_username").send_keys("amin29")
    time.sleep(1.0)
    context.driver.find_element(By.XPATH, "//input[@id='id_createpassword']").click()
    context.driver.find_element(By.XPATH, "//input[@id='id_profile_field_code_etudiant']").send_keys("KFKD6")
    time.sleep(1.0)
    context.driver.find_element(By.XPATH, "//input[@id='id_profile_field_nom_marital']").send_keys("MDJS")
    time.sleep(1.0)
    context.driver.find_element(By.XPATH, "//input[@id='id_profile_field_code_diplome']").send_keys("MDJS")
    time.sleep(1.0)
    context.driver.find_element(By.ID, "id_firstname").send_keys("Amin")
    time.sleep(1.0)
    context.driver.find_element(By.ID, "id_lastname").send_keys("Miladi")
    time.sleep(1.0)
    context.driver.find_element(By.ID, "id_email").send_keys("amin29.miladi@gmail.com")
    time.sleep(1.0)
    context.driver.find_element(By.ID, "id_submitbutton").click()
    time.sleep(2.0)
