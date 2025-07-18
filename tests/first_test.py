from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager    
from selenium.webdriver.chrome.options import Options

def test_page_title():
   # browser = webdriver.Chrome() #service=Service("/Users/orozas/Adalid/selenium/chrome/chromedriver")
    #browser.get("https://github.com")
    
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Crear un directorio temporal único para user-data-dir
    tmp_profile_dir = tempfile.mkdtemp(prefix="chrome-profile-")
    options.add_argument(f'--user-data-dir={tmp_profile_dir}')

    browser = webdriver.Chrome(options=options)
    
    
    titleElement = browser.find_element(By.ID,"hero-section-brand-heading")
    
    
    
    
    assert titleElement.text == "Build and ship software on a single, collaborative platform"
    browser.quit()
