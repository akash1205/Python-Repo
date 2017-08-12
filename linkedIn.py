from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome import *

username = input("Enter LinkedIn Username")
password = input("Enter LinkedIn Passowrd")

webdriver.chrome.webdriver.WebDriver.get("https://www.linkedin.com/")
