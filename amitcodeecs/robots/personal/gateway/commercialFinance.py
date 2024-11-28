from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Gateway Commercial Finance
# ------------------------------------------------------

def GatewayCommercialFinance(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "mobileNumber": 7349303040,
        #         "companyName": "My Company",
        #         "amountNeeded": 50000
        #     }
        # }
        driver.get("https://gatewaycfs.com/invoice-factoring/quote/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        companyName = data.get("personal").get("companyName")
        amountNeeded = data.get("personal").get("amountNeeded")

        random_sleep(20)

        driver.switch_to.frame(0)
        # Amount Needed
        write_delay(driver, '//*[@id="amount_needed-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', amountNeeded)
        random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="firstname-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastname-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', lastName)
        random_sleep(1)

        # Phone Number
        write_delay(driver, '//*[@id="mobilephone-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', mobileNumber)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="email-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', email)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="company-ea755ddc-2db7-46a9-8317-b44c30b826ec"]', companyName)
        random_sleep(1)

        # Get a Quote
        send_click(driver, '//*[@id="hsForm_ea755ddc-2db7-46a9-8317-b44c30b826ec"]/div[8]/div[2]/input')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Gateway Commercial Finance"
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
        card_name = "Gateway Commercial Finance"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
