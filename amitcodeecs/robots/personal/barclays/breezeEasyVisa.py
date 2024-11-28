from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Barclays Breeze Easy Visa Credit Card
# -----------------------------------------------------------------

def breezeEasyVisa(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "occupation": "Agriculture",
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
        #         "membershipNumber": 7349303041,
        #         "employmentType": "EMPLOYED",
        #         "state": 'AK',
        #         "zipcode": 99501,
        #         "city": "Jaipur",
        #         "homeAddress": "123 Main St., Apt 4B, New York",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        # product_id = "668fb416133bed94c15bad51"
        
        driver.get(
            "https://cards.barclaycardus.com/credit-card/5b7efc4e-56c1-4c44-a081-2c90402a1a1c?referrerid=BCSCD&xsessionid=C037C94A5E8F88E55E75D0B086ED0678"
        )
        # send_click(
        #     driver,
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)

        occupation = data.get("personal").get("position")
        membershipNumber = data.get("personal").get("membershipNumber")
        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        grossIncome = data.get("personal").get("householdIncome")
        monthlymortage = data.get("personal").get("monthlyPayment")

        random_sleep(20)

        # First Name
        write_delay(
            driver,
            '//*[@id="firstName"]',
            firstName
        )

        random_sleep(1)

        # Last name
        write_delay(
            driver,
            '//*[@id="lastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)

        # Date of birth
        write_delay(
            driver,
            '//*[@id="dateOfBirth"]',
            dob
        )
        random_sleep(1)
        random_sleep(1)
        
        # Email
        write_delay(
            driver,
            '//*[@id="email"]',
            email
        )

        random_sleep(1)
        random_sleep(1)

        # Phone number
        write_delay(
            driver,
            '//*[@id="primaryPhone"]',
            mobileNumber
        )
        
        # Home address
        write_delay(
            driver,
            '//*[@id="addressLine1"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="zip"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="city"]',
            city,
            clear=True
        )

        random_sleep(1)

        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="state"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        # SSN Number
        write_delay(
            driver,
            '//*[@id="socialSecurityNumber"]',
            ssn
        )
        
        random_sleep(2)
        random_sleep(2)
        # Continue button
        send_click(driver, '//*[@id="continue"]')

        random_sleep(2)
        random_sleep(2)
        
        # ------------------------
        # Page 2
        # ------------------------
        
        # Financial information
        send_click(driver, '//*[@id="incomeOtherSource-T"]')
        
        # Occupation
        random_sleep(2)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="occupation"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value(occupation)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        # Gross annual income
        write_delay(
            driver,
            '//*[@id="grossIncome"]',
            grossIncome
        )

        random_sleep(1)
        # Monthly mortage income
        write_delay(
            driver,
            '//*[@id="monthlyHousingPayment"]',
            monthlymortage
        )
        random_sleep(1)
        
        # membership number
        random_sleep(1)
        # write_delay(
        #     driver,
        #     '//*[@id="memberid"]',
        #     membershipNumber
        # )
        random_sleep(1)
        random_sleep(1)
        
        # Continue button
        send_click(driver, '//*[@id="continue"]')
        
        # ----------------------------
        # Page 3
        # ----------------------------
        random_sleep(1)
        # Check box
        send_click(driver, '//*[@id="electronicDelivery-container"]/label/span[1]')
        
        random_sleep(1)
        # Apply button
        send_click(driver, '//*[@id="applyNow"]')
        
        random_sleep(15)
        # --------------------------------
        # Verify popup
        # --------------------------------
        
        random_sleep(1)
        # Verify address
        send_click(driver, '//*[@id="primaryAddressValidation-step-radio-entered-address"]')
        random_sleep(1)
        random_sleep(1)
        
        # Done
        send_click(driver, '//*[@id="navigation-button"]')
        random_sleep(1)
        
        # ----------------------
        # Card design
        # ----------------------
        # send_click(driver, '//*[@id="app"]/div/div/div/div[3]/div/div[2]/div/button')

        random_sleep(1)


        random_sleep(1)

        random_sleep(20)


        random_sleep(1)

        random_sleep(1)

        random_sleep(2)
        random_sleep(1)
        
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Barclays Breeze Easy Visa Credit Card"
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
        card_name = "Barclays Breeze Easy Visa Credit Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
