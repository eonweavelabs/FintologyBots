from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
import socket
from Utils.constants import DEV_MACHINE_NAME

def write_delay(driver,xpath, text, clear=True, delay=0.05):
    print(xpath)
    print(text)
    if(socket.gethostname() not in DEV_MACHINE_NAME):
        delay=0.2
    bylist=[By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.XPATH, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME]
    bylist=[By.LINK_TEXT, By.XPATH, By.CSS_SELECTOR]
    for by_val in bylist:
        try:
            driver.find_element(by=by_val, value=xpath)
            break
        except:
             pass
    text=str(text)
    if(clear):
        # driver.find_element(by=by_val, value=xpath).clear()
        print(by_val)
        print(xpath)
        driver.find_element(by=by_val, value=xpath).send_keys(Keys.CONTROL, "a", Keys.DELETE)
    
    for x in text:
        
        retry_counter=0
        while retry_counter<100:
            try:
                driver.find_element(by=by_val, value=xpath).send_keys(x)
                break        
                # try:
                #     driver.find_element(by=By.XPATH, value=xpath).send_keys(x)
                #     break
                # except:
                #     driver.find_element(by=By.CSS_SELECTOR, value=xpath).send_keys(x)
                #     break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_counter+=1
                sleep(0.1)
        sleep(randint(max((delay*100)-20, 0), ((delay*100)+10))/100)