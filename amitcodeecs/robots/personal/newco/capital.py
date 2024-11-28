from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Newco Capital
# -----------------------------------------------------------------

def newcoCapital(driver, data, product_id):
    try:
        driver.get("https://www.newcocapitalgroup.com")
        random_sleep(15)
        
        send_click(driver, '//*[@id="comp-l4gs3rgv"]/a')  # Contact Us

        personal = data.get("personal")
        email = personal.get("email")
        first_name = personal.get("first_name")
        last_name = personal.get("last_name")
        phone = personal.get("phone")
        who_are_you = personal.get("who_are_you")
        business_website = personal.get("business_website")
        send_message = personal.get("send_message")

        random_sleep(20)
        
        # Business Information
        driver.switch_to.frame(0)
        write_delay(driver, '//*[@id="6wmj24x3_1698070028088"]/input', email)
        random_sleep(1)
        write_delay(driver, '//*[@id="1d59c4d2_1698090875077-fname"]', first_name)
        random_sleep(1)
        write_delay(driver, '//*[@id="1d59c4d2_1698090875077-lname"]', last_name)
        random_sleep(1)
        # driver.switch_to.default_content()
        write_delay(driver, '//*[@id="6b6322d8_1698090969468"]', 5252)
        random_sleep(1)
        send_click(driver, '//*[@id="kf65yrna_1698070028088"]/div[2]/div/div[1]')
        random_sleep(1)
        send_click(driver, '//*[@id="kf65yrna_1698070028088"]/div[2]/ul/li[2]/label')
        random_sleep(1)
        write_delay(driver, '//*[@id="5c3e4793_1698091008713"]/input', business_website)
        random_sleep(1)
        send_click(driver, '//*[@id="submitButton"]')  # NEXT
        random_sleep(1)
        send_click(driver, '//*[@id="recaptcha-anchor"]')  # NEXT
        write_delay(driver, '//*[@id="bhnjla6u_1698070028089"]/textarea', send_message)
        random_sleep(10)
        
        card_name = "Newco Capital"
        filepath = f"FinalScreenshots/business/{first_name} {last_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        card_name = "Newco Capital"
        filepath = f"FinalScreenshots/business/{first_name} {last_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
