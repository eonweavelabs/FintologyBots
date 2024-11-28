from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Discover It Cash Back
# -----------------------------------------------------------------

def itCashBack(driver, data, product_id):
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
        # product_id = "668fb416133bed94c15bad51"
        print(123)
        driver.get(
            "https://www.discovercard.com/application/website/apply?adpt=mn&srcCde=GJVP&icmpgn=APPLY_NOW_TOP_BTN&_gl=1*ns4tag*_gcl_au*ODU1ODIwMDIyLjE3MzIyMDc3MDc.*_ga*NTk1MzMwNDYxLjE3MzIyMDc3MDc.*_ga_3MJNPV4VSE*MTczMjIwNzcwNy4xLjAuMTczMjIwNzcwNy42MC4wLjA."
        )
        print(123)
        # send_click(
        #     driver,
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)

        employmentType = data.get("personal").get("employmentType")
        householdIncome = data.get("personal").get("householdIncome")
        monthlyPayment = data.get("personal").get("monthlyPayment")
        position = data.get("personal").get("position")
        housingStatus = data.get("personal").get("housingStatus")
        employmentTypeDict = {
            "full-time": "FULL_TIME",
            "part-time": "PART_TIME",
            "freelance": "OTHER",
            "internship": "OTHER",
        }
        housingStatusDict = {
            "own": 1,
            "rent": 2, 
            "other": 3
        }
        educationDict = {
            "bachelor-degree": "BACHELORS_DEGREE",
            "high-school-diploma-or-GED": "HIGH_SCHOOL",
            "advanced-or-graduate-degree": "GRADUATE_DEGREE",
            "less-than-high-school-diploma": "LESS_THAN_HIGH_SCHOOL",
            "some-college-or-associate-degree": "ASSOCIATE_DEGREE",
        }
        us_citizen = True
        
        occupation = data.get("personal").get("position")
        bankOwned = data.get("personal").get("bankOwned")
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

        # Click on full name
        send_click(driver, '//*[@id="full-name"]')
        random_sleep(2)
        
        # First Name
        write_delay(
            driver,
            '//*[@id="first-name"]',
            firstName
        )

        random_sleep(1)

        # Last name
        write_delay(
            driver,
            '//*[@id="last-name"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
         # Home address
        write_delay(
            driver,
            '//*[@id="address"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="zip-code"]',
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


        # Date of birth
        write_delay(
            driver,
            '//*[@id="date-of-birth"]',
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
            '//*[@id="primary-phone"]',
            mobileNumber
        )
        
       
        # SSN Number
        write_delay(
            driver,
            '//*[@id="social-security-number"]',
            ssn
        )
        
        
        # Employee-ment stastus
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="employment-status"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value("FULL_TIME")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1


        # Gross annual income
        send_click(driver, '//*[@id="total-gross-income"]')
        write_delay(
            driver,
            '//*[@id="total-gross-income"]',
            grossIncome
        )
        
        # Occupation
        random_sleep(2)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="occupation-code"]'
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

        random_sleep(1)
        
        # Highest level of education
        random_sleep(2)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="highest-level-of-education"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value('BACHELORS_DEGREE')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        
        # Monthly mortage income
        write_delay(
            driver,
            '//*[@id="monthly-house-or-rent-payment"]',
            monthlymortage
        )
        random_sleep(1)
        
        # Housing status
        random_sleep(2)
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="housing-status"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value('HOME')
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1


        random_sleep(1)
        
        random_sleep(2)
        random_sleep(2)
        # Bank account owned
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="bank-accounts-owned-select"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value(bankOwned)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1


        random_sleep(2)
        random_sleep(2)
        # Continue button
        send_click(driver, '//*[@id="agree-terms-and-conditions"]')
        random_sleep(2)
        send_click(driver, '//*[@id="agree-to-paperless-disclosures"]')
        random_sleep(2)
        send_click(driver, '//*[@id="agree-to-ssa"]')
        random_sleep(2)
        random_sleep(2)
        send_click(driver, '//*[@id="submit"]')

        random_sleep(2)
        
        
        random_sleep(15)
        random_sleep(1)
        
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "discover It Cash Back"
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
        card_name = "discover It Cash Back"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
