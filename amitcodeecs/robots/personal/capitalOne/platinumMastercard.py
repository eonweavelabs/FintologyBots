from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# Capital One Platinum Mastercard
# -----------------------------------------------------------------

def platinumMastercard(driver,data, product_id):
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
        #         "state": 'DC',
        #         "zipcode": 20500,
        #         "city": "Washington",
        #         "homeAddress": "1600 Pennsylvania Avenue NW",
        #         "motherMaidenName": "motherMaidenName",
        #     }
        # }
        driver.get(
            "https://applynow.capitalone.com/?productId=29615"
        )
        # send_click(
        #     driver, 
        #     '//*[@id="main-content"]/section[1]/div/div[1]/div[2]/div/div[2]/div/div[2]/a'
        # )
        random_sleep(15)

        # citizenship = data.get("personal").get("citizenship")
        firstName = data.get("personal").get("firstName")
        middleName = data.get("personal").get("middleName")
        lastName = data.get("personal").get("lastName")
        dob = data.get("personal").get("dob")
        motherMaidenName = data.get("personal").get("motherMaidenName")
        ssn = data.get("personal").get("ssn")
        homeAddress = data.get("personal").get("homeAddress")
        city = data.get("personal").get("city")
        zipcode = data.get("personal").get("zipcode")
        state = data.get("personal").get("state")
        email = data.get("email")
        employmentType = data.get("personal").get("employmentType")
        mobileNumber = data.get("personal").get("mobileNumber")
        bonvoyNumber = data.get("personal").get("bonvoyNumber")
        residencyStatus = data.get("personal").get("housingStatus")
        grossIncome = data.get("personal").get("householdIncome")
        monthlymortage = data.get("personal").get("monthlyPayment")
        bankAccount = data.get("personal").get("bankAccount")
        occupation = data.get("personal").get("position")
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMP",
            "part-time": "EMP",
            "freelance": "EMP",
            "internship": "EMP",
        }
        
        bankAccountDist = {
            "checking-and-savings": "CAS",
            "checking": "CHK",
            "savings": "SAV",
            "neither": "NON",
        }
        
        random_sleep(20)
        
        # First Name
        write_delay(
            driver, 
            '//*[@id="firstName"]', 
            firstName
        )
        
        random_sleep(1)
        
        # Middle name
        if len(middleName):
            write_delay(
                driver, 
                '//*[@id="middleName"]', 
                middleName
            )
            random_sleep(1)
            # driver.find_element(by=By.XPATH, value="//input[@name='middleName']").send_keys(Keys.TAB)
            random_sleep(1)
        else:
            print("Middle name not provided. Skipping...")
            
        # Last name 
        write_delay(
            driver, 
            '//*[@id="lastName"]',
            lastName
        )
        random_sleep(1)
        random_sleep(1)
        
        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[3]/div/div/button'
        )
        
        random_sleep(1)
        # --------------------
        # Page - 2
        # --------------------
        
        #  U.S. citizen? yes
        send_click(
            driver, 
            '//*[@id="label-usacitizen-radio-0"]'
        )
        
        random_sleep(1)
        
        #  citizenship in another country? = > No
        send_click(
            driver, 
            '//*[@id="label-dualcitizen-radio-1"]'
        )
        random_sleep(1)
        
        
        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        # --------------------
        # Page - 3
        # --------------------
        
       
        random_sleep(1)
        
        # Home address
        write_delay(
            driver,
            '//*[@id="address.residential.addressLine1"]', 
            homeAddress
        )

        random_sleep(1)
        
        # ZIP Code
        write_delay(
            driver, 
            '//*[@id="address.residential.zipcode"]', 
            zipcode
        )

        random_sleep(1)
        
        # City
        write_delay(
            driver,
            '//*[@id="address.residential.city"]',
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
                    value='//*[@id="address.residential.state"]'
                )
                select = Select(select_element)
                select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        # --------------------
        # Page - 4
        # --------------------

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
            '//*[@id="phone"]', 
            mobileNumber
        )
        
        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        # --------------------
        # Page - 5
        # --------------------
        
        # Employment status
        random_sleep(1)
        send_click(
            driver,
            '//*[@id="label-employmentstatus-radio-0"]'
        )

        random_sleep(1)
        random_sleep(1)
        
        # Occupation
        write_delay(
            driver,
            '//*[@id="occupation"]',
            occupation
        )
        random_sleep(1)

        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        
        # --------------------
        # Page - 6
        # --------------------
        
        # Gross annual income
        random_sleep(1)
        write_delay(
            driver,
            '//*[@id="totalAnnualIncome"]',
            grossIncome
        )
        
        
        random_sleep(1)
        # Monthly mortage income
        write_delay(
            driver,
            '//*[@id="monthlyRentMortgage"]',
            monthlymortage
        )

        random_sleep(1)
        
        random_sleep(1)

        #  Contunue
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        
        # --------------------
        # Page - 7
        # --------------------
        
        
        #  Bank account
        send_click(
            driver, 
            '//*[@id="label-bankaccountsradio-radio-0"]'
        )
        random_sleep(1)
        random_sleep(1)
        
        #  Contunie
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        
        # --------------------
        # Page - 8
        # --------------------
        
        random_sleep(1)
        
        #  Contunie
        # send_click(
        #     driver, 
        #     '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        # )
        
        random_sleep(1)
        
        # --------------------
        # Page - 9
        # --------------------
        
        random_sleep(1)
        
        # Date of birth
        write_delay(
            driver,
            '//*[@id="dateOfBirth"]', 
            dob
        )
        random_sleep(1)
        
        
        # SSN Number
        write_delay(
            driver, 
            '//*[@id="socialSecurity"]', 
            ssn
        )
        
        random_sleep(1)
        
        # Confirm SSN Number
        write_delay(
            driver, 
            '//*[@id="confirmSocialSecurity"]', 
            ssn
        )
        
        random_sleep(1)
        
        
        #  Contunie
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/button'
        )
        
        random_sleep(1)
        
        
        # --------------------
        # Page - 10
        # --------------------
        
        # Checkbox
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/label'
        )

        random_sleep(1)
        
        # Checkbox - 2
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/label'
        )

        random_sleep(1)
        
        #  Contunie
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/div[2]/div/div/div[2]/button'
        )
        
        random_sleep(1)
        
        
        # --------------------
        # Page - 11
        # --------------------
        
        random_sleep(1)
        
        # Submit
        send_click(
            driver, 
            '//*[@id="section-card"]/div[2]/div/form/div/div[2]/div/div/div[3]/div/div/div[4]/div/button'
        )
        
        random_sleep(1)
        random_sleep(10)
        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "Capital One Platinum Mastercard"
        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        # product_id = "661cb8fd5418a96c1c8c25f5"    
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
        card_name = "Capital One Platinum Mastercard"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)

