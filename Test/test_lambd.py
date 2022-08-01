import os
import pytest
import requests
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import logging as logger
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

username = 'Pawan7593'
access_key = 'ZqUuuwHmf7zGkrte88kDIMw1fL2sSDpJxvNcDVCAvjD3QktycK'
desired_caps_crome = {
    "build" : "V1.0",
    "name" : "LambdaTestPlaygorund",
    "platform" : "Windows 10",
    "browserName" : "Chrome",
	"resolution": "1024x768",
    "version" : "103.0",
    "network" : True,
    "video": True,
    "visual": True,
    "console": True
    }
desired_caps_edge = {
    "build" : "V1.0",
	"name" : "LambdaTestPlaygorund_edge",
	"platform" : "Windows 10",
	"browserName" : "MicrosoftEdge",
    "version" :  "94.0",
	"resolution": "1024x768",
    "network" : True,
	"video": True,
    "visual": True,
    "console": True,
	}



@pytest.mark.test01
def test_lambda01():
    #driver = webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),desired_capabilities=desired_caps_crome)
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="E:\\Pawan\\Study\\selenuimPython\\chromedriver_103.exe")
    driver.maximize_window()
    # steps for login on LambdaTest Selenium Playground
    driver.get("https://www.lambdatest.com/automation-demos")
    driver.find_element_by_id("username").send_keys("lambda")
    driver.find_element_by_id("password").send_keys("lambda123")
    driver.find_element_by_css_selector("#newapply > div.w-360.ml-auto.text-center.smtablet\:w-full.smtablet\:ml-0 > button").click()
    # fill form on Selenium playground page
    driver.find_element_by_id("developer-name").send_keys("testmail@gmail.com")
    driver.find_element_by_xpath('//*[@id="populate"]').click()
    driver.switch_to.alert.accept()
    driver.find_element_by_css_selector("input[value='Every month']").click()
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element_by_css_selector("label[for='customer-service'] input[type='checkbox']").click()
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element_by_css_selector("#preferred-payment > option:nth-child(3)").click()
    driver.find_element_by_name("tried-ecom").click()
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(1)
    slider = driver.find_element_by_css_selector("div[role='slider']")
    ActionChains(driver).click_and_hold(slider).move_by_offset(256, 0).release().perform()
    Slider_position_value = driver.find_element_by_css_selector("div[role='slider']").get_attribute("aria-valuenow")
    # assert for slider at 9 no position
    logger.info(f"Slider position: {Slider_position_value}")
    assert Slider_position_value == "90", f"Expected response of slider is 90 , Actaul response {Slider_position_value}"
    driver.execute_script("window.scrollTo(0, 900);")
    driver.find_element_by_name("comments").send_keys("Feedback")
    # open new tab for download image
    driver.execute_script("window.open('https://www.lambdatest.com/selenium-automation');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollTo(0, 4500);")
    time.sleep(2)
    img = driver.find_element_by_css_selector("img[title='Jenkins']").get_attribute("src")
    r = requests.get(img)
    path = os.getcwd()
    open(path + '/jenkins.svg', 'wb').write(r.content)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_css_selector("input[type='file']").send_keys(os.getcwd() + "/jenkins.svg")
    logger.info(os.getcwd() + "/jenkins.svg")
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert_txt = alert.text
    alert.accept()
    # assert for upload image success
    assert alert_txt == 'your image upload sucessfully!!', f"Expected res 'your image upload sucessfully!!' Actual response {alert_txt}"
    time.sleep(2)
    button = driver.find_element_by_css_selector('#submit-button')
    driver.execute_script("arguments[0].click();", button)
    driver.execute_script("window.scrollTo(0, 200);")
    alert_txt2 = driver.find_element_by_xpath("(//p[contains(@class,'mb-10 text-gray-800 mt-20')])[1]").text
    # assert for submit form successfully
    assert alert_txt2 == 'You have successfully submitted the form.', f"Expected res 'You have successfully submitted the form.' Actual response {alert_txt}"
    time.sleep(3)
    driver.quit()


@pytest.mark.test02
def test_lambda02():
    #driver = webdriver.Remote(command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),desired_capabilities=desired_caps_edge)
    driver = webdriver.Chrome("E:\\Pawan\\Study\\selenuimPython\\chromedriver.exe")
    driver.maximize_window()
    # steps for login on LambdaTest Selenium Playground
    driver.get("https://www.lambdatest.com/automation-demos")
    driver.find_element_by_id("username").send_keys("lambda")
    driver.find_element_by_id("password").send_keys("lambda123")
    driver.find_element_by_css_selector("button[type='submit']").click()
    # fill form on Selenium playground page
    driver.find_element_by_id("developer-name").send_keys("testmail@gmail.com")
    driver.find_element_by_xpath('//*[@id="populate"]').click()
    driver.switch_to.alert.accept()
    driver.find_element_by_css_selector("input[value='Every month']").click()
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element_by_css_selector("label[for='customer-service'] input[type='checkbox']").click()
    driver.execute_script("window.scrollTo(0, 500);")
    driver.find_element_by_css_selector("option:nth-child(3)").click()
    driver.find_element_by_name("tried-ecom").click()
    driver.execute_script("window.scrollTo(0, 700);")
    time.sleep(1)
    slider = driver.find_element_by_css_selector("div[role='slider']")
    ActionChains(driver).click_and_hold(slider).move_by_offset(256, 0).release().perform()
    Slider_position_value = driver.find_element_by_css_selector("div[role='slider']").get_attribute("aria-valuenow")
    # assert for slider at 9 no position
    logger.info(f"Slider position: {Slider_position_value}")
    assert Slider_position_value == "90", f"Expected response of slider is 90 , Actaul response {Slider_position_value}"
    driver.execute_script("window.scrollTo(0, 900);")
    driver.find_element_by_name("comments").send_keys("Feedback")
    # open new tab for download image
    driver.execute_script("window.open('https://www.lambdatest.com/selenium-automation');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script("window.scrollTo(0, 4500);")
    time.sleep(2)
    img = driver.find_element_by_css_selector("img[title='Jenkins']").get_attribute("src")
    r = requests.get(img)
    path = os.getcwd()
    open(path + '/jenkins.svg', 'wb').write(r.content)
    driver.switch_to.window(driver.window_handles[0])
    driver.find_element_by_css_selector("input[type='file']").send_keys(os.getcwd() + "/jenkins.svg")
    logger.info(os.getcwd() + "/jenkins.svg")
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert_txt = alert.text
    alert.accept()
    # assert for upload image success
    assert alert_txt == 'your image upload sucessfully!!', f"Expected res 'your image upload sucessfully!!' Actual response {alert_txt}"
    driver.find_element_by_css_selector("#submit-button").click()
    driver.execute_script("window.scrollTo(0, 200);")
    alert_txt2 = driver.find_element_by_xpath("(//p[contains(@class,'mb-10 text-gray-800 mt-20')])[1]").text
    # assert for submit form successfully
    assert alert_txt2 == 'You have successfully submitted the form.', f"Expected res 'You have successfully submitted the form.' Actual response {alert_txt}"
    time.sleep(3)
    driver.quit()

