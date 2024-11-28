from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Truist Future Credit Card
# -----------------------------------------------------

def TruistFutureCreditCard(driver, data, product_id):
    try:
        driver.get(
            "https://www.truist.com/credit-cards/future"
        )
        random_sleep(15)
        
        send_click(driver, '//*[@id="cta-70532058"]/a')
        random_sleep(15)
        driver.switch_to.window(driver.window_handles[-1])
        # Start application
        send_click(driver, '//*[@id="cta-8"]/button')
        random_sleep(5)
        
        # data = {
        #     "personal": {
        #         "firstName": "John",
        #         "lastName": "Doe",
        #         "email": "johndoe@example.com",
        #         "isMajorityOwnerForeign": "No",  # or "Yes"
        #         "hasForeignOperations": "No",  # or "Yes"
        #         "zipCode": "28202",
        #         "organizationName": "Doe Enterprises",
        #         "ssn": "123-45-6789",
        #         "phone": "1234567890",
        #         "date": "01/01/2024",
        #         "state": "NY",
        #         "numOfEmployees": "5",
        #         "annualSales": "500000",
        #         "activities": "Technology consulting and solutions.",
        #         "address": "123 Main Street",
        #         "dob": "01/01/1990",
        #         "city": "New York",
        #         "residentSince": "01/2010"
        #     },
        #     "email": "johndoe@example.com",
        #     "application_id": "APP123456",
        # }


        personal = data.get("personal")

        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        email = data.get("email")
        isMajorityOwnerForeign = personal.get("isMajorityOwnerForeign")
        hasForeignOperations = personal.get("hasForeignOperations")
        

        
        send_click(driver, '//*[@id="buttonNo"]')
        random_sleep(1)
        # ZIP code
        write_delay(
            driver,
            '//*[@id="tru-core-input-2"]',
            personal.get("zipCode")
        )
        random_sleep(1)
        send_click(driver, '//*[@id="cta-16"]/button')
        random_sleep(10)
        
        # First Name
        write_delay(
            driver,
            '//*[@id="firstName"]',
            firstName
        )
        random_sleep(1)
        # Last Name
        write_delay(
            driver,
            '//*[@id="lastName"]',
            lastName
        )
        random_sleep(1)
        # Email Address
        write_delay(
            driver,
            '//*[@id="tru-core-input-6"]',
            email
        )
        random_sleep(1)
        # Citizenship
        send_click(
            driver,
            '//*[@id="tru-core-input-25"]',
        )
        random_sleep(1)
        send_click(driver, '//*[@id="5-option-id-5"]')
        random_sleep(1)
        # dob
        write_delay(
            driver,
            '//*[@id="tru-core-input-3"]',
            personal.get("dob")
        )
        random_sleep(1)
        # SSN
        write_delay(
            driver,
            '//*[@id="tru-core-input-20"]',
            personal.get("ssn")
        )
        # phone
        write_delay(
            driver,
            '//*[@id="tru-core-input-4"]',
            personal.get("phone")
        )
        random_sleep(1)
        
        # Owner
        send_click(
            driver,
            '//*[@id="tru-core-input-27"]',
        )
        random_sleep(1)
        send_click(driver, '//*[@id="26-option-id-5"]')
        random_sleep(1)
        
        # Address
        write_delay(
            driver,
            '//*[@id="stack-8"]/div/div/div/input',
            personal.get("address")
        )
        random_sleep(1)
        
        # city
        write_delay(
            driver,
            '//*[@id="tru-core-input-9"]',
            personal.get("city")
        )
        random_sleep(1)
        # State 
        select_element = driver.find_element(
            by=By.XPATH,
            value='//*[@id="tru-core-input-29"]'
        )
        random_sleep(1)
        driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, personal.get("state"))

        random_sleep(1)
        # zip
        # write_delay(
        #     driver,
        #     '//*[@id="tru-core-input-50"]',
        #     personal.get("zipCode")
        # )
        random_sleep(1)
        # Resident since
        write_delay(
            driver,
            '//*[@id="tru-core-input-7"]',
            personal.get("residentSince")
        )

        # Employment status
        select_element = driver.find_element(
            by=By.XPATH,
            value='//*[@id="tru-core-input-38"]'
        )
        random_sleep(1)
        driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, 'Employed')
        random_sleep(1)
        # Company
        write_delay(
            driver,
            '//*[@id="compName"]',
            personal.get("companyName")
        )
        random_sleep(1)
        # type
        write_delay(
            driver,
            '//*[@id="compTitle"]',
            personal.get("type")
        )
        random_sleep(1)
        # start date
        write_delay(
            driver,
            '//*[@id="tru-core-input-47"]',
            personal.get("startDate")
        )
        random_sleep(1)
        
        # annual income
        write_delay(
            driver,
            '//*[@id="tru-core-input-46"]',
            personal.get("annualInccome")
        )
        random_sleep(1)
        # Consent to Use Electronic Signatures and Records
        random_sleep(1)
        send_click(driver,'//*[@id="cta-19"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-32"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="tru-core-checkbox-input-1"]')
        random_sleep(2)
        send_click(driver,'//*[@id="tru-core-checkbox-input-2"]')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-17"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-36"]/button')
        random_sleep(20)


        full_name = f"{firstName} {lastName}"
        card_name = "Truist Future Credit Card"
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
        full_name = f"{firstName} {lastName}"
        card_name = "Truist Future Credit Card"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
