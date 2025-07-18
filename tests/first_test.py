from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.options import Options

def test_page_title():
    browser = webdriver.Chrome() #service=Service("/Users/orozas/Adalid/selenium/chrome/chromedriver")
    browser.get("https://github.com")
    
    titleElement = browser.find_element(By.ID,"hero-section-brand-heading")
    
    assert titleElement.text == "Build and ship software on a single, collaborative platform"
    browser.quit()
