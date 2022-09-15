from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\HP\Desktop\Images\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fref%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, "ap_email").send_keys("chandshaik321@gmail.com")
driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "ap_password").send_keys("Chang@786")
driver.find_element(By.ID, "signInSubmit").click()
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Sony Bravia 139 cm")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, "//div/span/a/div/img[@data-image-index='1']").click()

dropdown = Select(driver.find_elements(By.XPATH, "select[id='quantity']"))
dropdown.select_by_value(5)

driver.find_element(By.XPATH, "//span/input[@type='button']").click()