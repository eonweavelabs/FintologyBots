from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# -------------------------------------------------------
# Clearfund
# -------------------------------------------------------

def clearfund(driver,data, product_id):
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
        driver.get("https://www.clearfund.co/apply-now")
        # send_click(
        #     driver, '/html/body/div[1]/div/div[1]/div/div/header/div[3]/div[2]/div/div[2]/div[1]/div[1]/a')
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        email = data.get("email")
        phone = data.get("phone")
        company = data.get("company")
        revenue = data.get("revenue")
        time = data.get("time")
        position = data.get("position")
        money = data.get("money")
        
        random_sleep(20)
        
        # Full Name
        write_delay(
            driver,
            '//*[@id="input_comp-k7gftl1y"]', 
            f'{firstName} {lastName}'
        )
        
        random_sleep(1)

        write_delay(
            driver,
            '//*[@id="input_comp-k7gg9f56"]', 
            company
        )
        
        random_sleep(1)
        
        # Email
        write_delay(
            driver, 
            '//*[@id="input_comp-k7ggagme"]', 
            email
        )
        random_sleep(1)
        
        # revenue
        write_delay(
            driver, 
            '//*[@id="input_comp-k7gftl2y"]', 
            revenue
        )
        random_sleep(1)
        
        # time
        write_delay(
            driver, 
            '//*[@id="input_comp-k7gftl3f"]', 
            time
        )
        random_sleep(1)

        # position
        write_delay(
            driver, 
            '//*[@id="input_comp-k7gfwg4s"]', 
            position
        )
        random_sleep(1)

        # money
        write_delay(
            driver, 
            '//*[@id="input_comp-k7gfwla2"]', 
            money
        )
        random_sleep(1)
        
        # Phone
        write_delay(
            driver, 
            '//*[@id="input_comp-k7ggc4c0"]', 
            phone
        )
        random_sleep(1)
        random_sleep(1)
        # send_click(driver , '//*[@id="wpforms-500-field_4"]/li/label')
        # random_sleep(1)
        
        # Submit
        send_click(driver, '//*[@id="comp-k7gftl4f"]/button')
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
        card_name = "Clearfund"
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
        card_name = "Clearfund"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id,flag)
        

