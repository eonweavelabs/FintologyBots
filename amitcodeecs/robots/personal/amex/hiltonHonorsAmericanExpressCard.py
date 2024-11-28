from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Amex Hilton Honors American Express Card
# -----------------------------------------------------------------

def hiltonHonorsAmericanExpressCard(driver, data, product_id):
    try:
        # data = {
        #     "email": "bhawani@gmail.com",
        #     "personal": {
        #         "occupation": "AAAC",
        #         "bankOwned": "SAVINGS",
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
        
        product_id = "668fb416133bed94c15bad51"
        
        driver.get(
            "https://www.americanexpress.com/us/credit-cards/card-application/apply/hilton-honors-credit-card/25330-10-0?pmccode=117&intlink=US-Axp-Shop-Consumer-PDP-HiltonHonors-Prospect-ApplyNow-SideRail#/"
        )
        # send_click(
        #     driver,
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)
        
        occupation = data.get("personal").get("position")
        bankOwned = data.get("personal").get("bankOwned")
        membershipNumber = data.get("personal").get("membershipNumber")
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
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

        # Start a new application
        # send_click(driver, '//*[@id="close-banner-link"]')
        # random_sleep(2)
        
        # Click on full name
        # send_click(driver, '//*[@id="personalInfo.fullName.firstName"]')
        # random_sleep(2)
        
        # First Name
        write_delay(
            driver,
            '//*[@id="personalInfo.fullName.firstName"]',
            firstName
        )

        random_sleep(1)

        # Last name
        write_delay(
            driver,
            '//*[@id="personalInfo.fullName.lastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
        # Date of birth
        write_delay(
            driver,
            '//*[@id="personalInfo.dateOfBirth"]',
            dob
        )
        random_sleep(1)
        
        # Email
        write_delay(
            driver,
            '//*[@id="personalInfo.email"]',
            email
        )

        random_sleep(1)
        
        # Phone number
        write_delay(
            driver,
            '//*[@id="personalInfo.phoneNumber.number"]',
            mobileNumber
        )
        
        random_sleep(1)
        
        # Home address
        write_delay(
            driver,
            '//*[@id="personalInfo.homeAddress.streetAddress"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="personalInfo.homeAddress.zipCode"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="personalInfo.homeAddress.city"]',
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
                    value='//*[@id="personalInfo.homeAddress.state"]'
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


        
        random_sleep(1)

        
        
       
        # SSN Number
        write_delay(
            driver,
            '//*[@id="personalInfo.ssn"]',
            ssn
        )
        random_sleep(1)
        random_sleep(1)
        
        # Gross annual income
        # send_click(driver, '//*[@id="personalInfo.totalAnnualIncome"]')
        write_delay(
            driver,
            '//*[@id="personalInfo.totalAnnualIncome"]',
            grossIncome
        )
        
        random_sleep(2)
        
        # Income Source
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="personalInfo.incomeSource"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value("EMP")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(2)
        
        # Hilton honor 
        # send_click(driver, '//*[@id="mainContent"]/div/div[1]/div[3]/div[1]/div[1]/div/dls-cps-personal-info-form/div/div/div[2]/react-prospect-application/div/form/div/div/div[2]/div[3]/div/fieldset/div/div[2]/label')
        random_sleep(2)
        
        # Continue button
        send_click(driver, '//*[@id="mainContent"]/div/div[1]/div[3]/div[1]/div[1]/div/div[3]/react-prospect-application/div/form/div/div/div[3]/div/div/div/button')
        random_sleep(2)
        
        # --------------------
        # Page - 2
        # --------------------
        
        # Agree and contunie
        send_click(driver, '//*[@id="submit"]')
        random_sleep(10)
        
        # Contunie
        # send_click(driver, '//*[@id="getinfo-render"]/div[2]/div/div[2]/div/div/div/div[1]/div/div[2]/button')
        # random_sleep(2)
        
        # T&C
        # send_click(driver, '//*[@id="getinfo-render"]/div[2]/div[2]/div[3]/div/label')
        # random_sleep(2)
        
        
        # Submit
        # send_click(driver, '//*[@id="getinfo-render"]/div[3]/div[2]/button[1]')
        # random_sleep(2)
        
        # Bank name
        # write_delay(
        #     driver,
        #     '//*[@id="siteSearch"]',
        #     "BOB"
        # )
        
        # Bank name
        # write_delay(
        #     driver,
        #     '//*[@id="siteSearch"]',
        #     "BOB"
        # )
        
        random_sleep(2)
        
        
        random_sleep(15)
        random_sleep(1)
        
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Amex Hilton Honors American Express Card"
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
        card_name = "Amex Hilton Honors American Express Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
