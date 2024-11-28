from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Can Capital
# ------------------------------------------------------

def canCapital(driver, data, product_id):
    try:        
        driver.get("https://applynow.cancapital.com/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        businessLegalName = data.get("business").get("legalName")
        dba = data.get("business").get("dba")
        startDate = data.get("business").get("startDate")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="mat-input-0"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="mat-input-1"]', lastName)
        random_sleep(1)

        # Email Address
        write_delay(driver, '//*[@id="mat-input-2"]', email)
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="mat-input-3"]', mobileNumber)
        random_sleep(1)

        # Business Legal Name
        write_delay(driver, '//*[@id="mat-input-4"]', businessLegalName)
        random_sleep(1)

        # Doing bussiness as
        write_delay(driver, '//*[@id="mat-input-5"]', dba)
        random_sleep(1)

        # Agree to Privacy Policy
        send_click(driver, '//*[@id="mat-mdc-checkbox-1"]/div/label')
        random_sleep(1)

        # Consent to Marketing
        send_click(driver, '//*[@id="StepForm1"]/div[5]')
        random_sleep(5)


        # Bussiness start date
        write_delay(driver, '//*[@id="mat-input-6"]', startDate )
        random_sleep(1)


        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/form/div[2]/div[2]/nz-radio-group/label[2]')
        random_sleep(1)

        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/form/div[3]/div[2]/nz-radio-group/label[2]')
        random_sleep(1)

        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/form/div[4]/div[2]/nz-radio-group/label[1]')
        random_sleep(1)

        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/form/div[5]/div[2]/button')
        random_sleep(5)

        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/div[1]/div[2]/div[2]/div/nz-radio-group/label')
        random_sleep(1)

        send_click(driver, '/html/body/app-root/div/stepsforms/div/div/div/div/div[3]/div[2]/button')
        random_sleep(5)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Can Capital"
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
        full_name = f"{data.get('personal').get('firstName')} {data.get('personal').get('lastName')}"
        card_name = "Can Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
