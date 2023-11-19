from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class GitLoginPage:

    def __init__(self, driver) -> None:
        self.driver = driver
        


    
    def open_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait

    
    def find_el(self):
        element = self.driver.find_element(By.NAME,"commit")
        self.element = element

    def click_element(self):
        self.element.click()

    def check_error_msg(self):
        error_msg = self.driver.find_element(By.ID,"js-flash-container")
        return error_msg.text
        

    


      


