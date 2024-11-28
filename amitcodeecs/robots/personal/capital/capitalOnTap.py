from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback


# ------------------------------------------------------
# Capital On Tap
# ------------------------------------------------------

def capitalOnTap(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "firstName": "Neha",
        #         "lastName": "lastName",
        #         "dob": "10/06/2000",
        #         "mobileNumber": 7349303040,
        #         "state": "AK",
        #         "zipcode": 85445,
        #         "city": "Jaipur",
        #         "homeAddress": "123 street",
        #     },
        #     "business": {
        #         "legalName": "Business Legal Name",
        #         "tradingName": "Trading Name",
        #         "postcode": "12345",
        #         "buildingName": "Building Name",
        #         "buildingNumber": "123",
        #         "streetName": "Street Name",
        #         "monthlyTurnover": 10000,
        #     },
        #     "credentials": {
        #         "password": "password123",
        #         "confirmPassword": "password123",
        #     }
        # }
        
        driver.get("https://account.capitalontap.com/apps/apply/?userId=3811244069141103&_gl=1*13s0678*_gcl_au*NTI5NTAyMjM4LjE3MjY2NTc3MjE.&_ga=2.24649597.639062880.1727678451-1038805437.1726657721&step=1")
        random_sleep(15)

        firstName = data.get("personal").get("firstName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        mobileNumber = data.get("personal").get("mobileNumber")
        businessLegalName = data.get("business").get("legalName")
        tradingName = data.get("business").get("tradingName")
        businessPostcode = data.get("business").get("postcode")
        buildingName = data.get("business").get("buildingName")
        buildingNumber = data.get("business").get("buildingNumber")
        streetName = data.get("business").get("streetName")
        monthlyTurnover = data.get("business").get("monthlyTurnover")
        password = data.get("credentials").get("password")
        confirmPassword = data.get("credentials").get("confirmPassword")

        random_sleep(20)

        # Email Address
        write_delay(driver, '//*[@id="emailAddress"]', email)
        random_sleep(1)

        # Promo Code (optional)
        # write_delay(driver, '//*[@id="promoCode"]', "")
        # random_sleep(1)

        # Agree to Privacy Policy
        send_click(driver, '//*[@id="agreeToPrivacyPolicy"]')
        random_sleep(1)

        # Consent to Marketing
        send_click(driver, '//*[@id="consentToMarketing"]')
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="__next"]/div[1]/div/div[1]/div[3]/div/div/form/div/button')
        random_sleep(1)

        # Business Legal Name
        write_delay(driver, '//*[@id="businessLegalName"]', businessLegalName)
        random_sleep(1)

        # Trading Name
        # write_delay(driver, '//*[@id="tradingName"]', tradingName)
        # random_sleep(1)

        # Enter Business Address Manually
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[4]/div/div[2]/div/div/div/div[2]/a')
        random_sleep(1)
        # Business Postcode
        # write_delay(driver, '//*[@id="businessAddressSearch"]', 10001)
        # random_sleep(1)

        # Building Name
        write_delay(driver, '//*[@id="businessAddressBuildingName"]', buildingName)
        random_sleep(1)

        # Building Number
        write_delay(driver, '//*[@id="businessAddressBuildingNumber"]', buildingNumber)
        random_sleep(1)

        # Street Name
        write_delay(driver, '//*[@id="businessAddressStreet"]', streetName)
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="businessAddressCity"]', city)
        random_sleep(1)

        # Postcode
        write_delay(driver, '//*[@id="businessAddressPostCode"]', zipcode)
        random_sleep(1)

        # Monthly Turnover
        write_delay(driver, '//*[@id="monthlyTurnover"]', monthlyTurnover)
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[2]/button[1]')
        random_sleep(10)
        
        # manually enter personal address
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[2]/div[2]/div[1]/div/div/div')
        random_sleep(1)
        send_click(driver, '/html/body/div[4]/div/div')
        random_sleep(1)

        # Are you currently a listed director of this business?
        send_click(driver, '//*[@id="isCurrentDirector"]/label[1]')
        random_sleep(1)

        # Title
        # write_delay(driver, '//*[@id="salutation"]', "Mr.")
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[3]/div[1]/div[2]/div/div/div')
        random_sleep(2)
        send_click(driver, '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[1]')
        random_sleep(1)

        # First Name
        write_delay(driver, '//*[@id="firstName"]', firstName)
        random_sleep(1)

        # Middle Name
        # write_delay(driver, '//*[@id="middleName"]', "")
        # random_sleep(1)

        # Last Name
        write_delay(driver, '//*[@id="lastName"]', lastName)
        random_sleep(1)

        # Full Name
        # write_delay(driver, '//*[@id="companyDirector"]', f"{firstName} {lastName}")
        # random_sleep(1)

        # Date of Birth
        write_delay(driver, '//*[@id="dateOfBirth"]', dob)
        random_sleep(1)

        # Mobile Number
        write_delay(driver, '//*[@id="mobilePhone"]', mobileNumber)
        random_sleep(1)

        # Enter manually home address
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[1]/div[5]/div/div[2]/div/div/div/div[2]/a')
        random_sleep(1)

        # Building Name
        write_delay(driver, '//*[@id="personalAddressBuildingName"]', buildingName)
        random_sleep(1)

        # Street Number
        write_delay(driver, '//*[@id="personalAddressBuildingNumber"]', buildingNumber)
        random_sleep(1)

        # Street Name
        write_delay(driver, '//*[@id="personalAddressStreet"]', streetName)
        random_sleep(1)

        # City
        write_delay(driver, '//*[@id="personalAddressCity"]', city)
        random_sleep(1)

        # Postcode
        write_delay(driver, '//*[@id="personalAddressPostCode"]', zipcode)
        random_sleep(1)

        # Continue
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[2]/div/div/div/div/button')
        random_sleep(1)

        # Email Address
        write_delay(driver, '//*[@id="emailAddress"]', email)
        random_sleep(1)

        # Confirm Email Address
        write_delay(driver, '//*[@id="repeatEmailAddress"]', email)
        random_sleep(1)

        # Password
        write_delay(driver, '//*[@id="password"]', password)
        random_sleep(1)

        # Confirm Password
        write_delay(driver, '//*[@id="repeatPassword"]', confirmPassword)
        random_sleep(1)

        # Direct Debit Setup
        send_click(driver, '//*[@id="repaymentOptions"]/label[1]')
        random_sleep(1)

        # Cash from Credit Facility
        send_click(driver, '//*[@id="canSendCashFromCreditFacilityToBank"]/label[2]')  # Assuming NO
        random_sleep(1)

        # Apply Now
        send_click(driver, '//*[@id="__next"]/div[1]/div[3]/div/div/div/div/form/div/div[4]/button[1]')
        random_sleep(1)

        # Screenshot and upload
        full_name = f"{firstName} {lastName}"
        card_name = "Capital On Tap"
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
        card_name = "Capital On Tap"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get("application_id"), product_id, flag)
