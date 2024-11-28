from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Divy Bill
# ------------------------------------------------------

def divyBill(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "jobTitle": "Software Engineer",
        #         "companyName": "Tech Corp",
        #         "numberOfEmployees": "50-100",
        #         "mobileNumber": 7349303040,
        #     }
        # }
        driver.get("https://www.bill.com/product/spend-and-expense")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        jobTitle = data.get("personal").get("jobTitle")
        companyName = data.get("personal").get("companyName")
        numberOfEmployees = data.get("personal").get("numberOfEmployees")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")

        random_sleep(20)

        # First Name
        write_delay(driver, '//*[@id="firstName"]', firstName)
        random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastName"]', lastName)
        random_sleep(1)

        # Job Title
        write_delay(driver, '//*[@id="jobTitle-2"]', jobTitle)
        random_sleep(1)

        # Work Email
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)

        # Phone
        write_delay(driver, '//*[@id="phone"]', mobileNumber)
        random_sleep(1)

        # Company Name
        write_delay(driver, '//*[@id="name"]', companyName)
        random_sleep(1)

        # Number of Employees
        write_delay(driver, '//*[@id="numberOfEmployees"]', numberOfEmployees)
        random_sleep(1)

        # I'm With a Small or midsize business
        # send_click(driver, '//*[@id="direct"]')
        # random_sleep(1)

        # Accounting Firm
        # send_click(driver, '//*[@id="console"]')
        # random_sleep(1)

        # GET STARTED
        send_click(driver, '//*[@id="se-form-button"]')
        random_sleep(15)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Divy Bill"
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
        card_name = "Divy Bill"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
