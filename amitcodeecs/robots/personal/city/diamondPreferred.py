from Utils.random_sleep import random_sleep
from selenium.webdriver.common.by import By
from Utils.spawn_driver import start
from Utils.upload_screenshots import upload_screenshot
from selenium.webdriver.support.ui import Select
from Utils.write_delay import write_delay
from Utils.send_click import send_click
import traceback

# -----------------------------------------------------------------
# City Diamond Preferred Credit Card
# -----------------------------------------------------------------

def diamondPreferred(driver, data, product_id):
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
        driver.get(
            "https://online.citi.com/US/ag/cards/application?app=UNSOL&HKOP=608d295cca6a832d9455f97709fe858e684350d1359860de82b2b8a07336a954&ID=3000&ProspectID=P7vm8OMyxPMEHjunGmpiySE3PhfRnMtH&intc=7~1~64~1~DPO~1~CMSDefaultOffer&pid=257&afc=1A2&adobe_mc=MCMID%3D83143937576011983374238790889900988858,MCAID%3DNONE"
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
        housingStatus = data.get("personal").get("housingStatus")
        housingStatusDict = {"own": "OWN", "rent": "RENT"}

        employmentTypeDict = {
            "full-time": "EMPLOYED",
            "part-time": "EMPLOYED",
            "freelance": "EMPLOYED",
            "internship": "EMPLOYED",
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
        
        # Date of birth
        write_delay(
            driver,
            '//*[@id="dob"]', 
            dob
        )
        random_sleep(1)
        random_sleep(1)
        
        
        
        # Security questions
        random_sleep(1)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="securityWordHint-button-value"]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="cds-option2-4"]'
                )
                random_sleep(1)
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application/cds-row/div/cds-column[2]/div/cds-row/div/div[2]/form/div[2]/cds-row[1]/div/cds-column[6]/cds-form-field/div[2]/cds-dropdown2'
                # )
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="applicant.address.0-addressStateCode"]'
                # )
                # driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                
                # select = Select(select_element)
                # select.select_by_value(housingStatusDict.get(housingStatus))
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                retry_count += 1
                random_sleep(0.1)
        random_sleep(1)
        
        # Mother name
        write_delay(
            driver,
            '//*[@id="securityWord"]',
            motherMaidenName
        )
        random_sleep(1)
        
        # SSN Number
        write_delay(
            driver, 
            '//*[@id="ssnNo"]', 
            ssn
        )

        random_sleep(1)
        
        # Home address
        write_delay(
            driver,
            '//*[@id="streetAddress"]', 
            homeAddress
        )

        random_sleep(1)
        
        # ZIP Code
        write_delay(
            driver, 
            '//*[@id="zipCode"]', 
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
                send_click(
                    driver,
                    '//*[@id="state-button-value"]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="cds-option2-16"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application/cds-row/div/cds-column[2]/div/cds-row/div/div[2]/form/div[2]/cds-row[1]/div/cds-column[6]/cds-form-field/div[2]/cds-dropdown2'
                )
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="applicant.address.0-addressStateCode"]'
                # )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

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
            '//*[@id="mobileNo"]', 
            mobileNumber
        )

        random_sleep(1)
        
        # Checkbox One
        send_click(
            driver,
            '//*[@id="tNCAnchorBlock"]/div[3]/cds-column/fieldset[1]/div[2]/cds-form-field/div[2]',
        )
        random_sleep(1)
        
        
        # Marriott Bonvoy number
        # write_delay(
        #     driver, 
        #     '//*[@id="marriottBonvoyId-text-validate-input-field"]', 
        #     bonvoyNumber
        # )

        random_sleep(1)
        

        # # Employment status
        # send_click(
        #     driver,
        #     '//*[@id="yourInfoCommand"]/div[3]/fieldset/div[2]/div[1]/div/div/div/div/div'
        # )
        # random_sleep(1)
        # retry_count = 0
        # while retry_count < 600:
        #     try:
        #         select_element = driver.find_element(
        #             by=By.XPATH, 
        #             value='//*[@id="yourInfoCommand"]/div[3]/fieldset/div[2]/div[1]/div/div/div/div/div'
        #         )
        #         select = Select(select_element)
        #         select.select_by_value(employmentTypeDict.get(employmentType))
        #         break
        #     except:
        #         retry_count += 1
        #         random_sleep(0.1)
        # random_sleep(1)
        
        # Gross annual income
        write_delay(
            driver,
            '//*[@id="totalAnnualIncome"]',
            grossIncome
        )
        
        
        random_sleep(1)
        # Monthly mortage income
        write_delay(
            driver,
            '//*[@id="monthlyRent"]',
            monthlymortage
        )


        random_sleep(1)

        # I Agree
        try:
            send_click(driver, '//*[@id="tNCAnchorBlock"]/div[3]/cds-column/fieldset[2]/div[2]')
        except:
            driver.save_screenshot(
                f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - City Diamond Preferred Credit Card.png"
            )
        random_sleep(1)
        
        # Submit button
        send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-apply-card-flow-resolver/div/app-card-application/cds-row/div/cds-column[2]/div/cds-row/div/div[2]/form/div[7]/button')
       
        # ----------------------
        # Page - 2
        # ----------------------
        random_sleep(1)
        
        # Home address
        write_delay(
            driver,
            '//*[@id="cds-input-1"]', 
            homeAddress
        )

        random_sleep(1)
        
        # ZIP Code
        write_delay(
            driver, 
            '//*[@id="cds-input-3"]', 
            zipcode
        )

        random_sleep(1)
        
        # City
        write_delay(
            driver,
            '//*[@id="cds-input-4"]',
            city, 
            clear=True
        )

        random_sleep(1)
        
        # State
        random_sleep(2)
        retry_count = 0
        while retry_count < 600:
            try:
                send_click(
                    driver,
                    '//*[@id="state"]/div[2]'
                )
                random_sleep(1)
                send_click(
                    driver,
                    '//*[@id="cds-option2-75"]'
                )
                random_sleep(1)
                select_element = driver.find_element(
                    by=By.XPATH, 
                    value='//*[@id="CdsDropdown2_4"]'
                )
                # select_element = driver.find_element(
                #     by=By.XPATH, 
                #     value='//*[@id="applicant.address.0-addressStateCode"]'
                # )
                driver.execute_script("arguments[0].setAttribute('value',arguments[1])",select_element, state)
                
                # select = Select(select_element)
                # select.select_by_value(state)
                break
            except:
                driver.execute_script("window.scrollBy(0,5)")
                random_sleep(0.1)
                retry_count += 1

        random_sleep(1)
        
        # Submit button
        send_click(driver, '//*[@id="maincontent"]/div/div/div/app-apply-credit/div/citi-simple-layout/app-card-pend-resolution/cds-row/div/cds-column[2]/div/form/cds-row[3]/div/cds-column/button')
       

        random_sleep(10)
        random_sleep(1)

        # driver.save_screenshot(f"{data.get('preApproval').get('firstName')+data.get('preApproval').get('lastName')} - Chase Freedom.png")
        full_name = (
            data.get("preApproval").get("firstName")
            + " "
            + data.get("preApproval").get("lastName")
        )
        card_name = "City Diamond Preferred Credit Card"
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
        card_name = "City Diamond Preferred Credit Card"

        filepath = f"FinalScreenshots/personal/{full_name} - {card_name}.png"
        try:
            driver.save_screenshot(filepath)
            flag = 0
        except:
            flag = 1
            filepath = ""
        upload_screenshot(filepath, data.get(
            "application_id"), product_id, flag)
