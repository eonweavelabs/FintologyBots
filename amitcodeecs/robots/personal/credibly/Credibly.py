from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Credibly
# -----------------------------------------------------------------

def Credibly(driver, data, product_id):
    try:
        driver.get("https://www.credibly.com/apply-online/")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        companyName = data.get("personal").get("companyName")
        email = data.get("email")
        phoneNumber = data.get("personal").get("mobileNumber")
        industry = data.get("business").get("industry")
        timeInBusiness = data.get("business").get("timeInBusiness")
        monthlyDeposits = data.get("business").get("monthlyDeposits")
        revenueDeposited = data.get("business").get("revenueDeposited")

        random_sleep(20)
        driver.switch_to.frame(0)
        # First Name
        write_delay(driver, '//*[@id="firstname-31d0af5c-6269-4368-983d-8e689878679a"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastname-31d0af5c-6269-4368-983d-8e689878679a"]', lastName)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="company-31d0af5c-6269-4368-983d-8e689878679a"]', companyName)
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="email-31d0af5c-6269-4368-983d-8e689878679a"]', email)
        random_sleep(1)

        # Phone Number
        write_delay(driver, '//*[@id="phone-31d0af5c-6269-4368-983d-8e689878679a"]', phoneNumber)
        random_sleep(1)

        # Industry
        write_delay(driver, '//*[@id="industry_dropdown-31d0af5c-6269-4368-983d-8e689878679a"]', industry)
        random_sleep(1)

        # How long have you been in business?
        write_delay(driver, '//*[@id="tib-31d0af5c-6269-4368-983d-8e689878679a"]', timeInBusiness)
        random_sleep(1)

        # What's the average monthly deposit into your business bank account?
        write_delay(driver, '//*[@id="monthly_deposits-31d0af5c-6269-4368-983d-8e689878679a"]', monthlyDeposits)
        random_sleep(1)

        # Is your revenue deposited into a business bank account?
        write_delay(driver, '//*[@id="business_bank_account_drop_down-31d0af5c-6269-4368-983d-8e689878679a"]', revenueDeposited)
        random_sleep(1)

        # Agree to receive text messages
        send_click(driver, '//*[@id="sms_opt_out-31d0af5c-6269-4368-983d-8e689878679a"]')
        random_sleep(2)

        # Submit button
        send_click(driver, '//*[@id="hsForm_31d0af5c-6269-4368-983d-8e689878679a"]/div/div[2]/input')
        random_sleep(15)

        full_name = f"{firstName} {lastName}"
        card_name = "Credibly"
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
        card_name = "Credibly"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
