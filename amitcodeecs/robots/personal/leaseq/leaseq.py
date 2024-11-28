from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Leaseq
# ------------------------------------------------------

def leaseq(driver, data, product_id):
    try:

        driver.get("https://www.leaseq.com/contact")
        random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="name"]', personal.get("fullName"))
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="phone"]', personal.get("mobileNumber"))
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="submit"]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Leaseq"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
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
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Leaseq"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
