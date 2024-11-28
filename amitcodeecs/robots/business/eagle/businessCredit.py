from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Eagle Business Credit
# -----------------------------------------------------------------

def eagleBusinessCredit(driver, data, product_id):
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
        #         "monthlymortage": 546,
        #         "mobileNumber": 7349303040,
        #         "bonvoyNumber": 7349303041,
        #         "occupation": "Test",
        #         "employmentType": "full-time",
        #         "bankAccount": "checking-and-savings",
        #     },
        # } 
        driver.get("https://eaglebusinesscredit.com/apply-now/")
        random_sleep(15)
        # send_click(driver, '/html/body/content-wrapper/enterprise-root/card-page/div/shared-cms-render-component/shared-cms-container-component[1]/shared-cms-base-component[3]/ng-component/card-sbc-sticky-nav/div/div/div[1]/div[2]/div/a')
        # random_sleep(15)

        personal = data.get("personal")
        email = data.get("email")

        random_sleep(20)
        # Full Name
        write_delay(driver, '//*[@id="fullname"]', personal.get("fullName"))
        random_sleep(1)
        
        # Company name
        write_delay(driver, '//*[@id="customer_account"]', personal.get("companyName"))
        random_sleep(1)
        
        
        # Email Address
        write_delay(driver, '//*[@id="email"]', email)
        random_sleep(1)
        
        # Primary Phone Number
        write_delay(driver, '//*[@id="phone"]', personal.get("mobileNumber"))
        random_sleep(1)
        
        # Businss description
        write_delay(driver, '//*[@id="field[33]"]', personal.get("desc"))
        random_sleep(1)
        
        # Submit Application
        send_click(driver, '//*[@id="_form_23_submit"]')
        random_sleep(10)
        
        full_name = personal.get("firstName") + " " + personal.get("lastName")
        card_name = "Eagle Business Credit"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
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
        full_name = data.get("personal").get("firstName") + " " + data.get("personal").get("lastName")
        card_name = "Eagle Business Credit"
        filepath = f"FinalScreenshots/business/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
