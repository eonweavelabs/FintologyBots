from time import sleep
from selenium.webdriver.common.by import By
from random import randint


def send_click2(driver, xpath, delay=0.2, index=None, element=None):
    print("Sending click 2")
    bylist = [By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.XPATH, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME]
    bylist = [By.LINK_TEXT, By.XPATH, By.CSS_SELECTOR]
    for by_val in bylist:
        try:
            driver.find_elements(by=by_val, value=xpath)
            break
        except:
            pass
    sleep(1)
    retry_counter = 0
    while retry_counter < 200:
        try:
            if element:
                elements = element.find_elements(by=by_val, value=xpath)
                for elem in elements:
                    try:
                        print(elem, 'element')
                        elem.click()
                        break
                    except:
                        continue  
            else:
                driver.find_elements(by=by_val, value=xpath).click()
            break
        except:
            driver.execute_script("window.scrollBy(0,3)")
            retry_counter += 1
            sleep(0.1)
    sleep(randint(max((delay * 100) - 20, 0), ((delay * 100) + 20)) / 100)
