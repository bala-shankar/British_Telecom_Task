from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
print("Hello")
driver = webdriver.Chrome()

driver.get("https://www.bt.com/")

wait = WebDriverWait(driver, 20)
iframe = wait.until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='TrustArc Cookie Consent Manager']")))

driver.switch_to.frame(iframe)
sleep(5)

accept_cookies_button = driver.find_element(By.XPATH, "//a[@role='button' and contains(text(),'Accept all cookies')]")
accept_cookies_button.click()
sleep(5)

driver.switch_to.default_content()
driver.save_screenshot("BT1.png")

sleep(5)

driver.find_element(By.XPATH, "//a[@href='https://www.bt.com/mobile']").click()
sleep(5)

driver.find_element(By.XPATH, "//a[@href='https://www.bt.com/products/mobile/phones/']").click()
sleep(5)
driver.save_screenshot("BT2.png")

if len(driver.find_elements(By.XPATH, "//div[@class='flexpay-card_card_wrapper__Antym']")) < 3:
    print("Got less than three banners under See Handset Details")

driver.find_element(By.XPATH, "//a[@href='/products/mobile/sim-only-deals/' and @class='bt-btn bt-btn-primary']").click()
sleep(5)

sim_only_title = driver.title

if sim_only_title == 'SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile':
    print('Redricted to Sim only Deals page')

double_data_elements = driver.find_elements(By.XPATH, "//div[@class='simo-card-ee_social_norm__3lfdT'][normalize-space()='30% off and double data']")
sleep(5)

if len(driver.find_elements(By.XPATH, "//div[@class='simo-card-ee_product_card_wrapper__25TU6 mt-10']//child::div[1][normalize-space()='30% off and double data'] //following::div//span[normalize-space()='was 125GB']//following::div[normalize-space()='250GB']//following::span[normalize-space()='Essential Plan']//parent::div//following-sibling::div//span[normalize-space()='was £27']//following-sibling::div[text()='18']//following::sub[normalize-space()='.90']//parent::div//following-sibling::span[normalize-space()='Per month']"))==1:
    print("Element found")
