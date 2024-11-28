from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Bank Of America Premium Rewards
# -----------------------------------------------------------------

def premiumRewards(driver, data, product_id):
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
        
        driver.get(
            "https://www.bankofamerica.com/credit-cards/products/premium-rewards-credit-card/"
        )
        random_sleep(2)
        send_click(
            driver,
            '//*[@id="applyNow_engagement"]'
        )
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
     
        
        # First Name
        write_delay(
            driver,
            '//*[@id="customerFirstName"]',
            firstName
        )

        random_sleep(1)
      

        # Last name
        write_delay(
            driver,
            '//*[@id="customerLastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
        # Email
        write_delay(
            driver,
            '//*[@id="customerEmailAddress"]',
            email
        )

        random_sleep(1)
        
        # Phone number
        write_delay(
            driver,
            '//*[@id="customerPrimaryPhoneNumber"]',
            mobileNumber
        )
        
        random_sleep(1)
        
        # Home address
        write_delay(
            driver,
            '//*[@id="customerResidentialAddressOne"]',
            homeAddress
        )

        random_sleep(1)

        # ZIP Code
        write_delay(
            driver,
            '//*[@id="customerAddressInput"]',
            zipcode
        )

        random_sleep(1)

        # City
        write_delay(
            driver,
            '//*[@id="customerAddressCity"]',
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
                    value='//*[@id="customerAddressState"]'
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

        random_sleep(2)
        
        # Select mobile
        send_click(driver, '//*[@id="phoneNumberMobile"]')
        random_sleep(1)
        # send_click(driver, '//*[@id="phoneNumberMobile"]')
        
        random_sleep(2)
        
        # Continue button
        send_click(driver, '//*[@id="icaiContinueButton"]')
        
        random_sleep(2)
        
        # ---------------------------
        # Page - 2
        # ---------------------------
        
        # US Citizen
        send_click(driver, '//*[@id="customerUsCitizenYes"]')
        random_sleep(2)
        
        # Dual Citizen
        send_click(driver, '//*[@id="customerDualCitizenshipNo"]')
        random_sleep(2)
       
        # SSN Number
        write_delay(
            driver,
            '//*[@id="customerSocialSecurityNumber"]',
            ssn
        )
        random_sleep(1)
        
        # Residence
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="customerCountryOfResidence"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value("1000249")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Date of birth
        write_delay(
            driver,
            '//*[@id="customerBirthDate"]',
            dob
        )
        
        
        
        # Contunie
        send_click(driver, '//*[@id="icaiContinueButton"]')
        random_sleep(2)
        random_sleep(1)
        
        # ------------------------
        # Page - 3
        # ------------------------
        
        # Employee status
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="employmentStatus"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value("Employed")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(2)
        
        
        
        # Gross annual income
        # send_click(driver, '//*[@id="personalInfo.totalAnnualIncome"]')
        write_delay(
            driver,
            '//*[@id="annualSalary"]',
            grossIncome
        )
        
        random_sleep(2)
        
        # Income status
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                select_element = driver.find_element(
                    by=By.XPATH,
                    value='//*[@id="incomeSource"]'
                )
                # driver.execute_script(
                #     "arguments[0].setAttribute('value',arguments[1])", 
                #     select_element, 
                #     state
                # )

                select = Select(select_element)
                select.select_by_value("EmploymentIncome")
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(2)
        
        # Monthly income
        write_delay(
            driver,
            '//*[@id="monthlyHousingPayment"]',
            monthlymortage
        )
        
        random_sleep(2)
        
        # Occupation
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

        
        
        # Continue button
        send_click(driver, '//*[@id="icaiContinueButton"]')
        random_sleep(2)
        random_sleep(2)
        
        # -------------------------
        # Page - 4
        # -------------------------
        
        # Agree and contunie
        send_click(driver, '//*[@id="socialSecurityVerificationCheckbox"]')
        random_sleep(1)
        
        # Contunie
        send_click(driver, '//*[@id="termsAndConditionsCheckBox"]')
        random_sleep(2)
        
        # T&C
        # send_click(driver, '//*[@id="getinfo-render"]/div[2]/div[2]/div[3]/div/label')
        # random_sleep(2)
        
        
        # Submit
        send_click(driver, '//*[@id="icaiContinueButton"]')
        random_sleep(2)
        random_sleep(2)
        
        # -------------------
        # Page - 5
        # -------------------
        
        # Submit
        send_click(driver, '//*[@id="icaiContinueButton"]')
        random_sleep(2)
        random_sleep(2)
        
        # -------------------
        # Page - 6
        # -------------------
        
        # Submit
        send_click(driver, '//*[@id="consentCheckbox"]')
        random_sleep(2)
        send_click(driver, '//*[@id="continueBtn"]')
        random_sleep(2)
        random_sleep(2)
        
        # -------------------
        # Page - 7
        # -------------------
        # OTP verification
        send_click(driver, '//*[@id="sendCodeBtn"]')
        

        random_sleep(15)
        random_sleep(1)
        
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Bank Of America Premium Rewards"
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
        card_name = "Bank Of America Premium Rewards"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
