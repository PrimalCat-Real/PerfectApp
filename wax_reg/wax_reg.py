from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium import webdriver
# from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import settings
# import urllib
import time
# import pyautogui

import function_for_reg

# Const parameters
byPassUrl = 'https://all-access.wax.io/'
name = function_for_reg.name
mails = function_for_reg.content
passWord = function_for_reg.password
proton_name = settings.PROTON_NAME
proton_password = settings.PROTON_PASSWORD
# grab from site
api_key = settings.API_KEY
site_key = settings.SITE_KEY
# Crome options for selenium
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension(r'D:\Users\user\Desktop\Projects\PerfectApp\wax_reg\anticaptcha-plugin_v0.56.crx')

# Useragent for antidetect
ua = UserAgent()
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')

# set driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(byPassUrl)

assert 'WAX' in driver.title, "Website did't work"
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")


# pyautogui.moveTo(1185, 56)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(1029, 208)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(846, 211)
# pyautogui.click()
# pyautogui.write(api_key, interval=0.05)
# pyautogui.moveTo(810, 125)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(1089, 135)
# pyautogui.click()
# pyautogui.moveTo(1176, 44)
# pyautogui.click()
# time.sleep(2)
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)
def type_event(name, param):
    element = driver.find_element_by_xpath(name)
    element.send_keys(param)


def wax():
    time.sleep(5)
    driver.get(byPassUrl)
    # Click reg btn
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/span')))
    nain_reg_btn = driver.find_element_by_xpath(
        '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/span')
    nain_reg_btn.click()
    print('done')
    # client = AnticaptchaClient(api_key)
    # task = NoCaptchaTaskProxylessTask(byPassUrl, site_key)
    # job = client.createTask(task)
    # print("Waiting to solution by Anticaptcha workers")
    # job.join()
    # # Receive response
    # response = job.get_solution_response()
    # print("Received solution", response)
    #
    # # Inject response in webpage
    # driver.execute_script('document.getElementById("g-recaptcha-response").innerHTML = "%s"' % response)
    #
    # # Wait a moment to execute the script (just in case).
    time.sleep(1)
    # Press submit button
    # driver.find_element_by_xpath('//button[@type="submit" and @class="btn-std"]').click()

    # Doing sign Up form in wax page
    mail_input = driver.find_element_by_xpath(
        '//*[@id="root"]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[1]/input')
    mail_input.send_keys(mails)
    print('send')
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[2]/input')))
    type_event('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[2]/input', passWord)
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[3]/input')))
    type_event('/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[3]/input', passWord)
    time.sleep(10)
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/button')))
    sign_up = WebDriverWait(driver, 100).until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/button')))
    sign_up.click()
    print(sign_up.is_enabled())
    function_for_reg.lodad_log()
    function_for_reg.del_last_line()


# wax()

def proton_mail_get_code():
    driver.get('https://protonmail.com/ru/')
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/nav/div[3]/div/div[2]/ul/li[8]/a')))
    log_in_btn_proton_mail = driver.find_element_by_xpath(
        '/html/body/div[1]/nav/div[3]/div/div[2]/ul/li[8]/a')
    log_in_btn_proton_mail.click()
    time.sleep(4)
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/label[1]/div[2]/input')))
    type_event('/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/label[1]/div[2]/input', proton_name)
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/label[2]/div[2]/div/input')))
    type_event('/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/label[2]/div[2]/div/input', proton_password)
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/button')))
    log_in_btn_confirm = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[2]/div/main/div[2]/form/button')
    log_in_btn_confirm.click()
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/div/div[2]')))
    get_wax_mail = WebDriverWait(driver, 100).until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/main/div/div/div[2]')))
    get_wax_mail.click()
    WebDriverWait(driver, 100).until(ec.presence_of_element_located(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/main/section/div/div/article[2]/div[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td/table[1]/tbody/tr[2]/td[2]/a/span')))
    get_wax_mail = WebDriverWait(driver, 100).until(ec.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/div/main/section/div/div/article[2]/div[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td/table[1]/tbody/tr[2]/td[2]/a/span')))
    get_wax_mail.click()

proton_mail_get_code()
# WebDriverWait(driver, 10).until(ec.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='проверка recaptcha']")))
# WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
# time.sleep(2)
# src = driver.find_element_by_id("audio-source").get_attribute("src")
# audio = urllib.request.urlretrieve(src, "src.mp3")
