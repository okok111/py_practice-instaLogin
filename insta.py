from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
 
CHROMEDRIVER = "C:\Chrome_Driver\chromedriver.exe"
DOMAIN_BASE = "https://www.instagram.com/"
LOGIN_ID = ""
PASSWORD = ""

def get_driver():
  driver = webdriver.Chrome(CHROMEDRIVER)   
  return driver
 
def do_login(driver):
  login_url = DOMAIN_BASE + "accounts/login/"
  driver.get(login_url)
    
  elem_id = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.NAME, "username"))
     )
      
  try:
      elem_password = driver.find_element_by_name("password")
    
      if elem_id and elem_password:
            
         elem_id.send_keys(LOGIN_ID)
                      
         elem_password.send_keys(PASSWORD)
                               
         elem_btn = WebDriverWait(driver, 10).until(
           EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button'))
         )
             
         actions = ActionChains(driver)
         actions.move_to_element(elem_btn)
         actions.click(elem_btn)
         actions.perform()
 
         time.sleep(15)

         perform_url = driver.current_url
              
         if perform_url.find(login_url) == -1:
             return True
         else:
             return False            

      else:
         return False
  except:
      return False 
         
if __name__ == "__main__":

    driver = get_driver()

    login_flg = do_login(driver)

    if login_flg is True:
        url = 'https://www.instagram.com/explore/tags/dog/'
        driver.get(url)
        driver.set_window_size(1600, 1200)
        time.sleep(15)
        driver.save_screenshot('screenshot.png')
