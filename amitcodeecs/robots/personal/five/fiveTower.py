from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# -------------------------------------------------------
# Five Tower
# -------------------------------------------------------

def fiveTower(driver,data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "citizenship": "Indiam",
        #         "firstName": "Krishan Pratap",
        #         "middleName": "Test",
        #         "lastName": "lastName",
        #         "dob": "08/15/2001",
        #         "ssn": 873948923,
        #         "membership": 456836297456,
        #         "housingStatus": "Own",
        #         "grossIncome": 546843,
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 30201,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get("https://www.towerfive.com/contact/")
        # send_click(
        #     driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[1]/a')
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        company = data.get("company")
        revenue = data.get("revenue")
        grossIncome = data.get("personal").get("householdIncome")
        
        random_sleep(20)
        
        # First Name
        write_delay(
            driver,
            '//*[@id="input_5_1"]', 
            firstName
        )
        
        random_sleep(1)

        # Last name 
        write_delay(
            driver, 
            '//*[@id="input_5_10"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
        # Email
        write_delay(
            driver, 
            '//*[@id="input_5_12"]', 
            email
        )
        random_sleep(1)
        random_sleep(1)
        
        # Company
        write_delay(
            driver, 
            '//*[@id="input_5_3"]', 
            company
        )
        random_sleep(1)
        random_sleep(1)
        
        # Revenue
        write_delay(
            driver, 
            '//*[@id="input_5_7"]', 
            revenue
        )
        random_sleep(1)
        random_sleep(1)
        
        # Gross annual income
        write_delay(
            driver,
            '//*[@id="input_5_8"]',
            grossIncome
        )
        random_sleep(1)
        
        # Submit
        send_click(driver, '//*[@id="gform_submit_button_5"]')
        random_sleep(15)
        
        retry_count = 0
        while retry_count < 600:
            try:
                driver.find_element(
                    by=By.XPATH, value='//*[@id="CONFIRMATION_ADVISORY"]'
                )
                break
            except:
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Five Tower"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

    except:
        traceback.print_exc()
        input("Error in application")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Five Tower"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

