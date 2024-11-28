from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Funding Circle
# ------------------------------------------------------

def fundingCircle(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "companyNumber": "10421632",
        #     "personal" : {

        #     }
        # }
        driver.get("https://www.fundingcircle.com/uk/borrower/rewards-apply/eligibility")
        random_sleep(15)

        email = data.get("email")
        companyNumber = data.get("companyNumber")
        personal = data.get("personal")

        random_sleep(20)

        # company Number
        write_delay(driver, '//*[@id="company"]', companyNumber)
        random_sleep(5)
        send_click(driver, '//*[@id="root"]/div/div[2]/section/div/div/form/div[1]/ul/li')
        random_sleep(1)


        # company Email
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Check
        send_click(driver, '//*[@id="eligibility-submit-button"]')
        random_sleep(15)

      
       
        # Screenshot and upload
        full_name = f"{personal.get('firstName')} {personal.get('lastName')}"
        card_name = "Funding Circle"
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
        card_name = "Funding Circle"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)

