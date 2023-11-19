import pytest

from selenium import webdriver 
import time
from src.applications.github.ui.base_page import GitLoginPage
from src.config.config1 import *

base_page = GitLoginPage(webdriver.Chrome())  



def test_github_login_negative():
    base_page.open_page(f"{base_url}/login")
    base_page.find_el()
    base_page.click_element()
    base_page.check_error_msg()
    assert base_page.check_error_msg()  == "Incorrect username or password."

   

   