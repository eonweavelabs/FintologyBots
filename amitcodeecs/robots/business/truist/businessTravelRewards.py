from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------
# Truist Business Travel Rewards
# -----------------------------------------------------

def TruistBusinessTravelRewards(driver, data, product_id):
    try:
        driver.get(
            "https://www.truist.com/small-business/credit-cards/business-travel-rewards"
        )
        random_sleep(15)
        
        send_click(driver, '//*[@id="cta-1326083163"]/a')
        random_sleep(15)
        driver.switch_to.window(driver.window_handles[-1])
        # Start application
        send_click(driver, '//*[@id="cta-8"]/button')
        random_sleep(5)

        # Default data with dummy values
        # data = {
        #     "personal": {
        #         "firstName": "John",
        #         "lastName": "Doe",
        #         "isAuthorizedRepresentative": "Yes",
        #         "isMajorityOwnerForeign": "No",
        #         "hasForeignOperations": "No"
        #     },
        #     "email": "john.doe@example.com",
        # }

        personal = data.get("personal")

        firstName = personal.get("firstName")
        lastName = personal.get("lastName")
        email = data.get("email")
        isMajorityOwnerForeign = personal.get("isMajorityOwnerForeign")
        hasForeignOperations = personal.get("hasForeignOperations")

        # Are you an authorized representative of the organization? Yes
        send_click(driver, '//*[@id="stack-10"]/div/ul/li[1]')

        # First Name
        write_delay(
            driver,
            '//*[@id="tru-core-input-4"]',
            firstName
        )

        # Last Name
        write_delay(
            driver,
            '//*[@id="tru-core-input-5"]',
            lastName
        )

        # Email Address
        write_delay(
            driver,
            '//*[@id="tru-core-input-6"]',
            email
        )

        # Are any of the organization's majority owners a foreign individual/entity?
        if isMajorityOwnerForeign == "Yes":
            send_click(driver, '//*[@id="tru-core-button-toggle-3"]')
        else:
            send_click(driver, '//*[@id="tru-core-button-toggle-4"]')

        # Does the organization have foreign operations?
        if hasForeignOperations == "Yes":
            send_click(driver, '//*[@id="tru-core-button-toggle-5"]')
        else:
            send_click(driver, '//*[@id="tru-core-button-toggle-6"]')

        # Start application
        send_click(driver, '//*[@id="cta-21"]/button')
        random_sleep(1)
        send_click(driver, '//*[@id="tru-core-button-toggle-8"]')
        random_sleep(1)
        # ZIP code
        write_delay(
            driver,
            '//*[@id="tru-core-input-8"]',
            personal.get("zipCode")
        )
        random_sleep(1)
        send_click(driver, '//*[@id="cta-23"]/button')
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="tru-core-input-17"]',
        )
        random_sleep(1)
        send_click(driver, '//*[@id="9-option-id-5"]')
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="tru-core-input-10"]',
            personal.get("organizationName")
        )
        random_sleep(1)
        send_click(driver, '//*[@id="tru-core-input-21"]')
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="18-option-id-2"]',
        )
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="tru-core-input-39"]',
            personal.get("ssn")
        )
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="tru-core-input-11"]',
            personal.get("phone")
        )
        random_sleep(1)
        
        # Industry types
        send_click(driver, '//*[@id="tru-core-input-22"]')
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="19-option-id-1084"]',
        )
        random_sleep(1)
        # Date
        write_delay(
            driver,
            '//*[@id="tru-core-input-12"]',
            personal.get("date")
        )
        random_sleep(1)
        
        # State 
        select_element = driver.find_element(
            by=By.XPATH,
            value='//*[@id="tru-core-input-20"]'
        )
        driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, personal.get("state"))

        random_sleep(1)

        # number of employees
        write_delay(
            driver,
            '//*[@id="tru-core-input-14"]',
            personal.get("numOfEmployees")
        )
        random_sleep(1)
        # Annual sales
        write_delay(
            driver,
            '//*[@id="tru-core-input-15"]',
            personal.get("annualSales")
        )
        random_sleep(1)
        
        # activitiesv
        write_delay(
            driver,
            '//*[@id="tru-core-text-area-16"]',
            personal.get("activities")
        )
        random_sleep(1)
        
        # Street address
        write_delay(
            driver,
            '//*[@id="grid-52"]/div[1]/input',
            personal.get("address")
        )
        random_sleep(1)
        
        send_click(driver,'//*[@id="cta-25"]/button')
        random_sleep(1)
        send_click(driver,'//*[@id="cta-47"]/button')
        random_sleep(1)
        send_click(driver,'//*[@id="tru-core-button-toggle-10"]')
        random_sleep(1)
        send_click(driver,'//*[@id="cta-49"]/button')
        random_sleep(1)

        # SSN
        write_delay(
            driver,
            '//*[@id="tru-core-input-42"]',
            personal.get("ssn")
        )
        random_sleep(1)
        # dob
        write_delay(
            driver,
            '//*[@id="tru-core-input-34"]',
            personal.get("dob")
        )
        random_sleep(1)
        
        # Owner
        send_click(
            driver,
            '//*[@id="tru-core-input-43"]',
        )
        random_sleep(1)
        send_click(driver, '//*[@id="35-option-id-26"]')
        random_sleep(1)
        
        # Citizenship
        send_click(
            driver,
            '//*[@id="tru-core-input-44"]',
        )
        random_sleep(1)
        send_click(driver, '//*[@id="36-option-id-3"]')
        random_sleep(1)
        
        # phone
        write_delay(
            driver,
            '//*[@id="tru-core-input-38"]',
            personal.get("phone")
        )
        random_sleep(1)
        
        # Address
        write_delay(
            driver,
            '//*[@id="grid-71"]/div[1]/input',
            personal.get("address")
        )
        random_sleep(1)
        
        # city
        write_delay(
            driver,
            '//*[@id="tru-core-input-48"]',
            personal.get("city")
        )
        random_sleep(1)
        # State 
        select_element = driver.find_element(
            by=By.XPATH,
            value='//*[@id="tru-core-input-52"]'
        )
        random_sleep(1)
        driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, personal.get("state"))

        random_sleep(1)
        # zip
        write_delay(
            driver,
            '//*[@id="tru-core-input-50"]',
            personal.get("zipCode")
        )
        random_sleep(1)
        # Resident since
        write_delay(
            driver,
            '//*[@id="tru-core-input-51"]',
            personal.get("residentSince")
        )
        
        # Consent to Use Electronic Signatures and Records
        random_sleep(1)
        send_click(driver,'//*[@id="cta-63"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-53"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="tru-core-checkbox-input-3"]')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-51"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-67"]/button')
        random_sleep(2)
        send_click(driver,'//*[@id="tru-core-checkbox-input-5"]')
        random_sleep(2)
        send_click(driver,'//*[@id="cta-70"]/button')
        random_sleep(10)
        random_sleep(10)

        full_name = f"{firstName} {lastName}"
        card_name = "Truist Business Travel Rewards"
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
        card_name = "Truist Business Travel Rewards"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
