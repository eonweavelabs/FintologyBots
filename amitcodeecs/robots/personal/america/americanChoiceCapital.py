from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# American Choice Capital
# ------------------------------------------------------

def americanChoiceCapital(driver, data, product_id):
    try:
        #data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "ssn": 124365888,
        #         "housingStatus": "own",
        #         "grossIncome": 876655,
        #         "mobileNumber": 7349303040,
        #         "employmentType": "full-time",
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "city": "Jaipur",
        #         "homeAddress": "123 street",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get("https://americanchoicecapital.com/apply")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        grossIncome = data.get("personal").get("householdIncome")

        random_sleep(20)
        
        send_click(driver, '//*[@id="popup-widget50952"]/div/div/div[1]')
        random_sleep(1)
        # Name
        write_delay(driver, '//*[@id="input1"]', f"{firstName} {lastName}")
        random_sleep(1)

        # Email
        write_delay(driver, '//*[@id="input13"]', email)
        random_sleep(1)

        # Amount of
        write_delay(driver, '//*[@id="input91"]', grossIncome)
        random_sleep(1)

        # Time in Business
        write_delay(driver, '//*[@id="input101"]', "10 years")
        random_sleep(1)

        # Estimated Revenue
        write_delay(driver, '//*[@id="input111"]', grossIncome)
        random_sleep(1)

        # Message
        write_delay(driver, '//*[@id="input111"]', "This is a test message.")
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "American Choice Capital"
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
        card_name = "American Choice Capital"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
